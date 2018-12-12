from tkinter import *
from tkinter import messagebox
import shutil
import os
import numpy as np

lastusedpath = 'last_used_parameters.py'
default_path = 'default_parameters.py'

#from default_parameters import *

#NumberOfAnts = 2
#MaxActiveDropletsPerAnt = 300
##Pi = Pi
#seed1 = 1
#t_hat_in_seconds = 1.0
#X_hat_in_cm = 1.0
#tau = 0.1
#TAU = tau / t_hat_in_seconds
#SensingAreaRadius = 1.0
#SENSING_AREA_RADIUS = SensingAreaRadius / X_hat_in_cm
#SensingAreaHalfAnglePiOver = 4.0
#SensingAreaHalfAngle = np.pi/SensingAreaHalfAnglePiOver
#NaturalVelocityIncmsec = 3.5
#NaturalVelocity = NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm
#delta_t = 0.1
#Diffusion = 0.003
#Evaporation = 0.0001
#DropletAmountPerUnitTime = 10.0
#DropletAmount = DropletAmountPerUnitTime * delta_t
#Threshold = 0.2
#LambdaDeltas = NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))
#LambdaNonlocal = (3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))
#Lambda = 1.0
#x_1_cm = -10
#x_2_cm = 10
#y_1_cm = -10
#y_2_cm = 10
#x_1 = x_1_cm / X_hat_in_cm
#x_2 = x_2_cm / X_hat_in_cm
#y_1 = y_1_cm / X_hat_in_cm
#y_2 = y_2_cm / X_hat_in_cm



#from file_to_be_read_by_python import *
#exec(open("GUI2.py").read())



class OneParameter:
    def __init__(self,name=None,value=None,formula=None,changeable=True,default=None):
        if name == None:
            self.name = ''
        else:
            self.name = name
        if value != None:
            self.value = value
        else:
            self.value = default
        if formula != None:
            self.formula = formula
        else:
            self.formula = name
        self.changeable = changeable
        if default == None:
            self.default = value
        else:
            self.default = default
    def show_parameter(self):
        print(self.name+" = "+str(self.value),"  Default = "+str(self.default))

#OneParameter("Name",23432).show_parameter()

def wrapq(string):
    return "\'"+string+"\'"


def DefineParameters():
    Parameters = [
                OneParameter(name="NumberOfAnts",value=NumberOfAnts),
                OneParameter(name="MaxActiveDropletsPerAnt",value=MaxActiveDropletsPerAnt),
                OneParameter(name="seed1", value=seed1),
                OneParameter(name="t_hat_in_seconds",value=t_hat_in_seconds),
                OneParameter(name="X_hat_in_cm",value=X_hat_in_cm),
                OneParameter(name="tau",value=tau),
                OneParameter(name="TAU",value=TAU, formula="tau / t_hat_in_seconds",changeable=False),
                OneParameter(name="SensingAreaRadius",value=SensingAreaRadius),
                OneParameter(name="SENSING_AREA_RADIUS",value=SENSING_AREA_RADIUS,formula="SensingAreaRadius /X_hat_in_cm",changeable=False),
                OneParameter(name="SensingAreaHalfAnglePiOver",value=SensingAreaHalfAnglePiOver),
                OneParameter(name="SensingAreaHalfAngle",value=SensingAreaHalfAngle, formula="np.pi/SensingAreaHalfAnglePiOver",changeable=False),
                OneParameter(name="NaturalVelocityIncmsec",value=NaturalVelocityIncmsec),
                OneParameter(name="NaturalVelocity",value=NaturalVelocity, formula="NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm", changeable=False),
                OneParameter(name="delta_t",value=delta_t),
                OneParameter(name="Diffusion",value=Diffusion),
                OneParameter(name="Evaporation",value=Evaporation),
                OneParameter(name="DropletAmountPerUnitTime",value=DropletAmountPerUnitTime),
                OneParameter(name="DropletAmount",value=DropletAmount,formula="DropletAmountPerUnitTime * delta_t",changeable=False),
                OneParameter(name="Threshold",value=Threshold),
                OneParameter(name="LambdaDeltas",value=LambdaDeltas,formula="NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",changeable=False),
                OneParameter(name="x_1_cm",value=x_1_cm),
                OneParameter(name="x_2_cm",value=x_2_cm),
                OneParameter(name="y_1_cm",value=y_1_cm),
                OneParameter(name="y_2_cm",value=y_2_cm),
                OneParameter(name="x_1",value=x_1, formula="x_1_cm / X_hat_in_cm",changeable=False),
                OneParameter(name="x_2",value=x_2, formula="x_2_cm / X_hat_in_cm",changeable=False),
                OneParameter(name="y_1",value=y_1, formula="y_1_cm / X_hat_in_cm",changeable=False),
                OneParameter(name="y_2",value=y_2, formula="y_2_cm / X_hat_in_cm",changeable=False),
                ]
    return Parameters

