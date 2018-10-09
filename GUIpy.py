from tkinter import *
from tkinter import messagebox

from file_to_be_read_by_python import *
#exec(open("GUI2.py").read())


class OneParameter:
    def __init__(self,name,value,changeable=True):
        self.name = name
        self.value = value
        self.changeable = changeable
    def show_parameter(self):
        print(self.name+" = "+str(self.value))

OneParameter("Name",23432).show_parameter()

def wrapq(string):
    return "\'"+string+"\'"

AllParameters = [
                 OneParameter("Method",wrapq(Method)),
                 OneParameter("BorderBehavior",wrapq(BorderBehavior)),
                 OneParameter("numxx",numxx),
                 OneParameter("numyy",numyy),
                 OneParameter("NumberOfAnts",NumberOfAnts),
                 OneParameter("MaxActiveDropletsPerAnt",MaxActiveDropletsPerAnt),
                 OneParameter("IgnoreDropletsFartherThan",IgnoreDropletsFartherThan),
                 OneParameter("TestWithGivenTrail",TestWithGivenTrail),
                 OneParameter("GivenTrailType",wrapq(GivenTrailType)),
                 OneParameter("PheroNarrow",PheroNarrow),
                 OneParameter("PheroHigh",PheroHigh),
                 OneParameter("Pi",3.1415926535,False),
                 OneParameter("seed1",seed1),
                 OneParameter("TurnOffRandom",TurnOffRandom),
                 OneParameter("RegularizingEpsilon",RegularizingEpsilon),
                 OneParameter("t_hat_in_seconds",t_hat_in_seconds),
                 OneParameter("X_hat_in_cm",X_hat_in_cm),
                 OneParameter("tau",tau),
                 OneParameter("TAU","tau / t_hat_in_seconds",False),
                 OneParameter("SensingAreaRadius",SensingAreaRadius),
                 OneParameter("SENSING_AREA_RADIUS",\
                 "SensingAreaRadius / X_hat_in_cm",False),
                 OneParameter("SensingAreaHalfAngle",SensingAreaHalfAngle),
                 OneParameter("NaturalVelocityIncmsec",NaturalVelocityIncmsec),
                 OneParameter("NaturalVelocity",\
                 "NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm",False),
                 OneParameter("delta_t",delta_t),
                 OneParameter("Diffusion",Diffusion),
                 OneParameter("Evaporation",Evaporation),
                 OneParameter("DropletAmountPerUnitTime",DropletAmountPerUnitTime),
                 OneParameter("DropletAmount",\
                 "DropletAmountPerUnitTime * delta_t",False),
                 OneParameter("Threshold",Threshold),
                 OneParameter("LambdaDeltas",\
                 "NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",False),
                 OneParameter("LambdaNonlocal",\
                 "(3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))",False),
                 OneParameter("Lambda",Lambda),
                 OneParameter("SensitivityMethod",wrapq(SensitivityMethod)),
                 OneParameter("x_1_cm",x_1_cm),
                 OneParameter("x_2_cm",x_2_cm),
                 OneParameter("y_1_cm",y_1_cm),
                 OneParameter("y_2_cm",y_2_cm),
                 OneParameter("x_1","x_1_cm / X_hat_in_cm",False),
                 OneParameter("x_2","x_2_cm / X_hat_in_cm",False),
                 OneParameter("y_1","y_1_cm / X_hat_in_cm",False),
                 OneParameter("y_2","y_2_cm / X_hat_in_cm",False),
                 OneParameter("delta_x","(x_2-x_1)/numxx",False),
                 OneParameter("delta_y","(y_2-y_1)/numyy",False),
                 OneParameter("RNumber",RNumber),
                 OneParameter("ThetaNumber",ThetaNumber),
                 OneParameter("DRSector","SENSING_AREA_RADIUS / (RNumber)",False),
                 OneParameter("DThetaSector","SensingAreaHalfAngle / (ThetaNumber)",False),
                 OneParameter("ChangedSide",ChangedSide)
                 ]


def haha(param):
    param.show_parameter()
pp = OneParameter("Name2",23432,False)
haha(pp)


#varslist = [var1,var2,var3,var4]
#typelist = [type1,type2,type3,type4]
varslist = AllParameters

def SetupEntryField(varslist,window):
    nr_of_vars = len(varslist)
    entry_list = [0]*nr_of_vars
    entry_labels = [0]*nr_of_vars
    lines_on_the_window = 15
    li = lines_on_the_window
    for i in range(nr_of_vars):
        entry_labels[i] = Label(window, text=varslist[i].name)
        entry_labels[i].grid(sticky=W,ipadx="1cm",column=2*int(i/li),row=i%li+1)
        entry_list[i] = Entry(window, width=10,state=varslist[i].changeable*'normal'+ (1-varslist[i].changeable)*'disabled')
        entry_list[i].insert(0,varslist[i].value)
        entry_list[i].grid(column=2*int(i/li)+1,row=i%li+1)
    return entry_list, entry_labels
        






window = Tk()

window.title("Ants GUI")

window.geometry('1200x500')

#lbl = Label(window, text=var1)

#lbl.grid(column=0, row=0)

#txt = Entry(window,width=10)
#txt.insert(END,var1)
#txt.grid(column=1, row=0)
#txt.focus()
#
#txt2 = Entry(window,width=10)
#txt2.insert(END,var2)
#txt2.grid(column=1, row=1)
#
#duas = list(range(3))
#duas[1] = txt
#duas[1].delete(0,END)
#duas[1].insert(0,"fgfgfgfgfg")

[entry_values, entry_labels] = SetupEntryField(varslist,window)
entry_values[0].focus()



def write_python_file(event=None):
    #    lbl.configure(text= entry_values[0].get())
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
#    messagebox.showinfo("","Data was written to python file")


def write_files(event=None):
    write_python_file()
    messagebox.showinfo("","Data was written to file")

window.bind("<Return>",write_files)
#window.bind("<Return>",write_python_file)

btn = Button(window, text="Click Me or press Return", command=write_files)

btn.grid(column=0, row=0)

window.mainloop()





