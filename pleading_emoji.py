from tkinter import *
root = Tk()
'''center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    '''

myCanvas = Canvas(root,bg="lime", height=300, width=300)
myCanvas.pack()
#x=150,y=150,r=100
myCanvas.create_oval(50,50,250,250,fill="yellow",width=5)
#x=110,y=125,r=30
myCanvas.create_oval(80,95,140,155,fill="white",width=5)
#x=110,y=125,r=20
myCanvas.create_oval(90,105,130,145,fill="black")
#x=105,y=120,r=10
myCanvas.create_oval(95,110,115,130,fill="white")
#x=115,y=130,r=5
myCanvas.create_oval(110,125,120,135,fill="white")
#x=110,y=60,r=30
myCanvas.create_arc(80,30,140,90,style='arc',start=225,extent='90',width=4)

#x=190,y=125,r=30
myCanvas.create_oval(160,95,220,155,fill="white",width=5)
#x=190,y=125,r=20
myCanvas.create_oval(170,105,210,145,fill="black")
#x=185,y=120,r=10
myCanvas.create_oval(175,110,195,130,fill="white")
#x=195,y=130,r=5
myCanvas.create_oval(190,125,200,135,fill="white")
#x=190,y=60,r=30
myCanvas.create_arc(160,30,220,90,style='arc',start=225,extent='90',width=4)
#x=150,y=30
myCanvas.create_text(150,30,text="Pleading Face")
myCanvas.create_line(110,185,190,185,width=10)
myCanvas.mainloop()