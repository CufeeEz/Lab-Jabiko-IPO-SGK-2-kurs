from PIL import Image, ImageFilter, ImageDraw

img = Image.open('123.jpg')
print(img.size, img.format, img.mode)
print(img.info)
imgcopy = img.copy()
#imgcopy.show()

#thumbnail
img2 = img.resize((640, 360), Image.LANCZOS)
#img2.show()
print(img2.size)

#rotate
imgRotate = img.rotate(90)
print(imgRotate.size)
imgRotate = img.rotate(45, Image.NEAREST)
print(imgRotate.size)
imgRotate = img.rotate(45, expand=True)
print(imgRotate.size)

#transpose
imgTransope = img.transpose(Image.FLIP_LEFT_RIGHT)
#imgTransope.show()
imgTransope = img.transpose(Image.FLIP_TOP_BOTTOM)
#imgTransope.show()
imgTransope = img.transpose(Image.ROTATE_90)
#imgTransope.show()

#crop
imgCrop = img.crop((300, 300, 600, 600))
imgCrop.load()
print(imgCrop.size)
#imgCrop.save('crop.jpg')

#paste
imgPaste = img
imgPaste.paste((100, 100, 100), (300, 300, 700, 700))
#imgPaste.show()
imgPaste.paste((0, 128, 0),img.getbbox())
#imgPaste.show()

#split
print(img.mode) #rgb
R,G,B=img.split()
mask = Image.new("L", img.size, 128)
img3 = Image.merge("RGBA",(R,G,B, mask))
print(img3.mode)
#img3.show()

#convert
img4 = img
print(img4.mode) #rgb
img4.mode
img4 = img.convert("RGBA")
print(img4.mode) #rgba

#filter
testimg = Image.open('123.jpg')
img5 = testimg.filter(ImageFilter.EMBOSS)
#img5.show()

#Draw, point
imgdraw = Image.open('123.jpg')
draw = ImageDraw.Draw(imgdraw) #Создаем экземпляр класса
for n in range(100, 1050):
    draw.point((n, 100), fill=(255,0,0))
#imgdraw.show()

#line
draw.line((100,100,1000,800),fill=(100,100,100), width=10)
#imgdraw.show()

#rectangle
draw.rectangle((500,500,800,800), fill=(0,128,255), outline=(1,1,1))
#imgdraw.show()

#polygon
draw.polygon((600,600,650,650,600,650), outline=(0,0,0), fill=(255,255,0))
draw.polygon((200,200,250,200,275,250,250,300,200,300,175,250), outline=(0,0,0), fill=(255,0,255))
#imgdraw.show()

#elipse
draw.ellipse((700,700,800,800), fill=(255,255,0))
#imgdraw.show()

#arc
draw.arc((10,10,290,290), 100, 179, fill=(0,0,255))
#imgdraw.show()

#chord
draw.chord((400,400,670,670),180,30, fill=(255,0,0))
#imgdraw.show()

#pieslice
draw.pieslice((700,700,800,800), 180,0, fill='green')
imgdraw.show()