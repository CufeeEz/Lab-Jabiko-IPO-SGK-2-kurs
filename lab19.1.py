from wand import color
from wand.image import Image as WandImage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
img = WandImage(width = 500, height = 500, background = Color("teal"))
draw = Drawing()
draw.fill_color = Color('GREEN')
draw.rectangle(0,350,500,500)
draw.fill_color = Color('gold')
draw.ellipse((75, 75), (50,50))
draw.line((75, 75),(130,130))
draw.line((75, 75),(110,145))
draw.line((75, 75),(85,145))
draw.line((75, 75),(140,105))
draw.line((75, 75),(150,90))
draw.line((75, 75),(155,70))
draw.line((75, 75),(155,40))
draw.line((75, 75),(60,150))
draw.stroke_width = 2
draw.stroke_color = Color("black")
draw.fill_color = Color("white")
draw.arc((200,60),(300,100),(0,180))
draw.arc((320,20),(420,60),(0,180))
draw.arc((390,55),(480,85),(0,180))
draw.arc((330,80),(410,110),(0,180))
draw.arc((150,10),(250,55),(0,180))
draw.stroke_color = Color("chocolate")
draw.fill_color = Color("chocolate")
draw.rectangle(313,305,326,366)
draw.stroke_color = Color("olive")
draw.fill_color = Color("green")
draw.bezier([(260,230),(360,350),(290,350),(370,220),(320,200)])
draw.stroke_color = Color("brown")
draw.fill_color = Color("brown")
draw.rectangle(70,340,84,368)
draw.arc((60,350),(95,330),(180,0))
draw.stroke_color = Color("blue")
draw.fill_color = Color("blue")

draw.draw (img) #рисование
display (img) #вывод