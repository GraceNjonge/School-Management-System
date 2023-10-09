from tkinter import messagebox


def addstudent():
    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry('475x650+800+230')
    addroot.title('School Management System')
    addroot.iconbitmap('school.icon.ico')
    addroot.resizable(False,False)
    addroot.config(bg='blue')
#-------------------------------------------------------------
    idlabel = Label(addroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(addroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)

   
    addroot.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------#
def searchstudent():
    searchroot = Toplevel()
    searchroot.grab_set()
    searchroot.geometry('475x650+800+230')
    searchroot.iconbitmap('school.icon.ico')
    searchroot.resizable(False,False)
    searchroot.config(bg='blue')
#------------------------------------------------------------------------------------------------------------------------------------#
    idlabel = Label(searchroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(searchroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)
    searchroot.mainloop()
#-------------------------------------------------------------------------------------------------------------------------#
def deletestudent():
    deleteroot = Toplevel(master=DataEntryFrame)
    deleteroot.grab_set()
    deleteroot.geometry('475x650+800+230')
    deleteroot.iconbitmap('school.icon.ico')
    deleteroot.resizable(False,False)
    deleteroot.config(bg='blue')
#----------------------------------------------------------------------------------------------------------------------------------------#
    idlabel = Label(deleteroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(deleteroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(deleteroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(deleteroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(deleteroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(deleteroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(deleteroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------
    identry = Entry(deleteroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(deleteroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(deleteroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)
    deleteroot.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------#
def updatestudent():
    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry('475x650+800+230')
    updateroot.iconbitmap('school.icon.ico')
    updateroot.resizable(False,False)
    updateroot.config(bg='blue')
#-------------------------------------------------------------------------------------------------------#
    idlabel = Label(updateroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------------------------------------------------------------------------------------#
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)


    submitbutton = Button(updateroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)
    updateroot.mainloop()
#---------------------------------------------------------------------------------------------------------------------------#

def showstudent():
    showroot = Toplevel()
    showroot.grab_set()
    showroot.geometry('475x650+800+230')
    showroot.iconbitmap('school.icon.ico')
    showroot.resizable(False,False)
    showroot.config(bg='blue')
#-------------------------------------------------------------------------------------------------------------------------------#
    idlabel = Label(showroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(showroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(showroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(showroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(showroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(showroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(showroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------
    identry = Entry(showroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(showroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(showroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)
    showroot.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------#
    
def exportstudent():
    exportroot = Toplevel()
    exportroot.grab_set()
    exportroot.geometry('475x650+800+230')
    exportroot.iconbitmap('school.icon.ico')
    exportroot.resizable(False,False)
    exportroot.config(bg='blue')
#------------------------------------------------------------------------------------------------------------------------------------#
    idlabel = Label(exportroot,text="Enter Id : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(exportroot,text="Enter Name : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(exportroot,text="Enter Mobile : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(exportroot,text="Enter Email : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(exportroot,text="Enter Address : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(exportroot,text="Enter Gender : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(exportroot,text="Enter DOB : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

#----------------------------------------------------------#   

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

#------------------------------------------------------
    identry = Entry(exportroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(exportroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(exportroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=430)

    exportroot.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------#
def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    print(res)
#######################################################




#######################################################
def Connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('475x63350+800+230')
    dbroot.iconbitmap('school.icon.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #...................................#

    hostlabel = Label(dbroot,text="Enter host : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)

    Userlabel = Label(dbroot,text="Enter User : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter password : ",bg='gold2',font=('times',20, 'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10,y=130)

    hostval = StringVar()
    Userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    Userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=Userval)
    Userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)


    submitbutton = Button(dbroot ,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

#######################################################

def IntroLabelTick():
    global text

#######################################################
from tkinter import *
from tkinter import Toplevel

root = Tk()
root.geometry('1174x700+200+50')
root.title("Student Management System")
root.config(bg="gold2")
root.iconbitmap('school.icon.ico')
root.resizable(False,False)
######################################################
DataEntryFrame = Frame(root,bg="gold2",relief=RIDGE,borderwidth=2)
DataEntryFrame.place(x=10 ,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text="------Welcome-----",width=30,font=('arial','22','italic bold'),bg="gold2")
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1.Add Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2.Search Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3.Delete Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4.Update Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame,text='5.Show Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6.Export Student',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.Exit',width=25,font=('chiller',20,'bold'),bd=6,activebackground='blue',activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

ShowDataFrame = Frame(root,bg="gold2",relief=GROOVE,borderwidth=2)
ShowDataFrame.place(x=500,y=80,width=620,height=600)

ss = 'Welcome To Students Management System'
count = 0
text = ''

SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
SliderLabel.place(x=260, y=0)

connectbutton = Button(root,text='Connect to database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()