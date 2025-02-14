#User story 
# eing ได้เจอแอพหนึ่งที่สนใจ เป็นแอพเกี่ยวกับ poll เธอจึงได้ลองเข้าไปที่เว็บนั้น โดยได้ลองตรวจสอบว่า urls ของเธอชื่อ polls ใหม
# eing ได้เห็นว่ามันเกี่ยวกับแบบสำรวจเธอจึงได้ลองทดสอบเพิ่ม polls เข้าไป
# ใน polls จะมีฟังก์ชันในการเพิ่มคำถามและคำตอบ
# เธอจึงได้ลองเพิ่มคำถามว่ากินข้าวกับอะไรดี และลองเพิ่มคำตอบว่า 1.กระเพรา 2.ไข่เจียว เข้าไป
# เมื่อเธอเพิ่มเสร็จแล้วเธอจึงได้กดปุ่มบันทึก
# เมื่อบันทึกเสร็จระบบจะขึ้นว่าบันทึกเรียบร้อยแล้ว
# ต่อมาเธอได้ลองเข้าไปที่หน้า polls เพื่อดูแบบสอบถามที่ตัวเองสร้างขึ้น
# เธอพบแบบสอบถามมีคำถามว่า กินข้าวกับอะไรดี และพบคำตอบว่า 1.กระเพรา 2.ไข่เจียว
#เธอได้ลองโหวต กระเพราไป
#หลังจากนั้นเธอได้ลองสลับไปดูหน้าผลการตอบ
#เมื่อเข้าไปจะพบว่ามีคนตอบกระเพราขึ้นมา 1 คน
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        # เปิด browser Chrome และตั้ง implicit wait
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_connect_to_polls(self):
        # Step ที่ 1: เข้าเว็บหลักและตรวจสอบ title กับ header ว่ามีคำว่า "polls"
        self.browser.get("http://localhost:8000")
        self.assertIn("polls", self.browser.title.lower())
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("polls", header_text.lower())

    def test_create_poll_and_vote(self):
        # Step ที่ 1: เข้าเว็บหลักแล้วตรวจสอบ header
        self.browser.get("http://localhost:8000")
        self.assertIn("polls", self.browser.title.lower())
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("polls", header_text.lower())
        time.sleep(1)
        
        # Step ที่ 2: คลิกลิงก์เพื่อไปยังหน้าสร้าง Poll ใหม่
        add_poll_link = self.browser.find_element(By.LINK_TEXT, "เพิ่ม Poll")
        add_poll_link.click()
        time.sleep(1)
        
        # Step ที่ 3: กรอกแบบฟอร์มเพิ่ม poll
        question_input = self.browser.find_element(By.ID, "id_question")
        question_input.send_keys("กินข้าวกับอะไรดี")
        choice1_input = self.browser.find_element(By.ID, "id_choice1")
        choice1_input.send_keys("กระเพรา")
        choice2_input = self.browser.find_element(By.ID, "id_choice2")
        choice2_input.send_keys("ไข่เจียว")
        
        # Step ที่ 4: คลิกปุ่ม "บันทึก" เพื่อส่งแบบฟอร์ม
        submit_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'บันทึก')]")
        submit_button.click()
        time.sleep(1)
        
        # Step ที่ 5: ตรวจสอบว่ามีข้อความยืนยัน "บันทึกเรียบร้อยแล้ว" ปรากฏบนหน้าเว็บ
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("บันทึกเรียบร้อยแล้ว", body_text)
        
        # Step ที่ 6: คลิกลิงก์ไปยังหน้ารายการ Polls
        polls_link = self.browser.find_element(By.LINK_TEXT, "Polls")
        polls_link.click()
        time.sleep(1)
        
        # Step ที่ 7: ตรวจสอบว่ามี poll ที่สร้างขึ้นปรากฏอยู่
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กินข้าวกับอะไรดี", body_text)
        self.assertIn("กระเพรา", body_text)
        self.assertIn("ไข่เจียว", body_text)
        
        # Step ที่ 8: คลิกลิงก์ poll ที่มีคำถาม "กินข้าวกับอะไรดี" เพื่อเข้าไปดูรายละเอียดและโหวต
        poll_link = self.browser.find_element(By.LINK_TEXT, "กินข้าวกับอะไรดี")
        poll_link.click()
        time.sleep(1)
        
        # Step ที่ 9: เลือกตัวเลือก "กระเพรา" สำหรับโหวต
        # สมมุติว่า radio button อยู่ก่อน label ที่มีข้อความ "กระเพรา"
        choice_radio = self.browser.find_element(
            By.XPATH, "//label[contains(text(),'กระเพรา')]/preceding-sibling::input[@type='radio']"
        )
        choice_radio.click()
        time.sleep(1)
        
        # Step ที่ 10: คลิกปุ่ม "โหวต" เพื่อส่งโหวต
        vote_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'โหวต')]")
        vote_button.click()
        time.sleep(1)
        
        # Step ที่ 11: ตรวจสอบผลลัพธ์ว่ามีคนโหวต "กระเพรา" 1 คน
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กระเพรา", body_text)
        self.assertIn("1", body_text)

if __name__ == "__main__":  
    unittest.main()

