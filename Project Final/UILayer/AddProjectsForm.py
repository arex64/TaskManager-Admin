from tkinter import *
from DataAccessLayer.ProjectsDA import ProjectsDB
from Model.UserModel import User
from Model import *
from UILayer import *

class AddProjectsUI:
    def __init__(self, user: User):
        self.User = user

    def ProjectsFormLoad(self):
        projectfrm = Tk()
        projectfrm.title('Add Projects Form')
        projectfrm.iconbitmap('UILayer/images/Projects.ico')
        projectfrm.geometry('370x210')
        projectfrm['background'] = '#1c2e4a'
        projectfrm.resizable(0, 0)
        positionRight = int(projectfrm.winfo_screenwidth() / 2 - 370 / 2)
        positionDown = int(projectfrm.winfo_screenheight() / 2 - 210 / 2)
        projectfrm.geometry('+{}+{}'.format(positionRight, positionDown))

        def CheckValidation():
            projectNumber = txtProjectNumber.get()
            if not txtProjectNumber.get().isnumeric():
                txtProjectNumber.set(txtProjectNumber.get()[:len(txtProjectNumber.get()) - 1])



        def backToMain():
            projectfrm.destroy()
            from UILayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertProjectsCommand():
            ProjectName = txtProjectName.get()
            ClientName = txtClientName.get()
            ProjectNumber = txtProjectNumber.get()
            project = Projects(ProjectName,ClientName,ProjectNumber)
            projectdb = ProjectsDB(project)
            projectdb.insertProject()
            txtProjectName.set('')
            txtClientName.set('')
            txtProjectNumber.set('')

        frameinfo = LabelFrame(projectfrm, text=' Projects Information ',foreground='red',bg='#5baee5')
        frameinfo.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        lblProjectName = Label(frameinfo, text='ProjectName: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtProjectName = StringVar()
        entProjectName = Entry(frameinfo, textvariable=txtProjectName,justify='center', width=30, highlightthickness=1) \
            .grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblClientName = Label(frameinfo, text='ClientName: ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtClientName = StringVar()
        entClientName = Entry(frameinfo, textvariable=txtClientName,justify='center', width=30, highlightthickness=1) \
            .grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblProjectNumber = Label(frameinfo, text='ProjectNumber: ').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtProjectNumber = StringVar()
        txtProjectNumber.trace('w',CheckValidation)
        entProjectNumber = Entry(frameinfo, textvariable=txtProjectNumber,justify='center', width=30, highlightthickness=1) \
            .grid(row=3, column=1, padx=10, pady=10, sticky='w')

        btnSubmit = Button(projectfrm, text='Submit', width=10, highlightthickness=1,relief='groov',command=insertProjectsCommand)\
            .grid(row=4, column=2, padx=20, pady=10, sticky='w')
        btnBack = Button(projectfrm, text='Back', width=10, highlightthickness=1,relief='groov',command=backToMain)\
            .grid(row=4, column=2, padx=20,pady=10, sticky='e')

        projectfrm.mainloop()