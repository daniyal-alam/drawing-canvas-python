from tkinter import *
from tkinter import colorchooser
from PIL import Image,ImageTk,ImageGrab
window=Tk()
current_x=0
current_y=0
pen_color="black"
pen_width=1

rectangles=[]
rectangle_color="black"
rectangle_width=1

circles=[]
circle_color="black"
circle_width=1

lines=[]
line_color="black"
line_width=1

erasers=[""]
erasing=[]
def Eraser_Destroy(event):
    global erasers,c1
    c1.delete(erasers[len(erasers)-1])
    erasers[len(erasers)-1]=""
def Width(a,b,c):
    global pen_width,circle_width,rectangle_width,line_width
    pen_width=s1.get()
    circle_width=s1.get()
    rectangle_width=s1.get()
    line_width=s1.get()
def Cursor_Color():
       global pen_color,rectangle_color,circle_color,line_color
       color = colorchooser.askcolor()[1]
       pen_color = color
       rectangle_color = color
       circle_color = color
       line_color = color
def Starting_Point_Pen(event):
    global current_x,current_y
    current_x=event.x
    current_y=event.y
def Pen(event):
    global current_x,current_y,c1,pen_color,pen_width
    c1.create_line(current_x,current_y,event.x,event.y,fill=pen_color,width=pen_width)
    current_x=event.x
    current_y=event.y
def Starting_Point_Rectangular(event):
    global current_x,current_y,rectangles
    current_x=event.x
    current_y=event.y
    rectangles.append("")
def Rectangular(event):
    global rectangles,current_y,current_x,c1,rectangle_color,rectangle_width
    c1.delete(rectangles[len(rectangles)-1])
    rectangles.append(c1.create_rectangle(current_x,current_y,event.x,event.y,fill=rectangle_color,width=rectangle_width))
def Starting_Point_Circular(event):
    global current_x,current_y,circles
    current_x=event.x
    current_y=event.y
    circles.append("")
def Circular(event):
    global current_x,current_y,c1,circle_color,circle_width
    c1.delete(circles[len(circles)-1])
    circles[len(circles)-1]=c1.create_oval(current_x,current_y,event.x,event.y,fill=circle_color,width=circle_width)
def Starting_Point_Line(event):
    global current_x,current_y,lines
    current_x=event.x
    current_y=event.y
    lines.append("")
def Straight_Line(event):
    global current_x,current_y,c1,lines,line_color,line_width
    c1.delete(lines[len(lines)-1])
    lines[len(lines)-1]=c1.create_line(current_x,current_y,event.x,event.y,fill=line_color,width=line_width)
def Eraser_Function1(event):
    global c1,erasing
    erasing.append(c1.create_rectangle(event.x,event.y,event.x+50,event.y+50,fill="SystemButtonFace",width=0))
def Eraser_Function2(event):
    global c1,erasing
    erasing.append(c1.create_rectangle(event.x,event.y,event.x+50,event.y+50,fill="SystemButtonFace",width=0))
def Eraser_Function3(event):
    global c1,erasers
    c1.delete(erasers[len(erasers)-1])
    erasers[len(erasers)-1]=c1.create_rectangle(event.x,event.y,event.x+50,event.y+50,fill="white")
def Eraser():
    global brush
    brush.selection_clear(0,END)
    c1.bind("<Button-1>",Eraser_Function1)
    c1.bind("<B1-Motion>",Eraser_Function2)
    c1.bind("<Motion>",Eraser_Function3)
def Brush_Selection(event):
    global brush
    if brush.selection_get()=="Pen":
        c1.bind("<Button-1>", Starting_Point_Pen)
        c1.bind("<B1-Motion>", Pen)
        c1.unbind("<Motion>")
    elif brush.selection_get()=="Rectangular":
        c1.bind("<Button-1>", Starting_Point_Rectangular)
        c1.bind("<B1-Motion>",Rectangular)
        c1.unbind("<Motion>")
    elif brush.selection_get()=="Circular":
        c1.bind("<Button-1>",Starting_Point_Circular)
        c1.bind("<B1-Motion>",Circular)
        c1.unbind("<Motion>")
    elif brush.selection_get()=="Straight Line":
        c1.bind("<Button-1>",Starting_Point_Line)
        c1.bind("<B1-Motion>",Straight_Line)
        c1.unbind("<Motion>")
def Canvas_Color():
    global c1,pen_color,rectangle_color,circle_color,erasing
    color = colorchooser.askcolor()[1]
    c1.config(bg=color)
    for x in erasing:
        c1.itemconfig(x,fill=color)
def Add_Thank_You_Text():
    c1.create_text(600, 290, text="Learning Together,", font=("Arial", 18, "bold"), fill="blue")
    c1.create_text(600, 320, text="Creating Together – Stanford CIP", font=("Arial", 18, "bold"), fill="red")
    c1.create_text(620, 350, text="Thanks for the wonderful opportunity With Gratitude to Stanford CIP – Empowering Learners Everywhere", font=("Arial", 18, "bold"), fill="purple")
def Clear():
    global c1
    c1['bg']="SystemButtonFace"
    c1.delete("all")
def Save_to_file():
    global e1,e1,label,btn
    if len(e1.get())>0:
        img=ImageGrab.grab(bbox=(0,17,window.winfo_screenwidth(),600))
        img.save(e1.get()+".jpg")
        e1.delete(0,END)
        e1.place_forget()
        label.place_forget()
        btn.place_forget()
def Save():
    global e1,label,btn
    label.place(x=1260, y=630)
    e1.place(x=1260, y=650, width=90)
    btn.place(x=1260, y=675)
c1 = Canvas(window,width=window.winfo_screenwidth(),height=600)
c1.pack()
l1 = LabelFrame(window,text="Cursor-Color")
l1.place(x=150,y=620)
cursor_color = Button(l1,text="Choose Color",command=Cursor_Color)
cursor_color.pack(ipadx=10,ipady=10)
l2 = LabelFrame(window,text="Canvas-Color")
l2.place(x=300,y=620)
canvas_color = Button(l2,text="Choose Color",command=Canvas_Color)
canvas_color.pack(ipadx=10,ipady=10)
btn_eraser = Button(window,text="Eraser",font=("times",20),command=Eraser)
btn_eraser.place(x=450,y=630)

brush = Listbox(window,height=4)
brush.insert(END,"Pen")
brush.insert(END,"Rectangular")
brush.insert(END,"Circular")
brush.insert(END,"Straight Line")
brush.place(x=600,y=630)
brush.bind("<<ListboxSelect>>",Brush_Selection)

l3 = LabelFrame(window,text="Brush Width")
l3.place(x=780,y=630)
v=IntVar()
s1 = Scale(l3,from_=0,to=100,orient=HORIZONTAL,variable=v)
s1.pack()
v.trace('w',Width)

btn_thank_you = Button(window, text="Add Credit", height=3, width=20, command=Add_Thank_You_Text)
btn_thank_you.place(x=915,y=635)

Btn_clear = Button(window,text="Clear",width=20,height=3,command=Clear)
Btn_clear.place(x=1135,y=635)

btn_save = Button(window,text="Save to PNG",height=3,width=20,command=Save)
btn_save.place(x=1300,y=635)
label=Label(window,text="Enter Filename")
label.place(x=1460,y=650)
e1=Entry(window)
e1.place(x=1560,y=650,width=90)
btn=Button(window,text="Save",width=12,command=Save_to_file)
btn.place(x=1460,y=675)
btn.place_forget()
e1.place_forget()
label.place_forget()
c1.bind("<Leave>",Eraser_Destroy)
window.mainloop()
