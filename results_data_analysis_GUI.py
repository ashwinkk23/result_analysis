#Importing modules
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re
import os
import sys
import matplotlib
import seaborn as sns
from pandas.tools.plotting import table
from matplotlib.backends.backend_pdf import PdfPages
import Tkinter
import tkMessageBox

#Counts Grades
def analyse(result):
    Sp = 0
    S = 0
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    X = 0
    for grade in result:
        if grade == 'S+':
            Sp = Sp + 1
        elif grade == 'S':
            S = S + 1
        elif grade == 'A':
            A = A + 1
        elif grade == 'B':
            B = B + 1
        elif grade == 'C':
            C = C + 1
        elif grade == D:
            D = D + 1
        elif grade == 'E':
            E = E + 1
        elif grade == 'F':
            F = F + 1
        elif grade == 'X':
            X = X + 1
        else:
            pass
    outlist = [("S+",int(Sp)),
              ("S",int(S)),
              ("A",int(A)),
              ("B",int(B)),
              ("C",int(C)),
              ("D",int(D)),
              ("E",int(E)),
              ("F",int(F)),
              ("X",int(X))]
    return outlist

#counts Total result
def TotRes(res):
    fcd = 0
    fc = 0
    sc = 0
    p = 0
    f = 0
    for ele in res:
        if ele == 'FCD':
            fcd = fcd + 1
        elif ele == 'FC':
            fc = fc + 1
        elif ele == 'SC':
            sc = sc + 1
        elif ele == 'P':
            p = p + 1
        elif ele == 'F':
            f = f + 1
        else:
            pass
    otlst = [('FCD',fcd),
                ('FC',fc),
                ('SC',sc),
                ('P',p),
                ('F',f)]
    return otlst

