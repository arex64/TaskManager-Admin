from tkinter import *
from DataAccessLayer.JobsDA import JobsDB
from Model.UserModel import User
from UILayer import *
from Model import *
from DataAccessLayer import *

class AddJobsUI:
    def __init__(self,user :User):
        self.User = user

    def JobsFormLoad(self):
        jobfrm = Tk()
        jobfrm.title('Jobs Form')
        jobfrm.iconbitmap('UILayer/images/Jobs (2).ico')
        jobfrm.geometry('320x170')
        jobfrm['background'] = '#1c2e4a'
        jobfrm.resizable(0, 0)
        positionRight = int(jobfrm.winfo_screenwidth() / 2 - 320 / 2)
        positionDown = int(jobfrm.winfo_screenheight() / 2 - 170 / 2)
        jobfrm.geometry('+{}+{}'.format(positionRight, positionDown))

        def backToMain():
            jobfrm.destroy()
            from UILayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertJobCommand():
            JobTitle = txtJobTitle.get()
            job = Jobs(JobTitle)
            jobdb = JobsDB(job)
            jobdb.insertJob()
            txtJobTitle.set('')

        frameinfo = LabelFrame(jobfrm, text=' Jobs ',foreground='red',bg='#5baee5')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblJobTitle = Label(frameinfo, text='JobTitle: ') \
            .grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtJobTitle = StringVar()
        entJobTitle = Entry(frameinfo, textvariable=txtJobTitle, width=30, highlightthickness=1) \
            .grid(row=1, column=1, padx=10, pady=10, sticky='w')

        btnSubmit = Button(jobfrm, text='Submit', width=10, justify='center',relief='groov', highlightthickness=1,command=insertJobCommand) \
            .grid(row=2, column=0, padx=20, pady=10)
        btnBack = Button(jobfrm, text='Back', width=10, justify='center',relief='groov', highlightthickness=1,command=backToMain) \
            .grid(row=3, column=0, padx=20, pady=10)

        jobfrm.mainloop()




