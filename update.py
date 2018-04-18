# import modules==================================
from tkinter import *
import sqlite3
import tkinter.messagebox

#update the appointments
conn = sqlite3.connect("database.db")
c = conn.cursor()

class Application(object):
	def __init__(self, master):
		self.master = master
		self.left = Frame(master, width=1200, height=720, bg='darkblue')
		self.left.pack(side=LEFT)
		#heading label
		self.heading = Label(master, text="Update Appointments", fg="steelblue", bg='darkblue', font=("arial 40 bold"))
		self.heading.place(x=150, y=0)

		#search criteria ---> name
		self.name = Label(master, text="Enter Patient's Name", bg='darkblue', font=("arial 18 bold"))
		self.name.place(x=0, y=80)

		#entry for the name
		self.namenet = Entry(master, width=40)
		self.namenet.place(x=280, y=90)

		#search button 
		self.search = Button(master, text="Search", width=12, fg="black", bg="lightgreen", command=self.search_db)
		self.search.place(x=340, y=120)

		#close button 
		self.search = Button(master, text="Exit System", font=('arial 18 bold'), fg="black", bg="lightgreen", command=self.quit)
		self.search.place(x=250, y=560)

	#search function
	def search_db(self):
		self.input = self.namenet.get()
		
		#execute sql
		sql = "SELECT * FROM appointments WHERE name LIKE ?"
		self.res = c.execute(sql, (self.input,))
		for self.row in self.res:
			self.name = self.row[1]
			self.age = self.row[2]
			self.gender = self.row[3]
			self.address = self.row[4]
			self.phone = self.row[5]
			self.doctor = self.row[6]
			self.apptime = self.row[7]
			# if u want to show phone num only = print("phone is " + str(self.phone))

		#create update form
		self.uname = Label(self.master, text="Patient's Name", bg='darkblue', font=('arial 18 bold'))
		self.uname.place(x=0, y=150)

		self.uage = Label(self.master, text="Age", bg='darkblue', font=('arial 18 bold'))
		self.uage.place(x=0, y=190)

		self.ugender = Label(self.master, text="Gender", bg='darkblue', font=('arial 18 bold'))
		self.ugender.place(x=0, y=230)

		self.uaddress = Label(self.master, text="Address", bg='darkblue', font=('arial 18 bold'))
		self.uaddress.place(x=0, y=270)

		self.uphone = Label(self.master, text="Phone Number", bg='darkblue', font=('arial 18 bold'))
		self.uphone.place(x=0, y=310)

		self.udoctor = Label(self.master, text="Doctor", bg='darkblue', font=('arial 18 bold'))
		self.udoctor.place(x=0, y=350)

		self.uapptime = Label(self.master, text="Appointment Time", bg='darkblue', font=('arial 18 bold'))
		self.uapptime.place(x=0, y=390)

		#entries for each label
		self.entry1 = Entry(self.master, width=40)
		self.entry1.place(x=280, y=160)
		self.entry1.insert(END, str(self.name))

		self.entry2 = Entry(self.master, width=40)
		self.entry2.place(x=280, y=200)
		self.entry2.insert(END, str(self.age))

		self.entry3 = Entry(self.master, width=40)
		self.entry3.place(x=280, y=240)
		self.entry3.insert(END, str(self.gender))

		self.entry4 = Entry(self.master, width=40)
		self.entry4.place(x=280, y=280)
		self.entry4.insert(END, str(self.address))

		self.entry5 = Entry(self.master, width=40)
		self.entry5.place(x=280, y=320)
		self.entry5.insert(END, str(self.phone))

		self.entry6 = Entry(self.master, width=40)
		self.entry6.place(x=280, y=360)
		self.entry6.insert(END, str(self.doctor))

		self.entry7 = Entry(self.master, width=40)
		self.entry7.place(x=280, y=400)
		self.entry7.insert(END, str(self.apptime))

		#update button
		self.update = Button(self.master, text="Update", width=20, height=2, fg="black", bg="lightgreen", command=self.update_db)
		self.update.place(x=320, y=440)

		#delete button
		self.delete = Button(self.master, text="Delete", width=20, height=2, fg="black", bg="red", command=self.delete_db)
		self.delete.place(x=150, y=440)

		

	def update_db(self):
		#declaring the variables to update
		self.var1 = self.entry1.get() # update name
		self.var2 = self.entry2.get() # update age
		self.var3 = self.entry3.get() # update gender
		self.var4 = self.entry4.get() # update address
		self.var5 = self.entry5.get() # update phone
		self.var6 = self.entry6.get() # update doctor
		self.var7 = self.entry7.get() # update apptime

		query = "UPDATE appointments SET name=?, age=?, gender=?, address=?, phone=?, doctor=?, apptime=? WHERE name LIKE ?"
		c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.namenet.get(),))
		conn.commit()
		tkinter.messagebox.showinfo("Success", "information for " + str(self.name) + " has been updated")

	def delete_db(self):
		sql2 = "DELETE FROM appointments WHERE name LIKE ?"
		c.execute(sql2, (self.namenet.get(),))
		conn.commit()
		tkinter.messagebox.showinfo("Success", "information for " + str(self.name) + " has been deleted")
		self.entry1.destroy()
		self.entry2.destroy()
		self.entry3.destroy()
		self.entry4.destroy()
		self.entry5.destroy()
		self.entry6.destroy()
		self.entry7.destroy()

	def quit(self):
		global root
		root.destroy()



#create the object
root =  Tk()
b = Application(root)
#resolution of the window
root.geometry("1200x720+0+0")
#rename window
b.master.title("HOSPITAL MANAGEMENT SYSTEM")
#prevent resize feature
root.resizable(False, False)
#end the loop
root.mainloop()
		