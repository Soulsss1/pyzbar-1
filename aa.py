import cv2 
from pyzbar import pyzbar 
# 1、讀取二維碼圖片 
qrcode = cv2.imread('c:\\Users\\Patron\\pyzbar-1\\qrcode.jpg')
# # 2、解析二維碼中的數據 
data= pyzbar.decode(qrcode) 
print(data) 
# 3、在數據中解析出二維碼的data信息 
text = data[0].data.decode('utf-8') 
print(text)
