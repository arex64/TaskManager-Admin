from tkinter import *
from DataAccessLayer.UserDA import UserDB
from babel import numbers
from babel import dates
import Model
from UILayer import images
from Model import *


class AddUserUI:
    def __init__(self, user: User):
        self.User = user

    def FormLoad(self):
        adduserfrm = Tk()
        adduserfrm.title(' Add User ')
        adduserfrm.iconbitmap('UILayer/images/User.ico')
        adduserfrm.geometry('333x300')
        adduserfrm['background'] = '#1c2e4a'
        adduserfrm.resizable(0, 0)
        positionRight = int(adduserfrm.winfo_screenwidth() / 2 - 333 / 2)
        positionDown = int(adduserfrm.winfo_screenheight() / 2 - 300 / 2)
        adduserfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def CheckValidation():
            firstName = txtFirstName
            lastName = txtLastName
            if len(txtFirstName.get())>15:
                txtFirstName.set(txtFirstName.get()[:len(txtFirstName.get())-1])

            if not txtFirstName.get().isnumeric():
                txtFirstName.set(txtFirstName.get()[:len(txtFirstName.get()) - 1])

            if len(txtLastName.get()) > 15:
                txtLastName.set(txtLastName.get()[:len(txtLastName.get()) - 1])

            if not txtLastName.get().isnumeric():
                txtLastName.set(txtLastName.get()[:len(txtLastName.get()) - 1])


        def backToMain():
            adduserfrm.destroy()
            from UILayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()


        def insertCommand():

            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            UserName = txtUserName.get()
            Password = txtPassword.get()
            Admin = txtAdmin.get()

            user = User(FirstName,LastName,UserName,Password,Admin)
            userdb = UserDB(user)
            userdb.insertUser()
            txtFirstName.set('')
            txtLastName.set('')
            txtUserName.set('')
            txtPassword.set('')
            txtAdmin.set('')

        frameinfo = LabelFrame(adduserfrm, text=' User Information',foreground='red',bg='#5baee5')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='n')

        lblFirstName = Label(frameinfo, text='FirstName:')\
            .grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName,justify='center', width=30, highlightthickness=1)\
            .grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblLastName = Label(frameinfo, text='LastName:')\
            .grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName,justify='center', width=30, highlightthickness=1)\
            .grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblUserName = Label(frameinfo, text='UserName:')\
            .grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtUserName = StringVar()
        entUserName = Entry(frameinfo, textvariable=txtUserName,justify='center', width=30, highlightthickness=1)\
            .grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblPassword = Label(frameinfo, text='Password:')\
            .grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtPassword = StringVar()
        entPassword = Entry(frameinfo, textvariable=txtPassword,justify='center', width=30, highlightthickness=1,show='*')\
            .grid(row=4, column=1, padx=10, pady=10, sticky='w')

        txtAdmin = IntVar()
        chbAdmin = Checkbutton(frameinfo, text='Admin', variable=txtAdmin)\
            .grid(row=5, column=1, padx=5, pady=10,sticky='e')

        btnAddUser = Button(adduserfrm, text='Add User', width=15, relief='groov',command=insertCommand)\
            .grid(row=6, column=0, padx=30, pady=10,sticky='w')
        btnBack = Button(adduserfrm, text='Back to Main', width=15, relief='groov',command=backToMain)\
            .grid(row=6, column=0, padx=30, pady=10, sticky='e')

        adduserfrm.mainloop()