def main():
    global dep,EC,CS,EE,ME,CV
    def initilize():
        #Reading Data
        try:
            data_file = e1.get()
            rd = pd.read_csv(data_file)
        except:
            tkMessageBox.showinfo("Error!","Data File doesnt exist.")
        
        if int(radio.get()) == 1:
            dep = 'EC'
        elif int(radio.get()) == 2:
            dep = 'CS'
        elif int(radio.get()) == 3:
            dep = 'EE'
        elif int(radio.get()) == 4:
            dep = 'ME'
        elif int(radio.get()) == 5:
            dep = 'CV'
        else:
            #dep = "Enter department"
            #print(dep)
            tkMessageBox.showinfo("Error!","Choose Valid Department")

        #Extracting required information, type = list
        df42 = rd.iloc[:,3]
        df43 = rd.iloc[:,4]
        df44 = rd.iloc[:,5]
        df45 = rd.iloc[:,6]
        df46 = rd.iloc[:,7]
        df47 = rd.iloc[:,8]
        df48 = rd.iloc[:,9]
        df41 = rd.iloc[:,10]
        result = rd.iloc[:,13]

        #Analysing data to plot
        ec42 = analyse(df42)
        ec43 = analyse(df43)
        ec44 = analyse(df44)
        ec45 = analyse(df45)
        ec46 = analyse(df46)
        ec47 = analyse(df47)
        ec48 = analyse(df48)
        ec41 = analyse(df41)
        tot = TotRes(result)

        #Creating DataFrame's
        lable1 = ['Grade','Number']
        dfec42=pd.DataFrame.from_records(ec42,columns=lable1)
        dfec43=pd.DataFrame.from_records(ec43,columns=lable1)
        dfec44=pd.DataFrame.from_records(ec44,columns=lable1)
        dfec45=pd.DataFrame.from_records(ec45,columns=lable1)
        dfec46=pd.DataFrame.from_records(ec46,columns=lable1)
        dfec47=pd.DataFrame.from_records(ec47,columns=lable1)
        dfec48=pd.DataFrame.from_records(ec48,columns=lable1)
        dfec41=pd.DataFrame.from_records(ec41,columns=lable1)
        lable2 = ['Result','Number']
        tot_res = pd.DataFrame.from_records(tot,columns=lable2)

        #print("Analysis completed!")
        #print(e2.get())
        #print(dep)
        
                
        #print("MAT"+dep+"41")
        fig1 = plt.figure(1)
        sns.barplot(x="Grade", y="Number", data=dfec41,palette="Reds_d")
        fig1.suptitle("MAT"+dep+"41",fontsize = 14,fontweight ='bold')
        #fig1.show()

        fig2 = plt.figure(2)
        result = dfec41.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig2.suptitle("MAT"+dep+"41_HeatMap",fontsize = 14,fontweight ='bold')
        #fig2.show()

        #print(dep+"42")
        fig3 = plt.figure(3)
        sns.barplot(x="Grade", y="Number", data=dfec42,palette="Greens_d")
        fig3.suptitle(dep+"42",fontsize = 14,fontweight ='bold')
        #fig3.show()

        fig4 = plt.figure(4)
        result = dfec42.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig4.suptitle(dep+"42_HeatMap",fontsize = 14,fontweight ='bold')
        #fig4.show()

        #print(dep+"43")
        fig5 = plt.figure(5)
        sns.barplot(x="Grade", y="Number", data=dfec43,palette="Blues_d")
        fig5.suptitle(dep+"43",fontsize = 14,fontweight ='bold')
        #fig5.show()

        fig6 = plt.figure(6)
        result = dfec43.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig6.suptitle(dep+"43_HeatMap",fontsize = 14,fontweight ='bold')
        #fig6.show()

        #print(dep+"44")
        fig7 = plt.figure(7)
        sns.barplot(x="Grade", y="Number", data=dfec44,palette="Purples_d")
        fig7.suptitle(dep+"44",fontsize = 14,fontweight ='bold')
        #fig7.show()

        fig8 = plt.figure(8)
        result = dfec44.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig8.suptitle(dep+"44_HeatMap",fontsize = 14,fontweight ='bold')
        #fig8.show()

        #print(dep+"45")
        fig9 = plt.figure(9)
        sns.barplot(x="Grade", y="Number", data=dfec45,palette="BuGn_r")
        fig9.suptitle(dep+"45",fontsize = 14,fontweight ='bold')
        #fig9.show()

        fig10 = plt.figure(10)
        result = dfec45.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig10.suptitle(dep+"45_HeatMap",fontsize = 14,fontweight ='bold')
        #fig10.show()

        #print(dep+"46")
        fig11 = plt.figure(11)
        sns.barplot(x="Grade", y="Number", data=dfec46,palette="GnBu_d")
        fig11.suptitle(dep+"46",fontsize = 14,fontweight ='bold')
        #fig11.show()

        fig12 = plt.figure(12)
        result = dfec46.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig12.suptitle(dep+"46_HeatMap",fontsize = 14,fontweight ='bold')
        #fig12.show()

        #print(dep+"L47")
        fig13 = plt.figure(13)
        sns.barplot(x="Grade", y="Number", data=dfec47,palette="RdBu_r")
        fig13.suptitle(dep+"L47",fontsize = 14,fontweight ='bold')
        #fig13.show()

        fig14 = plt.figure(14)
        result = dfec47.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig14.suptitle(dep+"L47_HeatMap",fontsize = 14,fontweight ='bold')
        #fig14.show()

        #print(dep+"L48")
        fig15 = plt.figure(15)
        sns.barplot(x="Grade", y="Number", data=dfec48,palette="YlGn")
        fig15.suptitle(dep+"L48",fontsize = 14,fontweight ='bold')
        #fig15.show()

        fig16 = plt.figure(16)
        result = dfec48.pivot(index='Grade',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig16.suptitle(dep+"L48_HeatMap",fontsize = 14,fontweight ='bold')
        #fig16.show()

        #print("Overall Result")
        fig17 = plt.figure(17)
        sns.barplot(x='Result',y='Number',data=tot_res,palette="OrRd")
        fig17.suptitle("Overall Result",fontsize = 14,fontweight ='bold')
        #fig17.show()

        fig18 = plt.figure(18)
        result = tot_res.pivot(index='Result',columns='Number',values='Number')
        sns.heatmap(result,square=True,annot=True)
        fig18.suptitle("OverAll_Result_HeatMap",fontsize = 14,fontweight ='bold')
        #fig18.show()

        #Saving Result to PDF file
        #print ('Generating PDF Report\n')
        pp = PdfPages(str(e2.get())+'.pdf')
        pp.savefig(fig1)
        pp.savefig(fig2)
        pp.savefig(fig3)
        pp.savefig(fig4)
        pp.savefig(fig5)
        pp.savefig(fig6)
        pp.savefig(fig7)
        pp.savefig(fig8)
        pp.savefig(fig9)
        pp.savefig(fig10)
        pp.savefig(fig11)
        pp.savefig(fig12)
        pp.savefig(fig13)
        pp.savefig(fig14)
        pp.savefig(fig15)
        pp.savefig(fig16)
        pp.savefig(fig17)
        pp.savefig(fig18)
        pp.close()
        tkMessageBox.showinfo("Complete","All Done!!!")
        os.startfile(str(e2.get())+'.pdf')
        sys.exit()
    top = Tkinter.Tk()
    top.geometry('250x330')
    clr = '#%02x%02x%02x' % (230, 230, 230)
    top.configure(bg=clr)
    top.grid()
    radio = Tkinter.IntVar()
    b1 = Tkinter.Button(top,text='START',command=initilize,bd=5,height=1,width=10,relief=Tkinter.RAISED,anchor=Tkinter.CENTER,bg='grey')
    b1.pack(side=Tkinter.BOTTOM,expand=Tkinter.NO)
    l1 = Tkinter.Label(top,text='Enter name of data file:',height=-1,width=-1,bd=5,bg=clr)
    l1.pack(anchor = Tkinter.W)
    e1 = Tkinter.Entry(top,bd=7,width = 38)
    e1.pack(expand=Tkinter.NO,anchor=Tkinter.CENTER)
    l2 = Tkinter.Label(top,text='Enter Department:',height=-1,width=-1,bd=5,bg=clr)
    l2.pack(anchor = Tkinter.W)
    r1 = Tkinter.Radiobutton(top,text='EC',variable = radio,value=1,bg=clr)
    r1.pack(anchor = Tkinter.W)
    r2 = Tkinter.Radiobutton(top,text='CS',variable = radio,value=2,bg=clr)
    r2.pack(anchor = Tkinter.W)
    r3 = Tkinter.Radiobutton(top,text='EE',variable = radio,value=3,bg=clr)
    r3.pack(anchor = Tkinter.W)
    r4 = Tkinter.Radiobutton(top,text='ME',variable = radio,value=4,bg=clr)
    r4.pack(anchor = Tkinter.W)
    r5 = Tkinter.Radiobutton(top,text='CV',variable = radio,value=5,bg=clr)
    r5.pack(anchor = Tkinter.W)
    l3 = Tkinter.Label(top,text="Enter the name of PDF report file.",height=-1,width=-1,bd=5,bg=clr)
    l3.pack(anchor = Tkinter.W)
    e2 = Tkinter.Entry(top,bd=7,width=38)
    e2.pack(expan = Tkinter.NO,anchor=Tkinter.CENTER)
    
    top.iconbitmap('data.ico')
    top.wm_title('Data Analysis')
    top.mainloop()

if __name__ == "__main__":
    main()