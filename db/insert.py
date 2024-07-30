# import requests
#
# # Mock items
# items = [
#     { "title": "iPhone 13 Pro", "description": "6.1-inch display, A15 Bionic chip, triple-camera system", "owner_id": 1 },
#     { "title": "Samsung Galaxy S21", "description": "6.2-inch display, Exynos 2100, triple-camera system", "owner_id": 2 },
#     { "title": "Google Pixel 6", "description": "6.4-inch display, Google Tensor, dual-camera system", "owner_id": 3 },
#     { "title": "OnePlus 9 Pro", "description": "6.7-inch display, Snapdragon 888, quad-camera system", "owner_id": 4 },
#     { "title": "Sony Xperia 1 III", "description": "6.5-inch display, Snapdragon 888, triple-camera system", "owner_id": 5 },
#     { "title": "Xiaomi Mi 11", "description": "6.81-inch display, Snapdragon 888, triple-camera system", "owner_id": 6 },
#     { "title": "Oppo Find X3 Pro", "description": "6.7-inch display, Snapdragon 888, quad-camera system", "owner_id": 7 },
#     { "title": "Huawei P40 Pro", "description": "6.58-inch display, Kirin 990, quad-camera system", "owner_id": 8 },
#     { "title": "Asus ROG Phone 5", "description": "6.78-inch display, Snapdragon 888, triple-camera system", "owner_id": 9 },
#     { "title": "Realme GT", "description": "6.43-inch display, Snapdragon 888, triple-camera system", "owner_id": 10 },
#     { "title": "Nokia 8.3 5G", "description": "6.81-inch display, Snapdragon 765G, quad-camera system", "owner_id": 11 },
#     { "title": "Motorola Edge 20 Pro", "description": "6.7-inch display, Snapdragon 870, triple-camera system", "owner_id": 12 },
#     { "title": "Vivo X60 Pro", "description": "6.56-inch display, Snapdragon 870, triple-camera system", "owner_id": 13 },
#     { "title": "LG Velvet", "description": "6.8-inch display, Snapdragon 765G, triple-camera system", "owner_id": 14 },
#     { "title": "ZTE Axon 30 Ultra", "description": "6.67-inch display, Snapdragon 888, quad-camera system", "owner_id": 15 },
#     { "title": "Lenovo Legion Duel 2", "description": "6.92-inch display, Snapdragon 888, dual-camera system", "owner_id": 16 },
#     { "title": "Alcatel 5V", "description": "6.2-inch display, MediaTek MT6762, dual-camera system", "owner_id": 17 },
#     { "title": "TCL 20 Pro 5G", "description": "6.67-inch display, Snapdragon 750G, quad-camera system", "owner_id": 18 },
#     { "title": "Google Pixel 5a", "description": "6.34-inch display, Snapdragon 765G, dual-camera system", "owner_id": 19 },
#     { "title": "Samsung Galaxy Note 20 Ultra", "description": "6.9-inch display, Exynos 990, triple-camera system", "owner_id": 20 }
# ]
#
# # Send each item to the local server
# for item in items:
#     try:
#         result = requests.post(f'http://127.0.0.1:8000/users/{'owner_id'}/items/', json=item)
#         if result.status_code == 200:
#             print(f'Successfully added item {item["title"]}')
#         else:
#             print(f'Failed to add item {item["title"]}, status code: {result.status_code}, response: {result.text}')
#     except Exception as e:
#         print(f'Exception occurred while adding item {item["title"]}: {e}')
import requests

# Mock items
items = [
    { "title": "iPhone 13 Pro", "description": "6.1-inch display, A15 Bionic chip, triple-camera system", "owner_id": 1 },
    { "title": "Samsung Galaxy S21", "description": "6.2-inch display, Exynos 2100, triple-camera system", "owner_id": 2 },
    { "title": "Google Pixel 6", "description": "6.4-inch display, Google Tensor, dual-camera system", "owner_id": 3 },
    { "title": "OnePlus 9 Pro", "description": "6.7-inch display, Snapdragon 888, quad-camera system", "owner_id": 4 },
    { "title": "Sony Xperia 1 III", "description": "6.5-inch display, Snapdragon 888, triple-camera system", "owner_id": 5 },
    { "title": "Xiaomi Mi 11", "description": "6.81-inch display, Snapdragon 888, triple-camera system", "owner_id": 6 },
    { "title": "Oppo Find X3 Pro", "description": "6.7-inch display, Snapdragon 888, quad-camera system", "owner_id": 7 },
    { "title": "Huawei P40 Pro", "description": "6.58-inch display, Kirin 990, quad-camera system", "owner_id": 8 },
    { "title": "Asus ROG Phone 5", "description": "6.78-inch display, Snapdragon 888, triple-camera system", "owner_id": 9 },
    { "title": "Realme GT", "description": "6.43-inch display, Snapdragon 888, triple-camera system", "owner_id": 10 },
    { "title": "Nokia 8.3 5G", "description": "6.81-inch display, Snapdragon 765G, quad-camera system", "owner_id": 11 },
    { "title": "Motorola Edge 20 Pro", "description": "6.7-inch display, Snapdragon 870, triple-camera system", "owner_id": 12 },
    { "title": "Vivo X60 Pro", "description": "6.56-inch display, Snapdragon 870, triple-camera system", "owner_id": 13 },
    { "title": "LG Velvet", "description": "6.8-inch display, Snapdragon 765G, triple-camera system", "owner_id": 14 },
    { "title": "ZTE Axon 30 Ultra", "description": "6.67-inch display, Snapdragon 888, quad-camera system", "owner_id": 15 },
    { "title": "Lenovo Legion Duel 2", "description": "6.92-inch display, Snapdragon 888, dual-camera system", "owner_id": 16 },
    { "title": "Alcatel 5V", "description": "6.2-inch display, MediaTek MT6762, dual-camera system", "owner_id": 17 },
    { "title": "TCL 20 Pro 5G", "description": "6.67-inch display, Snapdragon 750G, quad-camera system", "owner_id": 18 },
    { "title": "Google Pixel 5a", "description": "6.34-inch display, Snapdragon 765G, dual-camera system", "owner_id": 19 },
    { "title": "Samsung Galaxy Note 20 Ultra", "description": "6.9-inch display, Exynos 990, triple-camera system", "owner_id": 20 }
]

# Send each item to the local server
for item in items:
    owner_id = item.pop('owner_id')  # Remove owner_id from item dictionary
    try:
        url = f'http://127.0.0.1:8000/users/{owner_id}/items/'
        result = requests.post(url, json=item)
        if result.status_code == 201:
            print(f'Successfully added item {item["title"]}')
        else:
            print(f'Failed to add item {item["title"]}, status code: {result.status_code}, response: {result.text}')
    except Exception as e:
        print(f'Exception occurred while adding item {item["title"]}: {e}')
