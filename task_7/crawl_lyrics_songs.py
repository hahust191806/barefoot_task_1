import json
import spotipy
import webbrowser
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
import subprocess

os.environ["SPOTIPY_CLIENT_ID"] = "8f136fd89ed141f787a74b0a26a801dc"
os.environ["SPOTIPY_CLIENT_SECRET"] = "5168366b750e4e8f802ba9f8d6e6b7cd"

# Set the output directory
output_dir = "./songs"

# khởi tạo đối tượng webdriver với Chrome 
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Kieu Trung Ha\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Profile 2")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

list_song_url = []

with open("list_2000_tracks_name.txt", "r", encoding="utf-8") as f: 
        for line in f:
            # Tách dòng thành các phần riêng biệt bằng khoảng trắng
            parts = line.split()

            # Lấy liên kết Spotify cuối cùng của dòng và thêm nó vào danh sách
            list_song_url.append(parts[-1])
            
# chuyển hướng tới trang web tải lyrics bài hát 
driver.get("https://syrics-web-akashrchandran.vercel.app/")

for song_url in list_song_url: 
    # tải track songs
    subprocess.run(["spotify_dl", "-V", "-l", song_url, "--output", output_dir])
    
    # Tải lyrics synced 
    input_search = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/form/input")))
    input_search.click()
    input_search.clear()
    input_search.send_keys(song_url)

    search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/form/button")))
    search_button.click()

    download_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[2]/div/ul/li/button")))
    download_button.click()
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(2)
    driver.back()