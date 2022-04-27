from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.TasksDA import TasksDB
from Model.UserModel import User
from DataAccessLayer import *
from Model import *
from tkcalendar import DateEntry
from babel import numbers
from babel import dates

class AddTasksUI:
    def __init__(self, user: User):
        self.User = user

    def taskFormLoad(self):
        taskfrm = Tk()
        taskfrm.title('Tasks Form')
        taskfrm.iconbitmap('UILayer/images/Tasks.ico')
        taskfrm.geometry('750x340')
        taskfrm['background'] = '#1c2e4a'
        taskfrm.resizable(0, 0)
        positionRight = int(taskfrm.winfo_screenwidth() / 2 - 750 / 2)
        positionDown = int(taskfrm.winfo_screenheight() / 2 - 340 / 2)
        taskfrm.geometry('+{}+{}'.format(positionRight, positionDown))

        def backToMain():
            taskfrm.destroy()
            from UILayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertTasksCommand():
            PersonID = txtPersonID.get().split(' ')[0]
            ProjectID = txtProjectID.get().split(' ')[0]
            TaskName = txtTaskName.get()
            Status = txtStatus.get()
            StartDate = txtStartDate.get()
            Duration = txtDuration.get()
            Comment = txtComment.get()
            Deadline = txtDeadline.get()
            Priority = txtPriority.get()

            taskSave = Model.Task(PersonID,ProjectID,TaskName,Status,StartDate,Duration,Comment,Deadline,Priority)
            taskdbSave = TasksDB(taskSave)
            taskdbSave.insertTask()

            txtTaskName.set('')
            txtPersonID.set('')
            txtProjectID.set('')
            txtStartDate.set('')
            txtDuration.set('')
            txtDeadline.set('')
            txtPriority.set('')
            txtStatus.set('')
            txtComment.set('')

        taskdb = TasksDB()
        StaffList = taskdb.getStaffList()
        ProjectsList = taskdb.getProjectList()

        frameinfo = LabelFrame(taskfrm, text=' Assigned Tasks ',foreground='red',bg='#5baee5')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblTaskName = Label(frameinfo, text='TaskName: ').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtTaskName = StringVar()
        entTaskName = Entry(frameinfo, textvariable=txtTaskName,justify='center', width=30, highlightthickness=1) \
            .grid(row=1, column=1, padx=10, pady=10, sticky='w')

        PersonID = Label(frameinfo, text='Assigned Staff : ').grid(row=1, column=2, padx=10, pady=10, sticky='w')
        txtPersonID = StringVar()

        cmbPersonID = Combobox(frameinfo, width=20, textvariable=txtPersonID, state='readonly')
        cmbPersonID['values'] = StaffList
        cmbPersonID.grid(row=1, column=3, padx=10, pady=10, sticky='w')
        cmbPersonID.current()
        # entAssignedStaff = Entry(frameinfo, textvariable=txtStaffID,justify='center', width=30, highlightthickness=1) \
        #     .grid(row=1, column=3, padx=10, pady=10, sticky='w')

        lblProjectID = Label(frameinfo, text='ProjectNumber : ').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtProjectID = StringVar()
        cmbProjectID = Combobox(frameinfo, width=20, textvariable=txtProjectID, state='readonly')
        cmbProjectID['values'] = ProjectsList
        cmbProjectID.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        cmbProjectID.current()

        # entProjectNumber = Entry(frameinfo, textvariable=txtProjectID,justify='center', width=30, highlightthickness=1) \
        #     .grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblStartDate = Label(frameinfo, text='StartDate: ').grid(row=2, column=2, padx=10, pady=10, sticky='w')
        txtStartDate = StringVar()
        entStartDate = DateEntry(frameinfo, dates='LC_TIME', textvariable=txtStartDate,justify='center',
                                 width=20,year=2022,month=1,day=1,background='darkblue',foreground='white',borderwidth=1,relief='solid', highlightthickness=1) \
            .grid(row=2, column=3, padx=10, pady=10, sticky='w')

        lblDuration = Label(frameinfo, text='Duration: ').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtDuration = StringVar()
        entDuration = Entry(frameinfo, textvariable=txtDuration,justify='center', width=30, highlightthickness=1) \
            .grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblDeadLine = Label(frameinfo, text='Deadline: ').grid(row=3, column=2, padx=10, pady=10, sticky='w')
        txtDeadline = StringVar()
        entDeadline = DateEntry(frameinfo, textvariable=txtDeadline,justify='center', width=20,year=2022,month=1,day=1,background='darkblue',foreground='white',borderwidth=1,relief='solid', highlightthickness=1) \
            .grid(row=3, column=3, padx=10, pady=10, sticky='w')

        lblPriority = Label(frameinfo, text='Priority: ').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtPriority = StringVar()
        entPriority = Combobox(frameinfo, width=20, textvariable=txtPriority, state='readonly')
        arrayPriority = []
        with open('Database/Priority.csv', mode='r') as myfile:
            for line in myfile.readlines()[1:]:
                temp = line.rstrip('\n').split(',')
                arrayPriority.append(temp[1])
        entPriority['values'] = arrayPriority
        entPriority.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        entPriority.current()

        lblStatus = Label(frameinfo, text='Status: ').grid(row=4, column=2, padx=10, pady=10, sticky='w')
        txtStatus = StringVar()
        entStatus = Combobox(frameinfo, width=20, textvariable=txtStatus, state='readonly')
        arrayStatus = []
        with open('Database/Status.csv', mode='r') as myfile:
            for line in myfile.readlines()[1:]:
                temp = line.rstrip('\n').split(',')
                arrayStatus.append(temp[1])
        entStatus['values'] = arrayStatus
        entStatus.grid(row=4, column=3, padx=10, pady=10, sticky='w')
        entStatus.current()

        lblComment = Label(frameinfo, text='Comment: ').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtComment = StringVar()
        entComment = Entry(frameinfo, textvariable=txtComment,justify='center', width=50, highlightthickness=1) \
            .grid(row=5, column=1, padx=10, pady=10, sticky='w')

        btnSubmit = Button(taskfrm, text='Submit', width=10, justify='center',relief='groov', highlightthickness=1,command=insertTasksCommand)\
            .grid(row=6,column=0,padx=20, pady=10)
        btnBack = Button(taskfrm, text='Back', width=10, justify='center',relief='groov', highlightthickness=1,command=backToMain)\
            .grid(row=7, column=0, padx=20, pady=10)

        taskfrm.mainloop()