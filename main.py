# Slide-Show Presentation
#importing cycle from itertools library 
from itertools import cycle
#importing Tkinter library as tk
import tkinter as tk
#importing Image from PIL library
from PIL import Image
#importing ImageEnhance from PIL library
from PIL import ImageEnhance

#defining slides class
class slides(tk.Tk):
    def __init__(self, image_files, x, y, delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                                  for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides)
        self.title("Slides")
    def run(self):
        self.mainloop()

#inserting effects
image = Image.open('1.jpg')
image.save('1.gif')
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(2)
darker_image = enhancer.enhance(0.5)
brighter_image.save('x1.gif')
darker_image.save('y1.gif')
image = Image.open('2.jpg') 
image.save('2.gif')
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(2)
darker_image = enhancer.enhance(0.5)
brighter_image.save('x2.gif')
darker_image.save('y2.gif')
image = Image.open('3.jpg')
image.save('3.gif')
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(2)
darker_image = enhancer.enhance(0.5)
brighter_image.save('x3.gif')
darker_image.save('y3.gif')
image = Image.open('4.jpg')
image.save('4.gif')
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(2)
darker_image = enhancer.enhance(0.5)
brighter_image.save('x4.gif')
darker_image.save('y4.gif')
a = ['1.gif', 'y1.gif', 'x2.gif', '2.gif', 'y2.gif', 'x3.gif', '3.gif', 'y3.gif', 'x4.gif', '4.gif', 'y4.gif']

delay = 800
x = 100
y = 50

display = slides(a, x, y, delay)
display.show_slides()
display.geometry("600x400")
display.run()
