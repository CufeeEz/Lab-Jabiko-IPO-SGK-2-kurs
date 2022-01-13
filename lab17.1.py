from PIL import Image
img = Image.new("RGB",(100,100))
img.save('test.jpg')
#img.show()
img.close()
img2 = Image.open('123.jpg')
img2.show() 
print(img2.size)
print(img2.format)
print(img2.getpixel((777,404)))
img2.putpixel((777,404), (255,0,0))
print(img2.getpixel((777,404)))
#done
