import  tkinter
from tkinter import*
from tkinter.ttk import*
#################################variables

ml={'name':['IBM Machine Learning\nProfessional Certificate'],'platform':['coursera'],'duration':['6months'],'price':['2852 inr per month(Financial Aid available)']}#machine learning

ds={'name':['Google Data Analytics\nProfessional Certificate'],'platform':['coursera'],'duration':['6months(10hr/week)'],'price':['1,023 inr per month(Financial Aid available)']}#data science

gd={'name':['Graphic Design Bootcamp: Photoshop, Illustrator, InDesign'],'platform':['udemy'],'duration':['15.5 hrs'],'price':['3,520 inr']}#graphics des

ad={'name':['Flutter Course - Full Tutorial for Beginners \n(Build iOS and Android Apps) by freeCodeCamp.org'],'platform':['youtube'],'duration':['2hrs'],'price':['free']}#app dev




cl=['machine learning','data science','graphics designing','app devlopment']



################################functions

def fndc():
    f = tkinter.Toplevel()
    # rt.iconbitmap('cpy.ico')////////////insert icon ico file when done_______________
    f.title("find a course")
    f.geometry('600x355+250+100')
    f.resizable(0, 0)
    f.config(bg='black')

    lo = tkinter.Label(f, text="Enter the catogry of the course you are intrested to learn", bg='black', fg='#d3e1e6', font=("Arial", 16))  # blank
    lo.pack(pady=10)

    e1=tkinter.Entry(f,font=("Arial", 18))
    e1.pack(pady=15)

    def shwcrse():
        global cl
        global ml
        global ad
        global ds
        global gd
        f1= tkinter.Toplevel()
        # rt.iconbitmap('cpy.ico')////////////insert icon ico file when done_______________
        f1.title("find a course")
        f1.geometry('600x355+250+100')
        f1.resizable(0, 0)
        f1.config(bg='black')
        k=e1.get()
        i=0
        f.destroy()

        k.lower()
        for x in cl:
            if(x==k):
                i+=1
        if(i==0):
            lo = tkinter.Label(f1, text="There is currently no course in our database related to \n\"{}\"".format(k), bg='black',fg='#d3e1e6', font=("Arial", 16))  # blank
            lo.pack(pady=10)
        else:
            if (k == 'machine learning'):
                print(1)
                z = len(ml['name'])
                for x in range(0,z):
                    lx=tkinter.Label(f1, text="name:{}\nplatform:{}\nduration:{}\ncost:{}".format(ml['name'][x],ml['platform'][x],ml['duration'][x],ml['cost'][x]), bg='black',
                                   fg='#d3e1e6',
                                   font=("Arial", 14))  # blank
                lx.pack(pady=10)
                print(z)
            elif (k == 'data science'):
                print(1)
            elif (k == 'graphics designing'):
                print(1)
            elif (k== 'app devlopment'):
                z=len(ml['name'])
                print(z)
                lc = tkinter.Label(f1, text="Enter the catogry of the course you are going to recommend", bg='black',
                                   fg='#d3e1e6',
                                   font=("Arial", 14))  # blank
                lc.pack(pady=10)









    b1 = tkinter.Button(f, text="Search", bg='black', fg='#d3e1e6', font=("Arial", 18),command=shwcrse)  # blank
    b1.pack(pady=20)



