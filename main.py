from  tkinter import *

root = Tk()
root .geometry('644x900')
root.title("Calculator with Saurav Subedi")

def click(event):
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set('')
        screen.update()

    else:
        scvalue.set(scvalue.get() + str(text))
        screen.update()


scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvar=scvalue, font ='lucida 40 bold' )
screen.pack(fill = X, ipadx=8,pady=10,padx = 10)

i = [[9,8,7],[6,5,4],[3,2,1],[0,'-','*'],['/','C','=']]
for j in range(5):
    f = Frame(root,bg = 'grey')
    b = Button(f,text=i[j][0],padx =28, pady= 18,font='lucida 35 bold')
    b.pack(side=LEFT,padx=18,pady=5)
    b.bind("<Button-1>",click)

    b = Button(f,text=i[j][1],padx =28, pady= 18,font='lucida 35 bold')
    b.pack(side=LEFT,padx=18,pady=5)
    b.bind("<Button-1>",click)

    b = Button(f,text=i[j][2],padx =28, pady= 18,font='lucida 35 bold')
    b.bind("<Button-1>",click)
    b.pack(side=LEFT,padx=18,pady=5)

    f.pack()
#b = Button(f,text='8',padx =28, pady= 22,font='lucida 35 bold')
#b.pack(side=LEFT,padx=18,pady=12)
#b = Button(f,text='7',padx =28, pady= 22,font='lucida 35 bold')
#b.pack(side=LEFT,padx=18,pady=12)
root.mainloop()