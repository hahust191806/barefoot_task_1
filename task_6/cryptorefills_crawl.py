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
import pyperclip 
import json

# khởi tạo đối tượng webdriver với Chrome 
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Kieu Trung Ha\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Profile 2")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# # chuyển hướng tới trang web crypto refills 
driver.get("https://www.cryptorefills.com/")
time.sleep(3)

# khởi tạo đối tượng data lưu trữ dữ liệu 
data = {}

# <--Tìm quốc gia-->
# chọn quốc gia 
countries_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/a/span[2]")))
countries_element.click()
select_countries = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-shop-page/div/crypt-shop-panel/section/div[2]/div[2]/crypt-countries-dropdown/div/div/crypt-countries-select/div/ul/li[1]/a/div[2]/div")))
countries_name = select_countries.text
select_countries.click()
time.sleep(2)

# <--Lấy dữ liệu từng sản phẩm-->
# lấy ra list các phần tử card
# list_of_items = driver.find_elements(By.CSS_SELECTOR, "li.brands-list__child.ng-star-inserted")
# for i in range(1, len(list_of_items) + 1):
xpath_element = "/html/body/crypt-root/div/div/div/crypt-shop-page/div/div/div[3]/crypt-dynamic-products/div/div/div/li[" + str(1) + "]"
item_element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_element)))
item_element.click()

# wallet name 
wallet_name = None 

# pricing name 
pricing_name = None 

# area_redeem
area_redeem_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]")))
area_redeem = area_redeem_element.text

# delivery
delivery_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]")))
delivery = delivery_element.text

# title
title_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[2]/h1")))
title = title_element.text

# tên game 
game_name = title.split()
game = " ".join(game_name[:-2])

# img
img_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/img")))
img = img_element.get_attribute("src")

# country name 
country = countries_name

# type 
type_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/ol/li[3]/a/span")))
type = type_element.text

# content
content_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div")))
content = content_element.text

# desciption
check_description_element = driver.find_elements(By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/p-accordion/div/p-accordiontab[1]/div/div[1]/a/h2")
if check_description_element:
    decription_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[1]/div[2]/div/div[2]/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div/p")))
    decription = decription_element.text
else: 
    decription = ""
    
    
# <--Add to cart-->  
add_to_cart_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[2]/div[2]/div[2]/crypt-product-dynamic-preview/div/div[3]/button")))
add_to_cart_element.click()

# bấm vào list định giá 
pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
pricing_element.click()

# đợi khi list pricing hiện ra để lấy số phần tử trong list
pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
list_pricing = driver.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element")    
pyautogui.press('enter')

# pricing_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul")))
# list_pricing = driver.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element")

for id_pricing in range(1, len(list_pricing) + 1):
    pricing_xpath = "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[" + str(id_pricing) + "]"
    
    # chọn pricing 
    pricing_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span")))
    pricing_element.click()
    time.sleep(1)
    
    pricing_choose = wait.until(EC.visibility_of_element_located((By.XPATH, pricing_xpath)))
    pricing_choose.click()
    time.sleep(1)
    
    pricing_name = (wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[2]/p-dropdown/div/span/span")))).text
    
    # Lặp qua từng network
    network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
    network_element.click()
    
    # đợi khi list network hiện ra để lấy phần tử network
    network_container = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span/span")))
    list_network = driver.find_elements(By.CSS_SELECTOR, "li.p-ripple.p-element.p-dropdown-item")
    pyautogui.press('enter')
    
    wallet_data = {}
    
    for id_network in range(1, len(list_network) + 1):
        network_xpath = "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/div[3]/div/ul/p-dropdownitem[" + str(id_network) + "]"

        # chọn network 
        network_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span")))
        network_element.click()
        time.sleep(2)   

        network_choose = wait.until(EC.visibility_of_element_located((By.XPATH, network_xpath)))
        network_choose.click()
        time.sleep(2)
        
        wallet_name = (wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[2]/div[3]/p-dropdown/div/span/span")))).text
        
        # chuyển đến trang thanh toán 
        proceed_checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-cart/div/div/div[4]/div/div/button")))
        proceed_checkout_button.click()
        
        # click vào copy địa chỉ ví 
        copy_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-payment-page/div/div/div/div/crypt-payment-cart/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/a")))
        copy_button.click()
        wallet_address = pyperclip.paste()
        time.sleep(5)
        
        pricing = {
            game: [
                {
                    "wallet_address": None, 
                    "area_redeem": area_redeem,
                    "delevery": delivery,
                    "title": title, 
                    "country": country, 
                    "img": img, 
                    "type": type, 
                    "content": content, 
                    "decription": decription             
                }
                
            ]
        }
        
        wallet_data[wallet_name] = [wallet_address]

        # quay lại trang trước đó 
        driver.back()
        pyautogui.press('enter') 
        
    pricing[game][0]["wallet_address"] = wallet_data
    data[pricing_name] = pricing  
    file_name = countries_name + ".json"
    with open(file_name, "w") as old_file:
        json.dump(data, old_file, indent=4)
    
    driver.quit()
    
# return_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/crypt-root/div/div/div/crypt-products-page/div/div/div/div[1]/a")))
# return_element.click()
    
# file_name = countries_name + ".json"
# with open(file_name, "w") as old_file:
#     json.dump(data, old_file, indent=4)