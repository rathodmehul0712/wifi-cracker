import tkinter as tk
from threading import Thread
from time import sleep
from tkinter import ttk, messagebox
from GetWifiData import getData
from passwordGenerator import Generate
from WiFiCracker import getHosts, startHack
from Singleton import MyClass

LARGEFONT = ("Verdana", 35)
c = MyClass()
#  pyinstaller --onefile --icon "Files/icone.ico" main.py

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # self.iconbitmap("D:\\python practice\\project wifi\\Python-Graphical-Wifi-Cracker\\wifi.ico")
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.title("Wifi Cracker")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menu_bar = tk.Menu(self)
        menu_file = tk.Menu(menu_bar, tearoff=0)

        def showA():
            self.show_frame(Home)

        def showP1():
            self.show_frame(Page1)

        def showP2():
            self.show_frame(Page2)

        def showP3():
            self.show_frame(Page3)

        menu_file.add_command(label="Home",
                              command=showA)
        menu_file.add_command(label="Most known network passes",
                              command=showP1)
        menu_file.add_command(label="Generate passwords", command=showP2)
        menu_file.add_command(label="Crack Wifi", command=showP3)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Change Page", menu=menu_file)
        self.config(menu=menu_bar)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, Page1, Page2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # Home, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame Home

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Home", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

    # second window frame page1


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Most known network passes", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # code ------------------------------------
        # Create the text widget
        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=2, padx=10, pady=10)
        text_widget = tk.Text(frame1, height=10, width=100)
        scroll_bar = tk.Scrollbar(frame1)

        long_text = """Here will be displayed the result
        """

        text_widget.pack(side="left", )
        scroll_bar.pack(side="right", fill="y")
        # Insert text into the text widget
        text_widget.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text_widget.yview)
        text_widget.insert(tk.END, long_text)

        def Erase():
            text_widget.delete("1.0", "end")

        def GetWifiInfos():
            text_widget.delete("1.0", "end")
            text_widget.insert(tk.END, getData())

        button4 = ttk.Button(self, text="To Display",
                             command=GetWifiInfos)
        button4.grid(row=0, column=3, padx=10, pady=10)
        button5 = ttk.Button(self, text="Erase",
                             command=Erase)
        button5.grid(row=1, column=3, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    selection = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Generates MDP", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        ##code -----------------

        tk.Label(self, text="Password Length").grid(row=1, column=2)
        tk.Label(self, text="maximum passwords").grid(row=2, column=2)
        tk.Label(self, text="type of combinations").grid(row=3, column=2)

        def sel():
            self.selection = str(var.get())

        var = tk.IntVar()
        R1 = tk.Radiobutton(self, text="1) aplhanumeric combination", variable=var, value=1, command=sel)
        R2 = tk.Radiobutton(self, text="2) numeric combination only", variable=var, value=2, command=sel)
        R3 = tk.Radiobutton(self, text="3) single caractor combinations", variable=var, value=3, command=sel)
        R4 = tk.Radiobutton(self, text="4) spacial charactor combinations alone", variable=var, value=4, command=sel)
        R5 = tk.Radiobutton(self, text="5)spacial charactor and number combination alone", variable=var, value=5,
                            command=sel)
        R6 = tk.Radiobutton(self, text="6) alphanumeric combinations and special charactor", variable=var, value=6,
                            command=sel)
        R7 = tk.Radiobutton(self, text="7) special combination", variable=var, value=7, command=sel)
        R1.grid(row=4, column=3)
        R2.grid(row=5, column=3)
        R3.grid(row=6, column=3)
        R4.grid(row=7, column=3)
        R5.grid(row=8, column=3)
        R6.grid(row=9, column=3)
        R7.grid(row=10, column=3)
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e1.grid(row=1, column=3)
        e2.grid(row=2, column=3)
        tk.Label(self, text="Si 7) enter combination").grid(row=11, column=3)
        e3 = tk.Entry(self)
        e3.grid(row=11, column=4)



        def gerenateMDP7():
            Generate(self.selection, e1.get(), e2.get(), e3.get())
            messagebox.showinfo("Password Making", "generated passwords")
        def gerenateMDP1():
            Generate(self.selection, e1.get(), e2.get(), "")
            messagebox.showinfo("Password Making", "generated passwords")


        def gerenateMDP():
            if self.selection == "7":
                thread1 = Thread(target=gerenateMDP7)
                thread1.start()
            else:
                thread1 = Thread(target=gerenateMDP1)
                thread1.start()

        button4 = ttk.Button(self, text="Generate",
                             command=gerenateMDP)
        button4.grid(row=12, column=3, padx=10, pady=10)


class Page3(tk.Frame):
    hosts = []
    res = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Crack wifi", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # code 
        # Create the text widget
        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=2, padx=10, pady=10)
        text_widget = tk.Text(frame1, height=10, width=100)
        scroll_bar = tk.Scrollbar(frame1)

        long_text = """Here will be displayed the results
                """

        text_widget.pack(side="left", )
        scroll_bar.pack(side="right", fill="y")
        # Insert text into the text widget
        text_widget.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=text_widget.yview)
        text_widget.insert(tk.END, long_text)

        def attack():
            startHack(e3.get(), self.hosts)
            messagebox.showinfo("Testing", "Hacking done !")

        def Attack():
            text_widget.insert(tk.END, "Attack in progress...\n")
            thread1 = Thread(target=attack)
            thread1.start()
            thread2 = Thread(target=display)
            thread2.start()

        def display():
            while not c.getIsOver():
                res2 = c.getResults()
                text_widget.insert(tk.END, res2)
                c.setResults("")
                sleep(2)
            if c.getIsOver():
                res2 = c.getResults()
                text_widget.insert(tk.END, res2)
                c.setResults("")

        def Erase():
            text_widget.delete("1.0", "end")

        def getInfos():
            res = getHosts()
            self.hosts = res[0]
            self.res = res[1]
            text_widget.insert(tk.END, self.res)
            messagebox.showinfo("Scanning", "Finished info gathering !")

        def GetWifiInfos():
            text_widget.delete("1.0", "end")
            thread3 = Thread(target=getInfos)
            thread3.start()

        button4 = ttk.Button(self, text="See networks",
                             command=GetWifiInfos)
        button4.grid(row=0, column=3, padx=10, pady=10)
        button5 = ttk.Button(self, text="Erase",
                             command=Erase)
        button5.grid(row=1, column=3, padx=10, pady=10)
        tk.Label(self, text="Network to attack").grid(row=2, column=3)
        e3 = tk.Entry(self)
        e3.grid(row=2, column=4)
        button6 = ttk.Button(self, text="Attack",
                             command=Attack)
        button6.grid(row=3, column=4, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
