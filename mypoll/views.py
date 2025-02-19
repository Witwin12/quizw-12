from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "mypoll/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "mypoll/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "mypoll/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "mypoll/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("mypoll:results", args=(question.id,)))
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "mypoll/detail.html", {"question": question})

def reset_votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.choice_set.update(votes=0)  # รีเซ็ตทุกตัวเลือกของคำถามนี้ให้เป็น 0
    return HttpResponseRedirect(reverse("mypoll:results", args=(question.id,)))
