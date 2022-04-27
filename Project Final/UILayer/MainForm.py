from tkinter import *
from UILayer import *
from Model.UserModel import User
from Model import *


class MainUI:
    def __init__(self, user: User = None):
        self.User = user
        pass

    def mainFormLoad(self):
        mainfrm = Tk()
        mainfrm.title('Main Form')
        mainfrm.geometry('380x550')

        mainfrm.resizable(0, 0)
        positionRight = int(mainfrm.winfo_screenwidth() / 2 - 380 / 2)
        positionDown = int(mainfrm.winfo_screenheight() / 2 - 550 / 2)
        mainfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def registerStaffFormLoad():
            mainfrm.destroy()
            from UILayer.RegisterStaffForm import RegisterStaffUI
            registerStaffForm = RegisterStaffUI(self.User)
            registerStaffForm.staffFormLoad()

        def addJobsFormLoad():
            mainfrm.destroy()
            from UILayer.AddJobsForm import AddJobsUI
            jobForm = AddJobsUI(self.User)
            jobForm.JobsFormLoad()

        def addTasksFormLoad():
            mainfrm.destroy()
            from UILayer.AddTasksForm import AddTasksUI
            taskForm = AddTasksUI(self.User)
            taskForm.taskFormLoad(self)

        def addProjectFormLoad():
            mainfrm.destroy()
            from UILayer.AddProjectsForm import AddProjectsUI
            projectForm = AddProjectsUI(self.User)
            projectForm.ProjectsFormLoad()

        def addUserFormLoad():
            mainfrm.destroy()
            from UILayer.AddUserForm import AddUserUI
            userForm = AddUserUI(self.User)
            userForm.FormLoad()

        def addTasksFormLoad():
            mainfrm.destroy()
            from UILayer.AddTasksForm import AddTasksUI
            taskForm = AddTasksUI(self.User)
            taskForm.taskFormLoad()

        def addProjectFormLoad():
            mainfrm.destroy()
            from UILayer.AddProjectsForm import AddProjectsUI
            projectForm = AddProjectsUI(self.User)
            projectForm.ProjectsFormLoad()

        def showAboutUs():
            from tkinter import messagebox as msg
            msg.showinfo('About Us', 'Task Manager')

        imgRegisterStaff = PhotoImage(file='UILayer/images/AddStaff.png')
        imgAddJobs = PhotoImage(file='UILayer/images/JobsForm.png')
        imgManageTasks = PhotoImage(file='UILayer/images/TasksForm.png')
        imgManageProjects = PhotoImage(file='UILayer/images/ProjectsForm.png')
        imgAddUser = PhotoImage(file='UILayer/images/AddUser.png')
        imgAboutUs = PhotoImage(file='UILayer/images/About Us.png')

        frameinfo = LabelFrame(mainfrm, text=' Welcome Dear ' + self.User.FirstName, foreground='red', bg='#1c2e4a', )
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        btnRegisterSatff = Button(frameinfo, text='Register Staff', image=imgRegisterStaff, relief='groov',
                                  bg='#5baee5', compound=TOP, height=140, width=120, highlightthickness=1,
                                  command=registerStaffFormLoad) \
            .grid(row=1, column=0, padx=20, pady=10)
        btnAddJobs = Button(frameinfo, text='Add Jobs', bg='#5baee5', image=imgAddJobs, compound=TOP, relief='groov',
                            height=140, width=120, justify='center', highlightthickness=1, command=addJobsFormLoad) \
            .grid(row=1, column=1, padx=20, pady=10)
        btnManageTasks = Button(frameinfo, text='Manage Tasks', bg='#5baee5', image=imgManageTasks, relief='groov',
                                compound=TOP, height=140, width=120, justify='center', highlightthickness=1,
                                command=addTasksFormLoad) \
            .grid(row=2, column=0, padx=20, pady=10)
        btnManageProjects = Button(frameinfo, text='Manage Projects', bg='#5baee5', relief='groov',
                                   image=imgManageProjects, compound=TOP, height=140, width=120, justify='center',
                                   highlightthickness=1, command=addProjectFormLoad) \
            .grid(row=2, column=1, padx=20, pady=10)
        if int(self.User.Admin) == 1:
            btnAddUser = Button(frameinfo, text='Add User', bg='#5baee5', image=imgAddUser, relief='groov',
                                compound=TOP, height=140, width=120,
                                justify='center', highlightthickness=1, command=addUserFormLoad) \
                .grid(row=3, column=0, padx=20, pady=10)

        btnAboutUs = Button(frameinfo, text='About Us', bg='#5baee5', relief='groov', image=imgAboutUs, compound=TOP,
                            height=140, width=120, justify='center', highlightthickness=1, command=showAboutUs) \
            .grid(row=3, column=1, padx=20, pady=10)

        mainfrm.mainloop()
