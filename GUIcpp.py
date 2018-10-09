from tkinter import *
from tkinter import messagebox

from Parameters import *
#exec(open("GUI2.py").read())


class OneParameter:
    def __init__(self,cpp_stuff,name,value,changeable=True):
        self.cpp_stuff = cpp_stuff
        self.name = name
        self.value = value
        self.changeable = changeable
    def show_parameter(self):
        print(self.cpp_stuff+"\t"+self.name+" = "+str(self.value))

OneParameter("static bla bla","Name",23432).show_parameter()

AllParameters = [
                 OneParameter("static string","Method","\'\'"),
                 OneParameter("static string","BorderBehavior","\'periodic\'"),
                 OneParameter("static double const","numxx",100.),
                 OneParameter("static double const","numyy",100.),
                 OneParameter("static int const","NumberOfAnts",25),
                 OneParameter("static int const","MaxActiveDropletsPerAnt",500),
                 OneParameter("static double const","IgnoreDropletsFartherThan",5.),
                 OneParameter("static int const","TestWithGivenTrail",0),
                 OneParameter("static string","GivenTrailType","\'\'"),
                 OneParameter("static double const","PheroNarrow",8.),
                 OneParameter("static double const","PheroHigh",5.),
                 OneParameter("static double const","Pi",3.1415926535),
                 OneParameter("unsigned","seed1",3536835118),
                 OneParameter("static double const","TurnOffRandom",3.),
                 OneParameter("static double const","RegularizingEpsilon",0.01),
                 OneParameter("static double const","t_hat_in_seconds",1.),
                 OneParameter("static double const","X_hat_in_cm",1.),
                 OneParameter("static double const","tau",.1),
                 OneParameter("static double const","TAU","tau / t_hat_in_seconds",False),
                 OneParameter("static double const","SensingAreaRadius",.8),
                 OneParameter("static double const","SENSING_AREA_RADIUS",\
                 "SensingAreaRadius / X_hat_in_cm",False),
                 OneParameter("static double const","SensingAreaHalfAngle","1.*Pi/4."),
                 OneParameter("static double const","NaturalVelocityIncmsec",2.),
                 OneParameter("static double const","NaturalVelocity",\
                 "NaturalVelocityIncmsec * t_hat_in_seconds / X_hat_in_cm",False),
                 OneParameter("static double const","delta_t",0.1),
                 OneParameter("static double const","Diffusion",0.002),
                 OneParameter("static double const","Evaporation",0.01),
                 OneParameter("static double const","DropletAmountPerUnitTime",1.),
                 OneParameter("static double const","DropletAmount",\
                 "DropletAmountPerUnitTime * delta_t",False),
                 OneParameter("static double const","Threshold",0.7),
                 OneParameter("static double const","LambdaDeltas",\
                 "NaturalVelocity/(SENSING_AREA_RADIUS*np.cos(SensingAreaHalfAngle))",False),
                 OneParameter("static double const","LambdaNonlocal",\
                 "(3./2.)*NaturalVelocity*SensingAreaHalfAngle/(SENSING_AREA_RADIUS*np.sin(SensingAreaHalfAngle))",False),
                 OneParameter("static double const","Lambda",1.),
                 OneParameter("string","SensitivityMethod","\'\'"),
                 OneParameter("static double const","x_1_cm",-30.),
                 OneParameter("static double const","x_2_cm",30.),
                 OneParameter("static double const","y_1_cm",-30.),
                 OneParameter("static double const","y_2_cm",30.),
                 OneParameter("static double const","x_1","x_1_cm / X_hat_in_cm",False),
                 OneParameter("static double const","x_2","x_2_cm / X_hat_in_cm",False),
                 OneParameter("static double const","y_1","y_1_cm / X_hat_in_cm",False),
                 OneParameter("static double const","y_2","y_2_cm / X_hat_in_cm",False),
                 OneParameter("static double const","delta_x","(x_2-x_1)/numxx",False),
                 OneParameter("static double const","delta_y","(y_2-y_1)/numyy",False),
                 OneParameter("static int const","RNumber",5),
                 OneParameter("static int const","ThetaNumber",5),
                 OneParameter("static double const","DRSector","SENSING_AREA_RADIUS / (RNumber)",False),
                 OneParameter("static double const","DThetaSector","SensingAreaHalfAngle / (ThetaNumber)",False),
                 OneParameter("static int const","ChangedSide",0)
                 ]


def haha(param):
    param.show_parameter()
pp = OneParameter("static yadaydad","Name2",23432,False)
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

lbl = Label(window, text=var1)

lbl.grid(column=0, row=0)

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


def write_cpp_file(event=None):
    #    lbl.configure(text= entry_values[0].get())
    filename = "file_to_be_read_by_cpp.cpp"
    f = open(filename,"w").close()
    f = open(filename,"a")
    for i in range(len(varslist)):
        if  varslist[i].changeable:
            f.write(varslist[i].cpp_stuff+" "+varslist[i].name+" = "+ entry_values[i].get()+';\n')
        else:
            f.write(varslist[i].cpp_stuff+" "+varslist[i].name+" = "+ varslist[i].value+';\n')
    f.close()
#    messagebox.showinfo("","Data was written to cpp file")

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
            f.write(varslist[i].name+" = "+ varslist[i].value+'\n')
    f.close()
#    messagebox.showinfo("","Data was written to python file")


def write_files(event=None):
    write_cpp_file()
    write_python_file()
    messagebox.showinfo("","Data was written to files")

window.bind("<Return>",write_files)
#window.bind("<Return>",write_python_file)

btn = Button(window, text="Click Me or press Return", command=write_files)

btn.grid(column=0, row=0)

window.mainloop()





