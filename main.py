import qrcode

url = input("Insira a URL: ").strip()
file_Path = "C:\\Users\\MATHEUS HENRIQUE\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_Path)

print("O QRcode foi gerado!")