#def DefineParametersAAAAAA():
#    Parameters = {
#                "NumberOfAnts": OneParameter(default=2),
#                "MaxActiveDropletsPerAnt": OneParameter(default=300),
#                "seed1": OneParameter(default=1),
#                "t_hat_in_seconds": OneParameter(default=1.),
#                "X_hat_in_cm": OneParameter(default=1.),
#                "tau": OneParameter(default=0.1),
#                "TAU": OneParameter(value=tau / t_hat_in_seconds, formula="tau / t_hat_in_seconds",changeable=False),
#                "SensingAreaRadius": OneParameter(default=1.),
#                "SENSING_AREA_RADIUS": OneParameter(value=SensingAreaRadius / X_hat_in_cm,formula="SensingAreaRadius /X_hat_in_cm",changeable=False),
#                "SensingAreaHalfAnglePiOver": OneParameter(default=4.),
#                "SensingAreaHalfAngle": OneParameter(value=np.pi/SensingAreaHalfAnglePiOver, formula="np.pi/SensingAreaHalfAnglePiOver",changeable=False),
#                "NaturalVelocityIncmsec": OneParameter(default=3.5),
#                "NaturalVelocity": OneParameter(value=NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm, formula="NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm", changeable=False),
#                "delta_t": OneParameter(default=0.1),
#                "Diffusion": OneParameter(default=0.003),
#                "Evaporation": OneParameter(default=0.0001),
#                "DropletAmountPerUnitTime": OneParameter(default=10.),
#                "DropletAmount": OneParameter(value=DropletAmountPerUnitTime * delta_t,formula="DropletAmountPerUnitTime * delta_t",changeable=False),
#                "Threshold": OneParameter(default=0.2),
#                "LambdaDeltas": OneParameter(value=NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle)),formula="NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",changeable=False),
#                "x_1_cm": OneParameter(default=-10),
#                "x_1_cm": OneParameter(default=10),
#                "y_1_cm": OneParameter(default=-10),
#                "y_2_cm": OneParameter(default=10),
#                "x_1": OneParameter(value=x_1_cm / X_hat_in_cm,formula="x_1_cm / X_hat_in_cm",changeable=False),
#                "x_2": OneParameter(value=x_2_cm / X_hat_in_cm,formula="x_2_cm / X_hat_in_cm",changeable=False),
#                "y_1": OneParameter(value=y_1_cm / X_hat_in_cm,formula="y_1_cm / X_hat_in_cm",changeable=False),
#                "y_2": OneParameter(value=y_2_cm / X_hat_in_cm,formula="y_2_cm / X_hat_in_cm",changeable=False),
#                }
#    
#    AllParameters = [
#                     OneParameter("NumberOfAnts",default=2),
#                     OneParameter("MaxActiveDropletsPerAnt",default=300),
#                     OneParameter("Pi",value=3.1415926535,changeable=False),
#                     OneParameter("seed1",default=1),
#                     OneParameter("t_hat_in_seconds",default=1.),
#                     OneParameter("X_hat_in_cm",default=1.),
#                     OneParameter("tau",default=0.1),
#                     OneParameter("TAU",formula="tau / t_hat_in_seconds",changeable=False),
#                     OneParameter("SensingAreaRadius",default=1.),
#                     OneParameter("SENSING_AREA_RADIUS",formula="SensingAreaRadius / X_hat_in_cm",changeable=False),
#                     OneParameter("SensingAreaHalfAnglePiOver",default=4.),
#                     OneParameter("SensingAreaHalfAngle",formula="np.pi/SensingAreaHalfAnglePiOver",changeable=False),
#                     OneParameter("NaturalVelocityIncmsec",default=3.5),
#                     OneParameter("NaturalVelocity",formula="NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm",changeable=False),
#                     OneParameter("delta_t",default=0.1),
#                     OneParameter("Diffusion",default=0.003),
#                     OneParameter("Evaporation",default=0.0001),
#                     OneParameter("DropletAmountPerUnitTime",default=10.),
#                     OneParameter("DropletAmount",formula="DropletAmountPerUnitTime * delta_t",changeable=False),
#                     OneParameter("Threshold",default=0.2),
#                     OneParameter("LambdaDeltas",formula="NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",changeable=False),
#                     OneParameter("LambdaNonlocal",formula="(3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))",changeable=False),
#                     OneParameter("Lambda",default=1.),
#                     OneParameter("x_1_cm",default=-10),
#                     OneParameter("x_2_cm",default=10),
#                     OneParameter("y_1_cm",default=-10),
#                     OneParameter("y_2_cm",default=10),
#                     OneParameter("x_1",formula="x_1_cm / X_hat_in_cm",changeable=False),
#                     OneParameter("x_2",formula="x_2_cm / X_hat_in_cm",changeable=False),
#                     OneParameter("y_1",formula="y_1_cm / X_hat_in_cm",changeable=False),
#                     OneParameter("y_2",formula="y_2_cm / X_hat_in_cm",changeable=False),
#                     ]
#    return AllParameters

