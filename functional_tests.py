#User story 
# eing ได้เจอแอพหนึ่งที่สนใจ เป็นแอพเกี่ยวกับ poll เธอจึงได้ลองเข้าไปที่เว็บนั้น โดยได้ลองตรวจสอบว่า urls ของเธอชื่อ mypoll ใหม
# เธอเห็นในหน้ามี ข้อความ กินข้าวกับอะไรดีเธอจึงกดเข้าไป
# เธอพบแบบสอบถามมีคำถามว่า กินข้าวกับอะไรดี และพบคำตอบว่า 1.กระเพรา 2.ไข่เจียว
# เธอได้ลองกดปุ่ม vote หลังจากนั้นระบบจะขึ้นว่า You didn't select a choice.
#เธอได้ลองโหวต กระเพราไป
#หลังจากนั้นระบบได้สลับไปดูหน้าผลการตอบ
#เมื่อเข้าไปจะพบว่ามีคนตอบกระเพราขึ้นมา 1 คน
#เธอเห็น ปุ่ม vote again จึงไดเ้ลองกดดู
#เมื่อกดแล้วจะกลับไปที่ หน้าโหวตอีกครั้ง
#รอบนี้เธอจึงลองโหวตไข่เจียวดู
#หลังจากระบบเธอได้สลับไปดูหน้าผลการตอบ
#เมื่อเข้าไปจะพบว่ามีคนตอบขึ้นมา 1 คน
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        # 2) คลิกคำถาม "กินข้าวกับอะไรดี"
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "กินข้าวกับอะไรดี"))
        ).click()

        # 3) ตรวจสอบตัวเลือกมี 'กระเพรา' และ 'ไข่เจียว'
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กินข้าวกับอะไรดี", body_text)
        self.assertIn("กระเพรา", body_text)
        self.assertIn("ไข่เจียว", body_text)

        # 4) กดปุ่ม Vote โดยไม่เลือกอะไร
        vote_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Vote']"))
        )
        vote_button.click()

        # ✅ เช็คว่าหน้ายังอยู่ที่เดิม (หมายถึงไม่มีการเลือกตัวเลือก)
        self.assertIn("mypoll", self.browser.current_url)

        # ✅ เช็คว่ามี error message "You didn't select a choice."
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("You didn't select a choice.", body_text)

        # 5) โหวต 'กระเพรา'
        choice_radio = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='1']"))
        )
        choice_radio.click()
        
        vote_button = self.browser.find_element(By.XPATH, "//input[@type='submit' and @value='Vote']")
        vote_button.click()

        # 6) ตรวจสอบผลโหวตของ 'กระเพรา' -- 1 vote
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "กระเพรา -- 1 vote")
        )

        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("กระเพรา -- 1 vote", body_text)

        # 7) กดปุ่ม "Vote again"
        vote_again_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Vote again?"))
    )
        vote_again_button.click()

        # 8) รอบนี้โหวต 'ไข่เจียว'
        choice_radio = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='2']"))
        )
        choice_radio.click()

        vote_button = self.browser.find_element(By.XPATH, "//input[@type='submit' and @value='Vote']")
        vote_button.click()

        # 9) ตรวจสอบผลโหวตของ 'ไข่เจียว' -- 1 vote
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "ไข่เจียว -- 1 vote")
        )

        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn("ไข่เจียว -- 1 vote", body_text)
        reset_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Reset Votes']"))
        )
        reset_button.click()


if __name__ == "__main__":
    unittest.main()
