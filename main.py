from  tkinter import *
def kalk():
    try:
        def plus():
            a = int(pole1.get())
            b = int(pole2.get())
            pole3.delete(0, END)
            pole3.insert(0, a+b)

        def minus():
            a = int(pole1.get())
            b = int(pole2.get())
            pole3.delete(0, END)
            pole3.insert(0, a-b)

        def dil():
            a = int(pole1.get())
            b = int(pole2.get())
            pole3.delete(0, END)
            pole3.insert(0, a/b)

        def mnoh():
            a = int(pole1.get())
            b = int(pole2.get())
            pole3.delete(0, END)
            pole3.insert(0, a*b)

        window = Tk()
        window.geometry("400x400")
        window.configure(bg="white")
        window.title("Калькулятор")

        nad1=Label(text="Перше число ")
        nad1.place(x=100, y=50,anchor="c")

        nad2=Label(text="Друге число ")
        nad2.place(x=100, y=100,anchor="c")

        nad3=Label(text="Відповідь ")
        nad3.place(x=100, y=300,anchor="c")

        pole1=Entry(window)
        pole1.place(x=270, y=50,anchor="c")

        pole2=Entry(window)
        pole2.place(x=270, y=100,anchor="c")

        pole3=Entry(window)
        pole3.place(x=270, y=300,anchor="c")

        kn1=Button(window, text="+", command=plus)
        kn1.place(x=70,y=180,anchor="c")

        kn2 = Button(window, text="-", command=minus)
        kn2.place(x=140, y=180, anchor="c")

        kn3= Button(window, text="/", command=dil)
        kn3.place(x=210, y=180, anchor="c")

        kn4 = Button(window, text="*", command=mnoh)
        kn4.place(x=280, y=180, anchor="c")

        window.mainloop()
    except Exception as ex:
            print(f'Eror information: {ex}')