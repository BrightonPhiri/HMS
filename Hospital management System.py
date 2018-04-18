# import modules==================================
from tkinter import *
import sqlite3
import tkinter.messagebox
import os

# connect to the database
conn = sqlite3.connect('database.db')

# cursor to move around e database
c = conn.cursor()

#empty list to later append id's from database
ids = []

# create tkinter window
class Application:
	def __init__(self, master):
		self.master = master

		# create the frames
		self.left = Frame(master, width=800, height=720, bg='darkblue')
		self.left.pack(side=LEFT)

		self.right = Frame(master, width=400, height=720, bg='steelblue')
		self.right.pack(side=RIGHT)

		#labels for the window
		self.heading = Label(self.left, text="KOMBORE HOSPITAL SYSTEM", font=('arial 40 bold'), fg="white", bg="darkblue")
		self.heading.place(x=0, y=0)

		#patient details==============================================================================
		self.name = Label(self.left, text="Name of Patient", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.name.place(x=0, y=100)

		self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.age.place(x=0, y=140)

		self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.gender.place(x=0, y=180)

		self.address = Label(self.left, text="Address", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.address.place(x=0, y=220)

		self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.phone.place(x=0, y=260)

		self.doctor = Label(self.left, text="Doctor", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.doctor.place(x=0, y=300)

		self.apptime = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg="black", bg="darkblue")
		self.apptime.place(x=0, y=340)

		#entries for paient labels=====================================================================
		self.name_ent = Entry(self.left, width=40)
		self.name_ent.place(x=250, y=110)

		self.age_ent = Entry(self.left, width=40)
		self.age_ent.place(x=250, y=150)

		self.gender_ent = Entry(self.left, width=40)
		self.gender_ent.place(x=250, y=190)

		self.address_ent = Entry(self.left, width=40)
		self.address_ent.place(x=250, y=230)

		self.phone_ent = Entry(self.left, width=40)
		self.phone_ent.place(x=250, y=270)

		self.doctor_ent = Entry(self.left, width=40)
		self.doctor_ent.place(x=250, y=310)

		self.apptime_ent = Entry(self.left, width=40)
		self.apptime_ent.place(x=250, y=350)

		#button for commanding 
		self.submit = Button(self.left, text="Add Patient", font=('arial 18 bold'), fg="black", bg="lightgreen", command=self.add_appointment)
		self.submit.place(x=260, y=390)

		#search button 
		self.search = Button(master, text="View Patients", font=('arial 18 bold'), fg="black", bg="lightgreen", command=self.update11)
		self.search.place(x=280, y=480)

		#close button 
		self.search = Button(master, text="Exit System", font=('arial 18 bold'), fg="black", bg="lightgreen", command=self.quit)
		self.search.place(x=290, y=560)


		#get number of appointments to show on the log
		sql2 = "SELECT ID FROM appointments" 
		self.result = c.execute(sql2)
		for self.row in self.result:
			self.id = self.row[0]
			ids.append(self.id)

		#ordering the ids
		self.new = sorted(ids)
		self.final_id = self.new[len(ids) -1]

		#display patient details on the right frame
		self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
		self.logs.place(x=15, y=0)
		self.box = Text(self.right, width=45, height=40)
		self.box.place(x=20, y=50)
		self.box.insert(END, 'Total Patients: ' + str(self.final_id) + "\n")



	def update11(self):
		import update

	def quit(self):
		global root
		root.quit()

		#function to call the submit button
	def add_appointment(self):
		#get user input
		self.val1 = self.name_ent.get()
		self.val2 = self.age_ent.get()
		self.val3 = self.gender_ent.get()
		self.val4 = self.address_ent.get()
		self.val5 = self.phone_ent.get()
		self.val6 = self.doctor_ent.get()
		self.val7 = self.apptime_ent.get()

		#check if user input is empty
		if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 == '':
			tkinter.messagebox.showinfo("Warning", "Please fill in all the details")
		else:
			#adding to the database
			sql = "INSERT INTO 'appointments' (name, age, gender, address, phone, doctor, apptime) VALUES(?, ?, ?, ?, ?, ?, ?)"
			c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
			conn.commit()
			tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")

			self.box.insert(END, "Appointment Fixed for " + str(self.val1) + " at " + str(self.val7))


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