#User story 
# eing ได้เจอแอพหนึ่งที่สนใจ เป็นแอพเกี่ยวกับ poll เธอจึงได้ลองเข้าไปที่เว็บนั้น โดยได้ลองตรวจสอบว่า urls ของเธอชื่อ mypoll ใหม
# เธอเห็นในหน้ามี ข้อความ กินข้าวกับอะไรดีเธอจึงกดเข้าไป
# เธอพบแบบสอบถามมีคำถามว่า กินข้าวกับอะไรดี และพบคำตอบว่า 1.กระเพรา 2.ไข่เจียว
#เธอได้ลองโหวต กระเพราไป
#หลังจากนั้นเธอได้ลองสลับไปดูหน้าผลการตอบ
#เมื่อเข้าไปจะพบว่ามีคนตอบกระเพราขึ้นมา 1 คน
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class MyPollTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_eing_mypoll_scenario(self):
        
        # 1) เข้าเว็บ mypoll
        self.browser.get("http://127.0.0.1:8000/mypoll/")
        self.assertIn("mypoll", self.browser.current_url)

        # 2) เห็นคำถาม 'กินข้าวกับอะไรดี' บนหน้า และคลิกเข้าไป
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กินข้าวกับอะไรดี", body_text)

        question_link = self.browser.find_element(By.LINK_TEXT, "กินข้าวกับอะไรดี")
        question_link.click()
        time.sleep(1)

        # 3) พบตัวเลือก 'กระเพรา' และ 'ไข่เจียว'
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กระเพรา", body_text)
        self.assertIn("ไข่เจียว", body_text)

        # 4) โหวต 'กระเพรา'
        choice_radio = self.browser.find_element(
            By.XPATH,
            "//label[contains(text(),'กระเพรา')]/preceding-sibling::input[@type='radio']"
        )
        choice_radio.click()

        vote_button = self.browser.find_element(By.XPATH, "//input[@type='submit' and @value='Vote']")
        vote_button.click()


        # 5) ตรวจสอบว่าผลโหวตของ 'กระเพรา' คือ 1 โหวต
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กระเพรา -- 1 vote", body_text)
        reset_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'Reset Votes')]")
        reset_button.click()

if __name__ == "__main__":
    unittest.main()
