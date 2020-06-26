import os
from tkinter import *
from tkinter import font as tf
from tkinter import filedialog

class NotePadWin:
    def __init__(self):
        self.veiwWin()
    def veiwWin(self):
        self.root_win = Tk()
        self.root_win.geometry("800x500")
        self.root_win.title(os.getcwd())
        self.root_win.minsize(500,500)
        menubar = Menu(self.root_win)
        filemenu = Menu(menubar,tearoff= 0)
        filemenu.add_command(label='New',command=self.openNFile)
        filemenu.add_command(label='Open File', command=self.openXFile)
        filemenu.add_command(label='Save', command=self.saveFile)
        filemenu.add_command(label='Save As', command=self.saveAsFile)
        menubar.add_cascade(label='File',menu=filemenu)

        editmenu = Menu(menubar,tearoff=0)
        editmenu.add_command(label='copy',command=self.copyText)
        editmenu.add_command(label='cut', command=self.cutText)
        editmenu.add_command(label='paste', command=self.paste)
        menubar.add_cascade(label='Edit',menu=editmenu)

        fontmenu = Menu(menubar,tearoff=0)
        fontmenu.add_command(label='Font ',command=self.setFont)
        menubar.add_cascade(label='Preferences',menu=fontmenu)

        menubar.configure(bg='grey', fg='white')
        self.root_win.configure(menu=menubar)

        scroll =Scrollbar(self.root_win)
        scroll.pack(side=RIGHT,fill='y')
        scroll.configure(width=18,bg='grey')
        self.t_area = Text(self.root_win,height=500,width=800)
        self.t_area.pack(fill=BOTH)
        scroll.config(command=self.t_area.yview)
        self.t_area.config(yscrollcommand=scroll.set)
        self.t_area.get('1.0',END)
        self.root_win.mainloop()


class OperationNotepd(NotePadWin):
    def __init__(self):
        self.file_type = [('all files','.*'),('text files','.txt')]
        self.val = ""
        self.font_f = StringVar
        self.font_nm = StringVar
        self.font_sz = StringVar

    def openNFile(self):
        self.t_area.delete(1.0,END)
    def openXFile(self):
        ans = filedialog.askopenfilename(parent = self.root_win,initialdir= os.getcwd(),title="select filer",
                                         filetypes=self.file_type)
        self.t_area.delete(1.0,END)
        file = open(ans,'r')
        self.t_area.insert(CURRENT,file.read())

    def saveFile(self):
        ans = filedialog.asksaveasfile(parent = self.root_win,initialdir= os.getcwd(),title="file name")
    def saveAsFile(self):
        ans = filedialog.asksaveasfile(parent=self.root_win, initialdir=os.getcwd(), title="file name")
    def cutText(self):
        self.val = self.t_area.selection_get()
        x=self.t_area.search(self.val,1.0,END)
        y= '%s+%dc' % (x,len(self.val))
        self.t_area.delete(x,y)
    def copyText(self):
        self.val = self.t_area.selection_get()
    def paste(self):
        self.t_area.insert(END,self.val)
    def setFont(self):
        font =Tk()
        font.geometry('800x200')
        font.title('font')
        font.minsize(800,200)
        font.maxsize(800,200)
        self.setComp(font)
        font.configure(bg='white')
        font.mainloop()

    def setComp(self,_font):
        self.font_face = Listbox(_font)
        self.font_face.grid(row=0,column=0,padx=10,pady=10)
        f = tf.families()
        for i in f:
            self.font_face.insert(END, i)
        self.font_name = Listbox(_font)
        self.font_name.grid(row=0, column=1, padx=10, pady=10)
        self.font_name.insert(END, "BOLD")
        self.font_name.insert(END, "ITALIC")
        self.font_name.insert(END, "ROMAN")
        self.font_name.insert(END, "PLAIN")
        self.slider = Scale(_font,from_=0,to=72,orient=VERTICAL)
        self.slider.grid(row=0,column=3)
        self.slider.bind("<Button-1>",self.getFsz)
        l1 = Label(_font,text="font_name :")
        l1.place(x=450,y=50,width=80)
        l2 = Label(_font, text="font_style :")
        l2.place(x=450,y=100,width=80)
        l3 = Label(_font,text='font_size :')
        l3.place(x=450,y=150,width=80)

        self.e1 = Entry(_font,textvariable=self.font_name)
        self.e1.place(x=530, y=50, width=80)
        self.e2 = Entry(_font,textvariable=self.font_face)
        self.e2.place(x=530, y=100, width=80)
        self.e3 = Entry(_font,textvariable=self.font_sz)
        self.e3.place(x=530, y=150, width=80)
        b1 = Button(_font,text="SET-FONT")
        b1.place(x=640,y=50,width=80)
        b1.configure(bg='green')
        b2 =Button(_font,text="RESET")
        b2.place(x=640,y=100,width=80)
        b2.configure(bg='red')

        self.font_face.bind("<Button-1>",self.getFont_face)
        self.font_name.bind("<Button-1>", self.getFont_name)
        b1.bind("<Button-1>",self.getFP)
        b2.bind("<Button-1>", self.reset_font)

    def getFP(self,event):
        fnm=self.e1.get()
        fsz=self.e3.get()
        fsty=self.e2.get()
        if(fsty == "BOLD"):
            self.t_area.configure(font= tf.Font(family=fnm, size=fsz, weight=tf.BOLD))
        if (fsty == 'ITALIC'):
            self.t_area.configure(font= tf.Font(family=fnm, size=fsz, weight=tf.ITALIC))
        if (fsty == 'PLAIN'):
            self.t_area.configure(font= tf.Font(family=fnm, size=fsz, weight=tf.NORMAL))
        if (fsty == 'ROMAN'):
             self.t_area.configure(font= tf.Font(family=fnm, size=fsz, weight=tf.ROMAN))


    def reset_font(self,event):
        self.e1.delete(0,END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
    def getFsz(self,event):
        self.e3.delete(0,END)
        self.e3.insert(0,self.slider.get())
    def getFont_face(self,event):
        self.e1.delete(0,END)
        self.e1.insert(0,self.font_face.get(ACTIVE))
    def getFont_name(self,event):
        self.e2.delete(0,END)
        self.e2.insert(0,self.font_name.get(ACTIVE))

def main():
    notepad = OperationNotepd()
    notepad.veiwWin()

if __name__ == '__main__':
    main()
