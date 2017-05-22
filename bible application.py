from tkinter import *
import threading
import os
import re
root=Tk()
class bibleapp(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.master.title('Standard Bible Application')
        self.master.maxsize(width=1000, height=600)
        self.master.minsize(width=1000, height=600)

        self.mainframe()
    def mainframe(self):
        self.frame=Frame()
        self.frame.pack()

        self.frame1=Frame()
        self.frame1.pack()

        self.frame2=Frame()
        self.frame2.pack()

        self.frame6 = Frame()
        self.frame6.pack()

        self.frame3=Frame()
        self.frame3.pack()

        self.frame4=Frame()
        self.frame4.pack()

        self.frame5 = Frame()
        self.frame5.pack()
        self.frameprogram()

    def frameprogram(self):
        self.img=PhotoImage(file='C:/Users/10/Desktop/Bible/Book_48px.png')
        self.blab2=Label(self.frame, image=self.img, width=2000, height=50, bg='sky blue').pack()
        self.lbl=Label(self.frame, text='Standard Bible Application', justify='left', font='arial 10 bold', bg='sky blue', width=1200, height=2).pack(ipady=0, ipadx=4)
        self.btn1=Button(self.frame1, text='Testament?', command=self.changename, fg='red', font='arial 9 bold').pack(side=LEFT)
        self.spin1=Spinbox(self.frame1, value=('Old Testament', 'New Testament'), width=20)
        self.spin1.pack(side=LEFT, padx=8)


        self.lbl3 = Label(self.frame1, text='')
        self.lbl3.pack(side=LEFT)
        self.spin2 = Spinbox(self.frame1, value=(''), fg='dark grey', width=20)
        self.spin2.pack(side=LEFT)
        self.search = Button(self.frame1, text='search', font='arial 8 bold', command=self.searches)
        self.search.pack(side=LEFT)
        self.searchdd1 = Button(self.frame1, text='all?', width=4, height=1, command=self.searchall, font='arial 8 bold', fg='red').pack(side=LEFT)

        self.searchd=Label(self.frame2, text='search Text?', fg='red', font='arial 9 bold').pack(side=LEFT)
        self.searchtt_textvariable=StringVar()
        self.searchtt=Entry(self.frame2, width=20, textvariable=self.searchtt_textvariable).pack(side=LEFT)
        self.img7=PhotoImage(file='C:/Users/10/Desktop/Bible/Search_48px_thumbnail.png')
        self.searchddx=Button(self.frame2, image=self.img7, width=14, height=14, command=self.searchddthread)
        self.searchddx.pack(side=LEFT)

        self.blab = Label(self.frame3, text='Bible', width=60).pack(side=LEFT)
        self.blab = Label(self.frame3, text='Note', width=60).pack(side=LEFT)
        self.text=Text(self.frame4, width=80, height=25, font='arial 9', fg='purple', wrap='word', state=DISABLED)
        self.scrolsl=Scrollbar(self.frame4)
        self.scrolsl.config(command=self.text.yview)
        self.scrolsl.pack(side=LEFT, fill=Y)
        self.text.config(yscrollcommand=self.scrolsl.set)
        self.text.tag_configure('tag-left', justify='left')
        self.text.tag_configure('tag-center', justify='center')
        self.text.pack(side=LEFT, fill=Y)

        self.text1=Text(self.frame4, width=55, height=25, wrap='word', fg='dark grey')
        self.scrolsl1 = Scrollbar(self.frame4)
        self.scrolsl1.config(command=self.text1.yview)
        self.scrolsl1.pack(side=RIGHT, fill=Y)
        self.text1.config(yscrollcommand=self.scrolsl1.set)
        self.text1.pack(side=LEFT, fill=Y)

        self.loading()

    def searchall(self):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.config(state=DISABLED)
        self.loading()

    def loading(self):
        with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
            self.text.config(state=NORMAL)
            self.text.config(fg='purple')
            self.vy='Old and New Testament'
            self.text.insert(END, self.vy+'\n\n', 'tag-center')
            self.text.config(state=DISABLED)
            for lines in file:
                lines = lines.rstrip()
                if re.search('^.+|.+|', lines):
                    self.text.config(state=NORMAL)
                    self.text.insert(END, lines[0:-1] + '\n\n', 'tag-left')
                    self.text.config(state=DISABLED)
        file.close()

    def saving(self):
        self.file='backingfile.txt'
        self.files='C:/Users/10/Desktop/Bible/'+self.file
        if os.path.exists(self.files):
            with open(self.files, 'w') as filing:
                filing.flush()
                pass
        else:
            os.mkdir(self.files)
            with open(self.files, 'w') as filings:
                pass
    def searchddthread(self):
        rk=threading.Thread(target=self.searchdd, args=('Thread-1',))
        rk.start()

    def searchdd(self, name):
        self.searchddx.config(state=DISABLED)
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.config(state=DISABLED)

        self.text.config(state=NORMAL)
        self.text.config(fg='red')
        self.text.insert(END, 'Word Search\n\n', 'tag-center')
        self.text.config(state=DISABLED)

        self.ggx=self.searchtt_textvariable.get()
        self.gg = self.ggx.split()
        self.gg1 = self.gg[0][0:3]
        if len(self.gg)>3:
            if self.gg1[0].islower():
                self.gg1 = self.gg1[0].upper() + self.gg1[1:3].lower()
                self.gg2 = self.gg[1][0:3]
                self.gg3=self.gg[-2][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg2[0].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg2[0].upper() + self.gg2[1:3].lower()
                self.gg3=self.gg[-2][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' +str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg2[0].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg[1][0:3]
                self.gg3=self.gg3[0].upper() + self.gg2[1:3].lower()
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' +str(self.gg1) + '.*' + str(self.gg2)+ '.*' + str(self.gg3) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg4.islower():
                self.gg = self.ggx.split()
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg[1][0:3]
                self.gg4 = self.gg4[0].upper() + self.gg4[1:3].lower()

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg1[-1].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg[1][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()





        if len(self.gg)==3:
            if self.gg1[0].islower():
                self.gg1 = self.gg1[0].upper() + self.gg1[1:3].lower()
                self.gg2 = self.gg[1][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg2[0].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg2[0].upper() + self.gg2[1:3].lower()
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg4.islower():
                self.gg = self.ggx.split()
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg[1][0:3]
                self.gg4 = self.gg4[0].upper() + self.gg4[1:3].lower()

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg1[-1].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg2 = self.gg[1][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search(str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search('.*' + str(self.gg1) + '.*' + str(self.gg2) + '.*' + str(
                                self.gg4), linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()
        elif len(self.gg)==2:
            if self.gg1[0].islower():
                self.gg1 = self.gg1[0].upper() + self.gg1[1:3].lower()
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search('.*' + str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search(str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg4[0].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg4 = self.gg4[0].upper()+self.gg4[1:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search('.*' + str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search(str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

            if self.gg1[-1].islower():
                self.gg1 = self.gg[0][0:3]
                self.gg4 = self.gg[-1][0:3]

                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search('.*' + str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search(str(self.gg1) + '.*' + str(
                                self.gg4) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()

        elif len(self.gg) == 1:
            if self.gg1[0].islower():
                self.gg1 = self.gg1[0].upper() + self.gg1[1:3].lower()
                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search('.*' + str(self.gg1) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search(str(self.gg1) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()
            if self.gg1[-1].islower():
                self.gg1 = self.gg[0][0:3]
                with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                    for linex in file:
                        linex = linex.rstrip()
                        if re.search('.*' + str(self.gg1) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                        elif re.search(str(self.gg1) + '.*', linex):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, linex[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                file.close()
        else:
            pass
        self.searchddx.config(state=NORMAL)


    def changename(self):
        self.yea = self.spin1.get()
        self.lbl3['text']='Book of the '+self.yea
        if self.yea=='Old Testament':
            self.biblist = []
            with open('C:/Users/10/Desktop/Bible/Old Testament.txt', 'r') as file:
                for f in file:
                    fx=f.strip(),
                    self.biblist.append(fx)
                    self.biblist=list(self.biblist)
                self.spin2['value']=self.biblist
        else:
            self.biblist = []
            with open('C:/Users/10/Desktop/Bible/New Testament.txt', 'r') as file:
                for f in file:
                    fx=f.strip(),
                    self.biblist.append(fx)
                    self.biblist=list(self.biblist)
                self.spin2['value']=self.biblist
            file.close()
    def searches(self):
        try:
            with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                self.det1 = self.spin2.get()
                if self.det1[0] != '{':
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.config(state=DISABLED)

                    self.text.config(state=NORMAL)
                    self.text.insert(END, self.spin1.get() + '\n', 'tag-center')
                    self.text.insert(END, 'The Book of ' + self.spin2.get() + '\n\n', 'tag-center')
                    self.text.config(state=DISABLED)
                    self.det = self.det1[0:4]
                    if self.det=='Judg':
                        self.det='Jdg'
                    else:
                        self.det=self.det[0:3]
                    for lines in file:
                        lines = lines.rstrip()
                        if re.search('^' + str(self.det), lines):
                            self.text.config(state=NORMAL)
                            self.text.insert(END, lines[0:-1] + '\n\n', 'tag-left')
                            self.text.config(state=DISABLED)
                    self.text.config(state=NORMAL)
                    self.text.insert(END, '\n\n' + 'The End of ' + self.spin2.get() + '\n', 'tag-center')
                    self.text.config(state=DISABLED)
                    file.close()

                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.config(state=DISABLED)

                    self.text.config(state=NORMAL)
                    self.text.insert(END, self.spin1.get() + '\n', 'tag-center')
                    self.text.insert(END, 'The Book of ' + self.spin2.get() + '\n\n', 'tag-center')
                    self.text.config(state=DISABLED)
                    self.det2 = self.spin2.get()
                    self.det3 = self.det2[0:5]
                    if self.det3 == '{1 Sa':
                        self.det3 = 'Sa1'
                    elif self.det3 == '{2 Sa':
                        self.det3 = 'Sa2'
                    elif self.det3 == '{1 Ki':
                        self.det3 = 'Kg1'
                    elif self.det3 == '{2 Ki':
                        self.det3 = 'Kg2'
                    elif self.det3 == '{1 Ch':
                        self.det3 = 'Ch1'
                    elif self.det3 == '{2 Ch':
                        self.det3 = 'Ch2'
                    elif self.det3 == '{1 Co':
                        self.det3 = 'Co1'
                    elif self.det3 == '{2 Co':
                        self.det3 = 'Co2'
                    elif self.det3 == '{1 Th':
                        self.det3 = 'Th1'
                    elif self.det3 == '{2 Th':
                        self.det3 = 'Th2'
                    elif self.det3 == '{1 Ti':
                        self.det3 = 'Ti1'
                    elif self.det3 == '{1 Th':
                        self.det3 = 'Th1'
                    elif self.det3 == '{1 Pe':
                        self.det3 = 'Pe1'
                    elif self.det3 == '{2 Pe':
                        self.det3 = 'Pe2'
                    elif self.det3 == '{1 Jo':
                        self.det3 = 'Jo1'
                    elif self.det3 == '{2 Jo':
                        self.det3 = 'Jo2'
                    elif self.det3 == '{3 Jo':
                        self.det3 = 'Jo3'
                    else:
                        self.det3 = ''
                    with open('C:/Users/10/Desktop/Bible/kjvdat.txt', 'r') as file:
                        for lines in file:
                            lines = lines.rstrip()
                            if re.search('^' + str(self.det3), lines):
                                self.text.config(state=NORMAL)
                                self.text.insert(END, lines[0:-1] + '\n\n', 'tag-left')
                                self.text.config(state=DISABLED)
                        self.text.config(state=NORMAL)
                        self.text.insert(END, '\n\n' + 'The End of ' + self.spin2.get() + '\n', 'tag-center')
                        self.text.config(state=DISABLED)
                    file.close()
        except IndexError:
            pass



def Main():
    bibleapp(master=root).mainloop()
if __name__=='__main__':
    Main()