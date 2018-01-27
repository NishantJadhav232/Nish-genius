import csv 
from PIL import Image,ImageDraw,ImageFont
from tkinter import *
home=Tk()
home.wm_title("IEEE")
home.config(bg="red")
frame = Frame(home,width=500,height=500)
frame.pack()
#iris = PhotoImage(file =iris.jpg)
frame(0,0, anchor = NW, image='iris.jpj')
home.mainloop()


#with open('IEEE-form.csv','r') as file:
#	read = csv.DictReader(file)
#	for row in read:
 #   		print(row['Full Name'],row['Serial no.'],row['Email ID'])


iris = Image.open('iris.jpg')





