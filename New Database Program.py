'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Howard C Davis
Final Tk
'''


from tkinter import *
from tkinter import ttk

class NewDatabase:
    def __init__(self, master):
        #Values
        self.User = StringVar()
        self.Pass = StringVar()
        self.Gen = StringVar()
        self.type = StringVar()
        self.job = StringVar()
        #Labels
        self.labelError = Label()
        self.labelError.grid(row=6, column=2)

        self.usernamelabel = Label(text = 'Username')  #The text prompting the username entry
        self.usernamelabel.grid(row = 0, column = 0)

        self.passwordlabel = Label(text='Password')  # The text prompting the password
        self.passwordlabel.grid(row=1, column = 0)
        #Entery
        self.username = Entry(textvariable=self.User, width=20)  # The username box
        self.username.grid(row=0, column=1)

        self.password = Entry(textvariable = self.Pass, width = 20, show='*')
        self.password.grid(row = 1, column = 1)
        #RadioButton
        self.genderM = Radiobutton(text='Male', variable=self.Gen, value = 0)
        self.genderM.grid(row=2, column=0, sticky = W)

        self.genderF = Radiobutton(text='Female', variable=self.Gen, value = 1)
        self.genderF.grid(row=2, column=1)
        #CheckButton
        self.admin = Checkbutton(text='Admin', onvalue = 'Admin', offvalue = 'No', variable=self.type)
        self.admin.grid(row=0, column=2)

        self.admin = Checkbutton(text='User', onvalue = 'User', offvalue = 'No', variable=self.type)
        self.admin.grid(row=1, column=2)

        self.admin = Checkbutton(text='Guest', onvalue = 'Guest', offvalue = 'No', variable=self.type)
        self.admin.grid(row=2, column=2)
        #Combo box
        self.combojob = ttk.Combobox(state = 'readonly', textvariable = self.job, values = ['IT', 'HR', 'Sales', 'Maintenance', 'Other'])
        self.combojob.bind("<<ComboboxSelected>>")
        self.combojob.grid(row = 3, column = 2)
        #Submit and clear buttons
        self.submitB = Button(text='Submit', command=self.check)
        self.submitB.grid(row=5, column=0)

        self.submitC = Button(text='Clear', command=self.clear)
        self.submitC.grid(row=5, column=1)

        self.clear()

    def check(self):
        if self.User.get() == '' or self.Pass.get() == 0 or self.type.get() == 'No' or self.combojob.get() == '' or self.Gen.get() == '-1':
            self.labelError.config(text = 'Error')
        else:
            self.labelError.config(text = '')
            self.submit()

    def submit(self):
        gen = ''

        if self.Gen.get() == '0':
            gen = 'Male'
        elif self.Gen.get() == '1':
            gen = 'Female'

        full = (self.User.get(), self.Pass.get(), gen, self.type.get(), self.job.get())
        full2 = str(full).replace('(', '').replace("'",'').replace(')','')

        Open = open('Database', 'a')
        Open.write(str(full2)+'\n')
        Open.close()

        self.clear()

        self.labelError.config(text='User Created')

    def clear(self):
        self.User.set('')
        self.Pass.set('')
        self.type.set('No')
        self.Gen.set(-1)
        self.job.set('')
        self.labelError.config(text = '')


root = Tk()
root.geometry('350x160')

root.title('Credit Applications')

app = NewDatabase(root)

root.mainloop()
root.destroy()