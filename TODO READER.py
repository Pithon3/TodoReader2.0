#-------------------------------------------#
# TODO Reader 2.0 - Aidan S (Idea by Erik D)#
#-------------------------------------------#
# Version 2.0 Details:                      #
#     New GUI look                          #
#     Multiple Lists                        #
#     Structured classes                    # 
#-------------------------------------------#

#Import Declarations
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        self.master = master

        file = open("ToDoMainfile.txt", "a")
        file.close()

        self.startlayout()

    def startlayout(self):
        self.setup()
        
        tempfile = open("ToDoMainfile.txt", "r")
        self.filenames = tempfile.readlines()
        tempfile.close()

        index = 0
        for name in self.filenames:
            self.filenames[index] = name.replace("\n", "")
            index += 1
        
        self.files = []
        for filename in self.filenames:
            file = open(filename, "a+")
            self.files.append(file)

        WelcomeL = Label(self, text = "                             Welcome to the To-Do Reader 2.0!                             ")
        WelcomeL.grid(columnspan = 8)

        nwrow = 2
        
        if self.files:
            YesFileLabel = Label(self, text = "Your todo lists:")
            YesFileLabel.grid()
            
            roll = 0
            for filename in self.filenames:
                self.NewButton(filename, self.files[roll])
                nwrow += 1
                roll += 1
                
        else:
            NoFileL = Label(self, text = "You curently have no todo lists.")
            NoFileL.grid(columnspan = 2)

        Spacer1 = Label(self, text = "")
        Spacer1.grid(row = nwrow)
        AddFileL = Label(self, text = "Add a file:")
        AddFileL.grid(row = nwrow, sticky = W)

        self.AddFile_ent = Entry(self)
        self.AddFile_ent.grid(row = nwrow, column = 1)
        self.AddFile_ent.insert(0, "")

        AddFileB = Button(self, text = "  OK  ", command = self.addfile)
        AddFileB.grid(row = nwrow, column = 2, sticky = W)

    def setup(self):
        super(Application, self).__init__(self.master)
        self.grid()

    def addfile(self):
        filename = self.AddFile_ent.get() + ".txt"
        file = open(filename, "a+")
        self.files.append(file)
        file.close()
        self.filenames.append(filename)
        self.RefreshMainfile()
        self.grid_forget()
        self.startlayout()

    def RefreshMainfile(self):
        clearfile = open("ToDoMainfile.txt", "w")
        clearfile.close()

        file = open("ToDoMainfile.txt", "a")
        for filename in self.filenames:
            file.write(filename)
            file.write("\n")

    def NewButton(self, ButtonName, ButtonFile):
        Button(self, text = ButtonName.replace(".txt", " >"), command = lambda: self.list(ButtonFile, ButtonName)).grid(sticky = E)

    def list(self, File, Name):
        self.grid_forget()
        self.setup()
        Button(self, text = "< Back", command = self.reset).grid(column = 0, row = 1)
        Label(self, text = Name.replace(".txt", "")).grid(column = 0, row = 0, columnspan = 6)
        Label(self, text = "\t\t\t\t\t\t\t\t\t\t").grid(row = 2, columnspan = 6)
        Fileitems = File.readlines()
        
        Line = 3
        for item in Fileitems:
            Button(self, text = item + " >")
            Line += 1

        AddItemL = Label(self, text = "Add an item:")
        AddItemL.grid(row = Line, sticky = W)

        self.AddItem_ent = Entry(self)
        self.AddItem_ent.grid(row = Line, column = 1)
        self.AddItem_ent.insert(0, "")

        AddItemB = Button(self, text = "  OK  ", command = lambda: self.additem(File, Name))
        AddItemB.grid(row = Line, column = 2, sticky = W)

    def additem(self, File, Name):
        File.write(self.AddItem_ent.get())
        
        
    def reset(self):
        self.grid_forget()
        self.setup()
        for line in self.files:
            line.close()
        
        self.startlayout()
       

root = Tk()
root.title("To-Do Reader 2.0")
root.geometry("400x300")
app = Application(root)
root.mainloop()
