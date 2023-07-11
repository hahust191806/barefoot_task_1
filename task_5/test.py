import base64
from time import sleep
import cv2
import requests
from PIL import Image
import os


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

url = 'https://us1.badoo.com/hidden?euri=peHsJsbIu6Dz1pyPM7xmFnMiSj.wwEy0G.yjK2ACmECFVehwY08t0CQCyzEDL8nf4Vy9hjEfGnrxI7NKm91xFwqru1isR.VNf4D9nPik5o1L4CmlOKBb1X2o0yq2CiNBADKmkJR23nnDwv38zEIzo-YlobHBXFsNAe6zAT-VsLHtbOU-YghL7IuxNuxotHpsZWcf-VStmO4'

# Tên file ảnh
filename = 'captcha.gif'

# Đường dẫn tuyệt đối đến thư mục hiện tại của chương trình
folder_path = os.path.abspath(os.path.dirname(__file__))

# Đường dẫn tới file ảnh trong thư mục hiện tại
# image_path = os.path.join(folder_path, filename)

# Gửi yêu cầu GET để tải ảnh từ đường dẫn
response = requests.get(url)

# Lưu ảnh vào file ảnh
with open(filename, 'wb') as f:
    f.write(response.content)
    
print(solve_captcha(filename))