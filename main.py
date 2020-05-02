from tkinter import*
import tkinter.messagebox
import stdDatabase_BackEnd



class Worker:

    def __init__(self, root):
        self.root = root
        self.root.title("KEZ")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg='cadet blue')


        WorID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Posada = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Adress = StringVar()
        Mobile = StringVar()

       #=======================================Function====================================================

        def iExit():
           iExit = tkinter.messagebox.askyesno("DATABASE", "Подтвердите ВЫХОД")
           if iExit > 0:
              root.destroy()
           return

        def clearData():
            self.txtWorID.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtFna.delete(0,END)
            self.txtPosad.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGend.delete(0,END)
            self.txtAdre.delete(0,END)
            self.txtMobi.delete(0,END)


        def addData():
            if (len(WorID.get())!= 0):
                stdDatabase_BackEnd.WorkerRec(WorID.get(), Firstname.get(), Surname.get(), Posada.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get())
                workerlist.delete(0,END)
                workerlist.insert(END,(WorID.get(), Firstname.get(), Surname.get(), Posada.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()))


        def displayData():
            workerlist.delete(0,END)
            for row in stdDatabase_BackEnd.viewData():
                workerlist.insert(END, row, str(""))


        def WorkerRec(event):
            global sd
            searchWor = workerlist.curselection()
            sd = workerlist.get(searchWor)



            self.txtWorID.delete(0,END)
            self.txtWorID.insert(END, sd[1])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END, sd[1])
            self.txtFna.delete(0,END)
            self.txtFna.insert(END, sd[1])
            self.txtPosad.delete(0,END)
            self.txtPosad.insert(END, sd[1])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END, sd[1])
            self.txtGend.delete(0,END)
            self.txtGend.insert(END, sd[1])
            self.txtAdre.delete(0,END)
            self.txtAdre.insert(END, sd[1])
            self.txtMobi.delete(0,END)
            self.txtMobi.insert(END, sd[1])



        def DeleteData():
            if (len(WorID.get())!= 0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                displayData()

        def SearchDatabase():
            workerlist.delete(0, END)
            for row in stdDatabase_BackEnd.searchData(WorID.get(), Firstname.get(), Surname.get(), Posada.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()):
                workerlist.insert(END, row, str(""))

        def update():
            if (len(WorID.get())!= 0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if (len(WorID.get())!= 0):
                stdDatabase_BackEnd.addWorRec(WorID.get(), Firstname.get(), Surname.get(), Posada.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get())
                workerlist.delete(0, END)
                workerlist.insert(END, (WorID.get(), Firstname.get(), Surname.get(), Posada.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get()))







       #=======================================Frames====================================================


        MainFrame = Frame(self.root, bg='cadet blue')
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg='Ghost White', relief = RIDGE )
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 40, 'bold'), text="Database", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg='Ghost White', relief = RIDGE )
        ButtonFrame.pack(side=BOTTOM)


        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, bg='cadet blue', relief = RIDGE )
        DataFrame.pack(side=BOTTOM)


        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,  bg='Ghost white', relief = RIDGE , font=('arial', 20, 'bold'),
        text="Информация о сотрудниках\n")
        DataFrameLEFT.pack(side=LEFT)


        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, bg='Ghost white', relief = RIDGE, font=('arial', 20, 'bold'),
        text="Детали о сотрудниках\n" )
        DataFrameRIGHT.pack(side=RIGHT)



        #=======================================Labels and Entry====================================================


        self.lblWorID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="iD сотрудника", padx=2, pady=2,bg="Ghost White")
        self.lblWorID.grid(row=0, column=0, sticky=W)
        self.txtWorID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=WorID, width=39)
        self.txtWorID.grid(row=0, column=1, sticky=W)

        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Фамилия",padx=2, pady=3,bg="Ghost White")
        self.lblSna.grid(row=1, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        self.txtSna.grid(row=1, column=1, sticky=W)

        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Имя", padx=2, pady=4,bg="Ghost White")
        self.lblFna.grid(row=2, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtFna.grid(row=2, column=1, sticky=W)

        self.lblPosad = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Должность", padx=2, pady=4,bg="Ghost White")
        self.lblPosad.grid(row=3, column=0, sticky=W)
        self.txtPosad = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Posada, width=39)
        self.txtPosad.grid(row=3, column=1, sticky=W)

        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Возраст", padx=2, pady=4,bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1, sticky=W)


        self.lblGend = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Пол", padx=2, pady=4,bg="Ghost White")
        self.lblGend.grid(row=5, column=0, sticky=W)
        self.txtGend = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGend.grid(row=5, column=1, sticky=W)


        self.lblAdre = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Адрес", padx=2, pady=4,bg="Ghost White")
        self.lblAdre.grid(row=6, column=0, sticky=W)
        self.txtAdre = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Adress, width=39)
        self.txtAdre.grid(row=6, column=1, sticky=W)

        self.lblMobi = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Номер телефона", padx=2, pady=4,bg="Ghost White")
        self.lblMobi.grid(row=7, column=0, sticky=W)
        self.txtMobi = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobi.grid(row=7, column=1, sticky=W)



        #=======================================ListBox & ScrollBar Widget====================================================


        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky="ns")



        workerlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        workerlist.bind('<<ListboxSelect>>', WorkerRec)
        workerlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = workerlist.yview)


        #=======================================Button Widget====================================================

        self.btnAddDate = Button(ButtonFrame, text='Добавить', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayDate = Button(ButtonFrame, text='Показать', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=displayData)
        self.btnDisplayDate.grid(row=0, column=1)

        self.btnClearDate = Button(ButtonFrame, text='Очистить', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClearDate.grid(row=0, column=2)

        self.btnDeleteDate = Button(ButtonFrame, text='Удалить', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteDate.grid(row=0, column=3)

        self.btnSearchDate = Button(ButtonFrame, text='Поиск', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=SearchDatabase)
        self.btnSearchDate.grid(row=0, column=4)

        self.btnUpdateDate = Button(ButtonFrame, text='Обновить', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=update)
        self.btnUpdateDate.grid(row=0, column=5)

        self.btnExitDate = Button(ButtonFrame, text='Выход', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExitDate.grid(row=0, column=6)

if __name__ == "__main__":

    root = Tk()
    application = Worker(root)
    root.mainloop()