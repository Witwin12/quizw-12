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

class User_test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
    def can_connect_to_polls(self):
        # eing ได้เจอแอพหนึ่งที่สนใจ เป็นแอพเกี่ยวกับ poll เธอจึงได้ลองเข้าไปที่เว็บนั้น โดยได้ลองตรวจสอบว่า urls ของเธอชื่อ polls ใหม
        self.browser.get("http://localhost:8000")
        self.assertIn("polls", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("polls", header_text)


if __name__ == "__main__":  
     unittest.main()  