if not os.path.exists(lastusedpath):
    shutil.copy(default_path,lastusedpath)

from default_parameters import *

defaults = DefineParameters()

from last_used_parameters import *

varslist = DefineParameters()

for k in range(len(varslist)):
    varslist[k].default = defaults[k].value



#def write_defaults(event=None):
#    global default_path
#    filename = default_path
#    f = open(filename,"w").close()
#    f = open(filename,"a")
#    f.write('import numpy as np\n')
#    for i in range(len(varslist)):
#        if  varslist[i].changeable:
#            f.write(varslist[i].name+" = "+ str(varslist[i].default)+'\n')
#        else:
#            f.write(varslist[i].name+" = "+ str(varslist[i].value)+'\n')
#    f.close()
##    if not os.path.exists('file_to_be_read_by_python.py'):
#    shutil.copy(filename,'file_to_be_read_by_python.py')
#    shutil.copy(filename,lastusedpath)



def write_python_file(event=None):
    global lastusedpath
    filename = "file_to_be_read_by_python.py"
    f = open(filename,"w").close()
    f = open(filename,"a")
    f.write('import numpy as np\n')
    for i in range(len(varslist)):
        if  varslist[i].changeable:
            f.write(varslist[i].name+" = "+ entry_values[i].get()+'\n')
        else:
            f.write(varslist[i].name+" = "+ str(varslist[i].value)+'\n')
    f.close()
    shutil.copy(filename,lastusedpath)
#    messagebox.showinfo("","Data was written to python file")



#write_defaults()


window = Tk()
window.title("Ants GUI")
window.geometry('1200x500')


def SetupEntryField(varslist,window):
    nr_of_vars = len(varslist)
    entry_list = [0]*nr_of_vars
    entry_labels = [0]*nr_of_vars
    lines_on_the_window = 16
    li = lines_on_the_window
    counter=-1
    for var in varslist:
        counter += 1
        i = counter
        if var.changeable:
            entry_labels[i] = Label(window, text=var.name+' ('+str(var.default)+')')
            entry_labels[i].grid(sticky=W,ipadx="2cm",column=2*int(i/li),row=i%li+1)
            entry_list[i] = Entry(window, width=10,state='normal')
            entry_list[i].insert(0,var.value)
            entry_list[i].grid(column=2*int(i/li)+1,row=i%li+1)
        else:
            entry_labels[i] = Label(window, text=var.name)
            entry_labels[i].grid(sticky=W,ipadx="2cm",column=2*int(i/li),row=i%li+1)
            entry_list[i] = Label(window, text=var.value)
            entry_list[i].grid(column=2*int(i/li)+1,row=i%li+1)
    return entry_list, entry_labels


def UseDefaults(event=None):
    print("AAAAA")
    shutil.copy(default_path,'file_to_be_read_by_python.py')
    shutil.copy(default_path,lastusedpath)
#    pass

