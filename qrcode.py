from PIL import Image
import zbarlight

file_path = './list/7ab7df3f4425f4c446ea4e5398da8847.png'
i = 0
while i <11001 :
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
    codes = zbarlight.scan_codes('qrcode', image)
    file_name = codes[0].split()[-1]
    print codes[0]
    file_path ="./list/" + file_name + ".png" 
    i += 1

