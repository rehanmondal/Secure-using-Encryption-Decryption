from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x200")

def encryption():

    f = filedialog.askopenfile(mode= 'r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if f is not None:
        f_name = f.name
        key = ip_key.get(1.0,END)

        open_file = open(f_name,'rb')
        final = open_file.read()
        open_file.close()

        final = bytearray(final)

        for index,values in enumerate(final):
            final[index] = values^int(key)

        file_opened = open(f_name,'wb')
        file_opened.write(final)
        file_opened.close()

ip_key = Text(root,height=2,width=15)
ip_key.place(x=98,y=70)

butt = Button(root,text="Encrypt / Decrypt",command= encryption)
butt.place(x=104,y=120)

root.mainloop()