##############################_________recommend
def recrse():
    r = tkinter.Toplevel()
    # rt.iconbitmap('cpy.ico')////////////insert icon ico file when done_______________
    r.title("find a course")
    r.geometry('600x620+100+50')
    r.resizable(0, 0)
    r.config(bg='black')

    lc = tkinter.Label(r, text="Enter the catogry of the course you are going to recommend", bg='black', fg='#d3e1e6',
                       font=("Arial", 14))  # blank
    lc.pack(pady=10)

    e1 = tkinter.Entry(r, font=("Arial", 14))
    e1.pack(pady=15)

    ln= tkinter.Label(r, text="Enter the Name of the course you are going to recommend", bg='black', fg='#d3e1e6',
                       font=("Arial", 14))  # blank
    ln.pack(pady=10)

    e2 = tkinter.Entry(r, font=("Arial", 14))
    e2.pack(pady=15)

    lp = tkinter.Label(r, text="Enter the platform of the course you are going to recommend", bg='black', fg='#d3e1e6',
                       font=("Arial", 14))  # blank
    lp.pack(pady=10)

    e3 = tkinter.Entry(r, font=("Arial", 14))
    e3.pack(pady=15)

    ld = tkinter.Label(r, text="Enter the duration of the course you are going to recommend", bg='black', fg='#d3e1e6',
                       font=("Arial", 14))  # blank
    ld.pack(pady=10)

    e4 = tkinter.Entry(r, font=("Arial", 14))
    e4.pack(pady=15)

    lc = tkinter.Label(r, text="Enter the cost of the course you are going to recommend", bg='black', fg='#d3e1e6',
                       font=("Arial", 14))  # blank
    lc.pack(pady=10)

    e5= tkinter.Entry(r, font=("Arial", 14))
    e5.pack(pady=15)

    def updte():

        global cl
        global ml
        global ad
        global ds
        global gd
        k1=e1.get()
        k2=e2.get()
        k3=e3.get()
        k4=e4.get()
        k5=e5.get()
        print(k1,k2,k3,k4,k5)
        r.destroy()

        k1.lower()
        if(k1=='machine learning'):
            ml['name'].append(k2)
            ml['platform'].append(k3)
            ml['duration'].append(k4)
            ml['price'].append(k5)
        elif(k1=='data science'):
            ds['name'].append(k2)
            ds['platform'].append(k3)
            ds['duration'].append(k4)
            ds['price'].append(k5)
        elif (k1 == 'graphics designing'):
            gd['name'].append(k2)
            gd['platform'].append(k3)
            gd['duration'].append(k4)
            gd['price'].append(k5)
        elif (k1 == 'app devlopment'):
            ad['name'].append(k2)
            ad['platform'].append(k3)
            ad['duration'].append(k4)
            ad['price'].append(k5)
        r1 = tkinter.Toplevel()
        # rt.iconbitmap('cpy.ico')////////////insert icon ico file when done_______________
        r1.title("find a course")
        r1.geometry('400x300+100+50')
        r1.resizable(0, 0)
        r1.config(bg='black')

        lc = tkinter.Label(r1, text="Entered data has been added \nThank you for your Contribution", bg='black',
                           fg='#d3e1e6',
                           font=("Arial", 18))
        lc.pack(pady=10)

        def clsrecom():
            r1.destroy()

        bgh = tkinter.Button(r1, text='OK', bg='black', fg='#d3e1e6', font=("Arial", 16),command=clsrecom)  # go to home
        bgh.pack(pady=5)





    bsav = tkinter.Button(r, text='save', bg='black', fg='#d3e1e6', font=("Arial", 16),command=updte)  # save button
    bsav.pack(pady=25)












################################_________main_window___________________________________##########################
rt=tkinter.Tk()
#rt.iconbitmap('cpy.ico')////////////insert icon ico file when done_______________
rt.title("recocrse")
rt.geometry('600x355+250+100')
rt.resizable(0,0)
rt.config(bg='black')
#_______________lables__________#
l1=tkinter.Label(rt,text="recocrse",bg='black',fg='#d3e1e6',font=("Arial",24))
l1.pack(pady=5)

bf=tkinter.Button(rt,text='    FIND  A  COURSE   ',bg='black',fg='#d3e1e6',font=("Arial",18),command=fndc)#find a course
bf.pack(pady=25)

br=tkinter.Button(rt,text='Recommend a course',bg='black',fg='#d3e1e6',font=("Arial",18),command=recrse)#recommend
br.pack(pady=25)

lb=tkinter.Label(rt,text="",bg='black',fg='black',font=("Arial",8))#blank
lb.pack(pady=20)

lc=tkinter.Label(rt,text="This project is designed and made by team weebois\nfor the technica hackathon.this app recommends a course based on what the user wants to learn ",bg='black',fg='#d3e1e6',font=("Arial",8))
lc.pack(pady=5)
##################################################################################################################



rt.mainloop()
