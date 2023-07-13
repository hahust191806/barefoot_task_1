import json 

pricing_name = ["BmTC", "BTC"]
area_redeem = "Only redeemable in Afghanistan"
delevery = "Instant delivery"
wallet1 = "Mainnet"
wallet2 = "aaa"
wallet3 = "fffff"
address1 = "3Bq1ujXSzMNLpqiiBQW8BQcJYdnfa4t9EQ"
address2 = "lnbc720990n1pjf4pzjpp5rvawujcu4df8nf8wn0k3kq8lj"
address3 = "0xC0E4283c113fce652AB0744a36BF7F69D6F13188"
game = "minecraft"

data = {}

for i in pricing_name:
    pricing = {
        game: [
            {
                "wallet_address": None, 
                "area_redeem": area_redeem,
                "delevery": delevery,
                "title": title, 
                "country": country, 
                "img": img, 
                "type": type, 
                "content": content, 
                "decription": decription             
            }
            
        ]
    }


    wallet_data = {}
    wallet_data[wallet1] = [address1]
    wallet_data[wallet2] = [address2]
    wallet_data[wallet3] = [address3]

    pricing[game][0]["wallet_address"] = wallet_data

    data[i] = pricing
print(data)

    
# Ghi dữ liệu mới vào file cũ
with open("data.json", "w") as old_file:
    json.dump(data, old_file, indent=4)
    
# # Đường dẫn đến file JSON cũ
# old_file_path = "data.json"

# # Đọc dữ liệu từ file JSON cũ
# with open(old_file_path, "r") as old_file:
#     old_data = json.load(old_file)

# # Tạo đối tượng JSON mới
# new_data = {
#     pricing: {
#         game: [
#             {
#                 "wallet_address": None, 
#                 "area_redeem": area_redeem,
#                 "delevery": delevery
#                 # "title": title, 
#                 # "country": country, 
#                 # "img": img, 
#                 # "type": type, 
#                 # "content": content, 
#                 # "decription": decription             
#             }
         
#         ]
#     }
# }

# # Nối đối tượng mới với dữ liệu đọc được
# old_data.append(new_data)

# # Ghi dữ liệu mới vào file cũ
# with open(old_file_path, "w") as old_file:
#     json.dump(old_data, old_file, indent=4)