from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import babel.dates
import babel.numbers
from UILayer import *
from Model.UserModel import User
from Model import *
from DataAccessLayer.StaffDA import StaffDB
from DataAccessLayer import *



class RegisterStaffUI:
    def __init__(self, user: User):
        self.User = user

    def staffFormLoad(self):

        stafffrm = Tk()
        stafffrm.title('Staff Form')
        stafffrm.iconbitmap('UILayer/images/Staff.ico')
        stafffrm.geometry('420x395')
        stafffrm['background'] = '#1c2e4a'
        stafffrm.resizable(0, 0)
        positionRight = int(stafffrm.winfo_screenwidth() / 2 - 420 / 2)
        positionDown = int(stafffrm.winfo_screenheight() / 2 - 435 / 2)
        stafffrm.geometry('+{}+{}'.format(positionRight, positionDown))

        def checkValidation(*args):
            firstName= txtFirstName.get()
            lastName = txtLastName.get()
            nationalCode = txtNationalCode.get()
            mobileNumber = txtMobileNumber.get()
            if len(txtFirstName.get())>15:
                txtFirstName.set(txtFirstName.get()[:len(txtFirstName.get())-1])

            if len(txtLastName.get())>15:
                txtLastName.set(txtLastName.get()[:len(txtLastName.get())-1])

            if not txtNationalCode.get().isnumeric():
                txtNationalCode.set(txtNationalCode.get()[:len(txtNationalCode.get()) - 1])

            if len(txtNationalCode.get())>10:
                txtNationalCode.set(txtNationalCode.get()[:len(txtNationalCode.get()) - 1])

            if not txtMobileNumber.get().isnumeric():
                txtMobileNumber.set(txtMobileNumber.get()[:len(txtMobileNumber.get()) - 1])

            if len(txtMobileNumber.get())>11:
                txtMobileNumber.set(txtMobileNumber.get()[:len(txtMobileNumber.get()) - 1])


        def backToMain():
            stafffrm.destroy()
            from UILayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertStaffCommand():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            NationalCode = txtNationalCode.get()
            Birthdate = txtBirthdate.get()
            Gender = txtGender.get()
            MobileNumber = txtMobileNumber.get()
            Education = txtEducation.get()
            staff = Staff(FirstName, LastName, NationalCode, Birthdate, Gender, MobileNumber, Education)
            staffdb = StaffDB(staff)
            staffdb.insertStaff()
            txtFirstName.set('')
            txtLastName.set('')
            txtNationalCode.set('')
            txtBirthdate.set('')
            txtGender.set('')
            txtMobileNumber.set('')
            txtEducation.set('')

        frameinfo = LabelFrame(stafffrm, text=' Staff Information ', foreground='red', bg='#5baee5')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        txtFirstName.trace('w',checkValidation)
        entFirstName = Entry(frameinfo, textvariable=txtFirstName,justify='center', width=40, highlightthickness=1) \
            .grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        txtLastName.trace('w',checkValidation)
        entLastName = Entry(frameinfo, textvariable=txtLastName,justify='center', width=40, highlightthickness=1) \
            .grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblNationalCode = Label(frameinfo, text='NationalCode: ').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtNationalCode = StringVar()
        txtNationalCode.trace('w',checkValidation)
        entNationalCode = Entry(frameinfo,textvariable=txtNationalCode,justify='center', width=40, highlightthickness=1) \
                .grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')\
            .grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtBirthdate = StringVar()
        entBirthdate = DateEntry(frameinfo, textvariable=txtBirthdate,justify='center', width=14,year=2022,month=1,day=1,
                                 background='darkblue',foreground='white',borderwidth=1,relief='solid', highlightthickness=1) \
            .grid(row=4, column=1, padx=10, pady=10, sticky='w')
        lblBirthdateHint = Label(frameinfo, text='(Sample: MM/DD/YYY)') \
            .grid(row=5, column=1, padx=10, pady=0, sticky='w')

        lblGender = Label(frameinfo, text='Gender: ').grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txtGender = IntVar()
        rdMale = Radiobutton(frameinfo,text='Male',variable=txtGender,value=1)\
            .grid(row=6,column=1,pady=10,padx=10,sticky='w')
        rdFemale= Radiobutton(frameinfo,text='Female',variable=txtGender,value=2)\
            .grid(row=6,column=1,pady=10,padx=10,sticky='e')
        txtGender.set(1)

        lblMobileNumber = Label(frameinfo, text='MobileNumber: ').grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txtMobileNumber = StringVar()
        txtMobileNumber.trace('w',checkValidation)
        entMobileNumber = Entry(frameinfo, textvariable=txtMobileNumber,justify='center', width=40, highlightthickness=1) \
            .grid(row=7, column=1, padx=10, pady=10, sticky='w')

        lblEducation = Label(frameinfo, text='Education: ').grid(row=8, column=0, padx=10, pady=10, sticky='w')
        txtEducation = StringVar()
        entEducation = Combobox(frameinfo, width=20, textvariable=txtEducation, state='readonly')
        arrayEducation = []
        with open('Database/Education.csv', mode='r') as myfile:
            for line in myfile.readlines()[1:]:
                temp = line.rstrip('\n').split(',')
                arrayEducation.append(temp[1])
        entEducation['values'] = arrayEducation
        entEducation.grid(row=8, column=1, padx=10, pady=10, sticky='w')
        entEducation.current()
        # entEducation = Entry(frameinfo, textvariable=txtEducation,justify='center', width=40, highlightthickness=1) \
        #     .grid(row=8, column=1, padx=10, pady=10, sticky='w')
        # lblMaritialStatus = Label(frameinfo,text='MaritialStatus:').grid(row=9,column=0,pady=10, padx=10,sticky='w')
        # txtMaritialStatus = StringVar()
        # entMaritialStatus = Entry(frameinfo,textvariable=txtMaritialStatus,justify='center',width=40,highlightthickness=1)\
        #     .grid(row=9,column=1, padx=10, pady=10, sticky='w')
        btnSubmit = Button(stafffrm, text='Submit', width=10, highlightthickness=1,relief='groov',command=insertStaffCommand)\
            .grid(row=10, column=0, padx=20,pady=10, sticky='w')
        btnBack = Button(stafffrm, text='Back', width=10, highlightthickness=1,relief='groov',command=backToMain)\
            .grid(row=10, column=0, padx=20, pady=10, sticky='e')

        stafffrm.mainloop()



