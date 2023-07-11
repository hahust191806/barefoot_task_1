from selenium import webdriver # Import WebDriver implementations 
from selenium.webdriver.common.keys import Keys # Cung cấp các phím trong bàn phím 
from selenium.webdriver.common.by import By # Dùng để xác định vị trí các phần tử trong tài liệu 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import keyboard
import base64
from time import sleep
import cv2
import requests
from PIL import Image
import os
from selenium.webdriver.support.ui import Select
from faker import Faker
import pyautogui

# resolve captcha
def solve_captcha(uri):
    gif_file_path = uri

    with open(gif_file_path, 'rb') as file:
        imgcontent = file.read()
        
    data = {
        "clientKey": "438230e974574a76828d65b4efbe4493",
        "task": {
            "type": "ImageToTextTask",
            "body": base64.b64encode(imgcontent).decode("utf-8")
        }
    }
    get_id = requests.post('https://api.anycaptcha.com/createTask', json=data, headers={'Host': 'api.anycaptcha.com', 'Content-Type': 'application/json'}).json()
    taskId = get_id.get('taskId')
    payload = {
        'clientKey': '438230e974574a76828d65b4efbe4493',
        'taskId': taskId
    }
    while True:
        sleep(0.5)
        response = requests.post('https://api.anycaptcha.com/getTaskResult', json=payload,
                                 headers={'Host': 'api.anycaptcha.com', 'Content-Type': 'application/json'}).json()
        if response.get('status') == 'processing':
            pass
        elif response.get('status') == 'ERROR_CAPTCHA_UNSOLVABLE':
            break
        else:
            return response.get('solution').get('text')

class auto_signup:
    def __init__(self):
        self.email = None 
        self.user_name = None
        self.current_url = None 
    
    def run_auto_signup(self):
        # Khởi tạo tên mail
        fake = Faker()
        username = fake.user_name()
        self.email = f"{username}hust@gmail.com"
        self.user_name = fake.name()
        
        # khởi tạo đối tượng webdriver với Chrome 
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        
        # Chuyển hướng tới url được cung cấp, và driver sẽ đợi đến khi web được tải xong
        driver.get("https://badoo.com/signup")
        time.sleep(2)

        # <--Page 1-->: send tài khoản và mật khẩu, sau đó click submit 
        # tìm id element
        id_element = wait.until(EC.visibility_of_element_located((By.ID, 'login')))
        # tìm password element
        password_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "js-password"))) 
         
        # entering user name 
        id_element.send_keys(self.email)
        
        # entering password 
        password_element.send_keys("Hayeulinh1@")
        
        # find submit button
        submit_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn--block"))) 
        submit_element.click() # submit 
        time.sleep(5)

        self.current_url = driver.current_url 
        print(self.current_url)
        if self.current_url == 'https://badoo.com/signup':
            while self.current_url == 'https://badoo.com/signup':
                # <--Step 2--> resolve captcha
                captcha_element = wait.until(EC.visibility_of_element_located((By.ID, "check_code_img"))) 

                # chụp ảnh captcha và lưu dưới file captcha.gif
                screenshot = captcha_element.screenshot_as_png
                with open('captcha.gif', 'wb') as f:
                    f.write(screenshot)
                
                # giải captcha
                captcha = solve_captcha('captcha.gif')

                # tìm checkcode element 
                id_element = wait.until(EC.visibility_of_element_located((By.ID, "checkcode")))
                id_element.send_keys(captcha)
                
                # find submit button
                submit_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn--block")))
                submit_element.click() # submit 
                time.sleep(5)
                
                # lấy url hiện tại
                self.current_url = driver.current_url

        # <--Step 3-->: điền tên (không có số), ngày sinh, tháng sinh, năm sinh v.v.
        # tìm user name element
        fullname_element = wait.until(EC.visibility_of_element_located((By.NAME, "fullname")))
        fullname_element.send_keys(self.user_name) # entering user_name 
        
        # tìm day field element
        day_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.js-signup-day')))
        day_element.click() # Click vào phần tử select để mở trường select
        day_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-qa-value="1"]')))
        day_input.click()
        
        # tìm month field element
        month_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.js-signup-month')))
        month_element.click() # Click vào phần tử select để mở trường select
        # Tìm phần tử li chứa giá trị "01" và chọn nó
        div_element1 = driver.find_element(By.CSS_SELECTOR, '.js-signup-month')
        div_element2 = div_element1.find_element(By.CLASS_NAME, 'dropdown--select')
        div_element3 = div_element2.find_element(By.CLASS_NAME, 'dropdown__options')
        div_element4 = div_element3.find_element(By.CLASS_NAME, 'scroll--dynamic')
        div_element5 = div_element4.find_element(By.CLASS_NAME, 'scroll__inner')
        ul_element = div_element5.find_element(By.CLASS_NAME, 'options')
        month_input = ul_element.find_element(By.CSS_SELECTOR, 'li[data-qa-value="5"]')
        month_input.click()
        
        # tìm year field element
        year_element = driver.find_element(By.CSS_SELECTOR, '.js-signup-year') # Click vào phần tử select để mở trường select
        year_element.click()
        year_input = driver.find_element(By.CSS_SELECTOR, 'li[data-qa-value="1997"]') # Tìm phần tử li chứa giá trị "1997" và chọn nó
        year_input.click()
        
        # tìm location element
        local_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-location-list')))
        local_element.click()
        local_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-value="15_2950_243"]')))
        local_input.click()
        
        # tìm gender element
        gender_element = wait.until(EC.visibility_of_element_located((By.ID, 'male')))
        gender_element.click() # entering gender 
        
        # continue button 
        continue_button = wait.until(EC.visibility_of_element_located((By.NAME, 'create_profile')))
        continue_button.click()

        # tìm đối tượng submit và nhấn nút để tải lên
        submit_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "file-upload__hint")))
        submit_button.click()
        
        # điền đường dẫn tới tệp tin
        path_to_img = r"C:\Users\Kieu Trung Ha\Desktop\internship\task_5\deptraikhoaito.jpg"
        pyautogui.typewrite(path_to_img, interval=0.1)
        # ấn phím Enter
        pyautogui.press('enter')
        time.sleep(5)
        
        # create profile 
        create_profile = driver.find_element(By.CSS_SELECTOR, ".react-button.react-button--filled.react-button--md.react-button--color-primary.react-button--narrow")
        # create_profile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-button.react-button--filled.react-button--md.react-button--color-primary.react-button--narrow")))
        create_profile.click()
        # time.sleep(5)
        
acc1 = auto_signup()
acc1.run_auto_signup()