#def UseLast(event=None):
#    shutil.copy(lastusedpath,'file_to_be_read_by_python.py')
##    pass
#
#def DefineValues(event=None):
#    pass

def write_files(event=None):
    write_python_file()
    messagebox.showinfo("","Data was written to file")

window.bind('<Return>',write_files)
window.bind('<Control-Key-1>',UseDefaults)

btn1 = Button(window, text="Cntr-1: Use defaults", command=UseDefaults)
btn1.grid(column=0, row=0)

btn2 = Button(window, text="Ret: Use present values", command=write_files)
btn2.grid(column=1, row=0)


import platform
if platform.system() == 'Darwin':
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

[entry_values, entry_labels] = SetupEntryField(varslist,window)
entry_values[0].focus()

#btn1 = Button(window, text="1: Use defauls", command=UseDefaults)
#btn1.grid(column=0, row=0)
#
#btn2 = Button(window, text="2: Use last values", command=UseLast)
#btn2.grid(column=1, row=0)
#
#btn3 = Button(window, text="3: Change values", command=DefineValues)
#btn3.grid(column=2, row=0)



window.mainloop()
#
#
#
#def nothing(event=None):
#    pass
#
#window = Tk()
#
#window.title("Ants GUI")
#
#window.geometry('1200x500')
#btn1 = Button(window, text="1: Use defauls", command=UseDefaults)
#btn1.grid(column=0, row=0)
#
#btn2 = Button(window, text="2: Use last values", command=UseLast)
#btn2.grid(column=1, row=0)
#
#btn3 = Button(window, text="3: Change values", command=DefineValues)
#btn3.grid(column=0, row=0)
#
#window.mainloop()
#
#print("ahahaha")
#
#if os.path.exists(lastusedpath):
#    from last_used_parameters import *
#else:
#    from default_parameters import *
#
#
##def DefineParameters()
##    AllParameters = [
##                     OneParameter("NumberOfAnts",NumberOfAnts,default=2),
##                     OneParameter("MaxActiveDropletsPerAnt",MaxActiveDropletsPerAnt,default=300),
##                     OneParameter("Pi",3.1415926535,changeable=False),
##                     OneParameter("seed1",seed1,default=1),
##                     OneParameter("t_hat_in_seconds",t_hat_in_seconds,default=1.),
##                     OneParameter("X_hat_in_cm",X_hat_in_cm,default=1.),
##                     OneParameter("tau",tau,default=0.1),
##                     OneParameter("TAU",tau / t_hat_in_seconds,"tau / t_hat_in_seconds",False),
##                     OneParameter("SensingAreaRadius",SensingAreaRadius,default=1.),
##                     OneParameter("SENSING_AREA_RADIUS",SensingAreaRadius / X_hat_in_cm,\
##                     "SensingAreaRadius / X_hat_in_cm",False),
##                     OneParameter("SensingAreaHalfAngle",SensingAreaHalfAngle,default=np.pi/4.),
##                     OneParameter("NaturalVelocityIncmsec",NaturalVelocityIncmsec,default=3.5),
##                     OneParameter("NaturalVelocity",NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm,\
##                     "NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm",False),
##                     OneParameter("delta_t",delta_t,default=0.1),
##                     OneParameter("Diffusion",Diffusion,default=0.003),
##                     OneParameter("Evaporation",Evaporation,default=0.0001),
##                     OneParameter("DropletAmountPerUnitTime",DropletAmountPerUnitTime,default=10.),
##                     OneParameter("DropletAmount",DropletAmountPerUnitTime * delta_t,\
##                     "DropletAmountPerUnitTime * delta_t",False),
##                     OneParameter("Threshold",Threshold,default=0.2),
##                     OneParameter("LambdaDeltas",NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle)),\
##                     "NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",False),
##                     OneParameter("LambdaNonlocal",(3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle)),\
##                     "(3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))",False),
##                     OneParameter("Lambda",Lambda,default=1.),
##                     OneParameter("x_1_cm",x_1_cm,default=-10),
##                     OneParameter("x_2_cm",x_2_cm,default=10),
##                     OneParameter("y_1_cm",y_1_cm,default=-10),
##                     OneParameter("y_2_cm",y_2_cm,default=10),
##                     OneParameter("x_1",x_1_cm / X_hat_in_cm,"x_1_cm / X_hat_in_cm",False),
##                     OneParameter("x_2",x_2_cm / X_hat_in_cm,"x_2_cm / X_hat_in_cm",False),
##                     OneParameter("y_1",y_1_cm / X_hat_in_cm,"y_1_cm / X_hat_in_cm",False),
##                     OneParameter("y_2",y_2_cm / X_hat_in_cm,"y_2_cm / X_hat_in_cm",False),
##                     OneParameter("ChangedSide",ChangedSide)
##                     ]
##    return AllParameters
#
#
#
#def haha(param):
#    param.show_parameter()
#pp = OneParameter("Name2",23432,False,default=100000)
#haha(pp)
#haha(AllParameters[-2])
#
#
##varslist = [var1,var2,var3,var4]
##typelist = [type1,type2,type3,type4]
##varslist = AllParameters
#
#def SetupEntryField(varslist,window):
#    nr_of_vars = len(varslist)
#    entry_list = [0]*nr_of_vars
#    entry_labels = [0]*nr_of_vars
#    lines_on_the_window = 16
#    li = lines_on_the_window
#    for i in range(nr_of_vars):
#        entry_labels[i] = Label(window, text=varslist[i].name)
#        entry_labels[i].grid(sticky=W,ipadx="2cm",column=2*int(i/li),row=i%li+1)
#        if varslist[i].changeable:
#            entry_list[i] = Entry(window, width=10,state='normal')
#            entry_list[i].insert(0,varslist[i].formula)
#            entry_list[i].grid(column=2*int(i/li)+1,row=i%li+1)
#        else:
#            entry_list[i] = Label(window, text=varslist[i].value)
#            entry_list[i].grid(column=2*int(i/li)+1,row=i%li+1)
#    return entry_list, entry_labels
#        
#
#
#
#
#
#
#
##window.attributes("-topmost", True)
##window.focus_force()
#
#import platform
#if platform.system() == 'Darwin':
#    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
##window.lift()
##window.attributes("-topmost", True)
#
##lbl = Label(window, text=var1)
#
##lbl.grid(column=0, row=0)
#
##txt = Entry(window,width=10)
##txt.insert(END,var1)
##txt.grid(column=1, row=0)
##txt.focus()
##
##txt2 = Entry(window,width=10)
##txt2.insert(END,var2)
##txt2.grid(column=1, row=1)
##
##duas = list(range(3))
##duas[1] = txt
##duas[1].delete(0,END)
##duas[1].insert(0,"fgfgfgfgfg")
#
#[entry_values, entry_labels] = SetupEntryField(varslist,window)
#entry_values[0].focus()
#
#
#
#def write_python_file(event=None):
#    global lastusedpath
#    #    lbl.configure(text= entry_values[0].get())
#    filename = "file_to_be_read_by_python.py"
#    f = open(filename,"w").close()
#    f = open(filename,"a")
#    f.write('import numpy as np\n')
#    for i in range(len(varslist)):
#        if  varslist[i].changeable:
#            f.write(varslist[i].name+" = "+ entry_values[i].get()+'\n')
#        else:
#            f.write(varslist[i].name+" = "+ str(varslist[i].formula)+'\n')
#    f.close()
#    shutil.copy(filename,lastusedpath)
##    messagebox.showinfo("","Data was written to python file")
#
##def write_defaults(event=None):
##    global default_path
##    #    lbl.configure(text= entry_values[0].get())
##    filename = default_path
##    f = open(filename,"w").close()
##    f = open(filename,"a")
##    f.write('import numpy as np\n')
##    for i in range(len(varslist)):
##        if  varslist[i].changeable:
##            f.write(varslist[i].name+" = "+ str(varslist[i].default)+'\n')
##        else:
##            f.write(varslist[i].name+" = "+ str(varslist[i].formula)+'\n')
##    f.close()
##    if not os.path.exists('file_to_be_read_by_python.py'):
##        shutil.copy(default_path,'file_to_be_read_by_python.py')
#
#
#write_defaults()
#
#def write_files(event=None):
#    write_python_file()
#    messagebox.showinfo("","Data was written to file")
#
#window.bind("<Return>",write_files)
##window.bind("<Return>",write_python_file)
#
##btn = Button(window, text="Click Me or press Return", command=write_files)
##
##btn.grid(column=0, row=0)
#
##window.mainloop()
#
#
#
#
#
