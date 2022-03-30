import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import requests

class login(object):
    def __init__(self, root):
        self.root = root
        self.root.title("login page")
        self.root.geometry("1199x600+100+50")
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=350, y=150, height=340, width=500)
        title = Label(Frame_login, text="login here", font=("impact", 35, "bold"), fg="black", bg="white").place(x=90,
                                                                                                                 y=30)
        unamelabel = tk.Label(Frame_login, text="enter your username:", font=("Goudy old style", 14, "bold"), fg="gray",
                              bg="white").place(x=90, y=140)
        upasswordlabel = tk.Label(Frame_login, text="password:", font=("Goudy old style", 14, "bold"), fg="gray",
                              bg="white").place(x=90, y=210)
        unnametext = tk.StringVar()
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray", textvariable=unnametext)
        self.txt_user.place(x=90, y=170, width=350, height=35)
        self.txt_usr = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_usr.place(x=90, y=240, width=350, height=35)
        btn = tk.Button(Frame_login, text="login", fg="black", bd=0, font=("times new roman", 18),
                        command=lambda: [retrieve_input()])
        btn.place(x=150, y=280)

        # getting input from the user

        def retrieve_input():
            inputvalue = unnametext.get()
            if (inputvalue == ("recruiter@screel.in")):
                root.destroy()
                root1 = Tk()
                obj = Recruiter(root1)
                root1.mainloop()
            elif (inputvalue == ("candidate@screel.in")):
                root.destroy()
                root1 = Tk()
                obj = candiate(root1)

                root1.mainloop()
            else:
                tkinter.messagebox.showinfo("error", "Invalid user name ")
                login(root)

        class candiate(object):
            def __init__(self, root1):
                self.root1 = root1
                self.root1.title("candiate")
                self.root1.geometry("1199x600+100+50")
                # frame creation
                Frame_login = Frame(self.root1, bg="white")
                Frame_login.place(x=230, y=80, height=500, width=800)
                # connecting database creating table view
                columns = ('job_id', 'job_name', 'location', 'description', 'skills')
                table_list = ttk.Treeview(Frame_login, columns=columns, show='headings')
                table_list.column("job_id", anchor=CENTER, width=150)
                table_list.column("job_name", anchor=CENTER, width=150)
                table_list.column("location", anchor=CENTER, width=150)
                table_list.column("description", anchor=CENTER, width=150)
                table_list.column("skills", anchor=CENTER, width=150)
                table_list.heading("job_id", text="job ID", anchor=CENTER)
                table_list.heading("job_name", text="job name", anchor=CENTER)
                table_list.heading("location", text="location", anchor=CENTER)
                table_list.heading("description", text="description", anchor=CENTER)
                table_list.heading("skills", text="skills", anchor=CENTER)
                req = requests.get("http://127.0.0.1:8000/select/")
                records = req.json()
                for j in range(0, len(records)):
                    list = []
                    val = records[j]
                    value = val.values()
                    list.append(value)
                    for i, (job_id, job_name, location, description, skills) in enumerate(list):
                        table_list.insert("", 'end', values=(job_id, job_name, location, description, skills))
                table_list.pack(pady=20)

                btn = tk.Button(Frame_login, text="Apply", fg="black", bd=0, font=("times new roman", 18),
                                command=lambda: [add_frame()])
                btn.place(x=300, y=280)

                # adding application frame
                def add_frame():
                    Frame_login1 = Frame(self.root1, bg="white")
                    Frame_login1.place(x=230, y=50, height=500, width=800)
                    # firstname
                    firstnamelabel = tk.Label(Frame_login1, text="first name:*", font=("times new roman", 13, "bold"),
                                              fg="black",
                                              bg="white").place(x=50, y=80)
                    firstnametext = tk.StringVar()
                    self.firstname = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray",
                                           textvariable=firstnametext)
                    self.firstname.place(x=50, y=120, width=250, height=35)
                    # last name
                    lastnamelabel = tk.Label(Frame_login1, text="last name:*", font=("times new roman", 13, "bold"),
                                             fg="black",
                                             bg="white").place(x=50, y=170)
                    lastnametext = tk.StringVar()
                    self.lastname = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray",
                                          textvariable=lastnametext)
                    self.lastname.place(x=50, y=210, width=250, height=35)
                    # jobid
                    jobidlabel = tk.Label(Frame_login1, text="job id:*", font=("times new roman", 13, "bold"),
                                          fg="black",
                                          bg="white").place(x=50, y=260)
                    jobidtext = tk.StringVar()
                    self.jobid = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray",
                                       textvariable=jobidtext)
                    self.jobid.place(x=50, y=300, width=250, height=35)
                    # email id
                    itlabel = tk.Label(Frame_login1, text="IT skills:*", font=("times new roman", 13, "bold"),
                                       fg="black",
                                       bg="white").place(x=400, y=80)
                    ittext = tk.StringVar()
                    self.it = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray", textvariable=ittext)
                    self.it.place(x=400, y=120, width=250, height=35)
                    # it skills
                    quallabel = tk.Label(Frame_login1, text="Qualification:*", font=("times new roman", 13, "bold"),
                                         fg="black",
                                         bg="white").place(x=400, y=170)
                    qualtext = tk.StringVar()
                    self.qual = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray", textvariable=qualtext)
                    self.qual.place(x=400, y=210, width=250, height=35)
                    # year of experience
                    yearlabel = tk.Label(Frame_login1, text="year of experience :*",
                                         font=("times new roman", 13, "bold"),
                                         fg="black",
                                         bg="white").place(x=400, y=260)
                    yeartext = tk.StringVar()
                    self.year = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray", textvariable=yeartext)
                    self.year.place(x=400, y=300, width=250, height=35)
                    # jobname
                    emaillabel = tk.Label(Frame_login1, text="Email Id:*", font=("times new roman", 13, "bold"),
                                          fg="black",
                                          bg="white").place(x=50, y=360)
                    emailtext = tk.StringVar()
                    self.email = Entry(Frame_login1, font=("times new roman", 12), bg="lightgray",
                                       textvariable=emailtext)
                    self.email.place(x=50, y=390, width=250, height=35)

                    # submit button
                    btn = tk.Button(Frame_login1, text="Submit", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [insert_value(), removethis()])
                    btn.place(x=420, y=450)
                    btn = tk.Button(Frame_login1, text="Back", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [candiate(root1)])
                    btn.place(x=220, y=450)

                    def insert_value():

                        firstna = firstnametext.get()
                        lastna = lastnametext.get()
                        jobi = jobidtext.get()
                        email = emailtext.get()
                        it = ittext.get()
                        qual = qualtext.get()
                        yeart = yeartext.get()
                        if firstna != "" and lastna != "" and jobi != "" and email != "" and it != "" and qual != "" and yeart != "":
                            reques = requests.post(
                                "http://127.0.0.1:8000/insert applicant records?job_id=" + jobi + "&first_name=" + firstna + "&last_name=" + lastna + "&email_id=" + email + "&it_skills=" + it + "&qualification=" + qual + "&yearofexp=" + yeart)
                            result = reques.json()

                            tkinter.messagebox.showinfo("message", result)
                            add_frame()
                        else:
                            tkinter.messagebox.showinfo("message", "Mandatory field missing... ")
                            add_frame()

                    def removethis():
                        Frame_login1.destroy()

        class Recruiter(object):
            def __init__(self, root1):
                self.root1 = root1
                self.root1.title("recruiter")
                self.root1.geometry("1199x600+100+50")
                # creating frame
                Frame_login = Frame(self.root1, bg="white")
                Frame_login.place(x=230, y=80, height=500, width=800)
                create_btn = tk.Button(Frame_login, text="Insert Record", font=("times new roman", 18), width=20,
                                       command=lambda: insert_table())
                create_btn.place(x=80, y=100)
                upset_btn = Button(Frame_login, text="Update Record", font=("times new roman", 18), width=20,
                                   command=lambda: update_table())
                upset_btn.place(x=80, y=200)
                delete_btn = Button(Frame_login, text="Delete Records", font=("times new roman", 18), width=20,
                                    command=lambda: delete())
                delete_btn.place(x=400, y=100)
                list_btn = Button(Frame_login, text=" Job Table List", font=("times new roman", 18), width=20,
                                  command=lambda: job_list_table())
                list_btn.place(x=400, y=200)
                applicant_list_btn = Button(Frame_login, text=" Applicant Table list", font=("times new roman", 18),
                                            width=20,
                                            command=lambda: applicant_list())
                applicant_list_btn.place(x=230, y=310)

                def insert_table():
                    upset_frame = Frame(self.root1, bg="white")
                    upset_frame.place(x=230, y=80, height=500, width=800)
                    # job id
                    job_name_label1 = tk.Label(upset_frame, text="job name:", font=("times new roman", 13, "bold"),
                                               fg="black",
                                               bg="white").place(x=50, y=80)
                    job_name_text = tk.StringVar()
                    self.txt_user1 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_name_text)
                    self.txt_user1.place(x=50, y=120, width=250, height=35)
                    # job name
                    location_label1 = tk.Label(upset_frame, text="location:", font=("times new roman", 13, "bold"),
                                               fg="black",
                                               bg="white").place(x=50, y=170)
                    location_text = tk.StringVar()
                    self.txt_user2 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=location_text)
                    self.txt_user2.place(x=50, y=210, width=250, height=35)

                    # description
                    job_desc_label1 = tk.Label(upset_frame, text="description:", font=("times new roman", 13, "bold"),
                                               fg="black",
                                               bg="white").place(x=400, y=80)
                    job_desc_text = tk.StringVar()
                    self.txt_user4 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_desc_text)
                    self.txt_user4.place(x=400, y=120, width=250, height=35)
                    # skills
                    job_skills_label1 = tk.Label(upset_frame, text="skills:", font=("times new roman", 13, "bold"),
                                                 fg="black",
                                                 bg="white").place(x=400, y=170)
                    job_skill_text = tk.StringVar()
                    self.txt_user5 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_skill_text)
                    self.txt_user5.place(x=400, y=210, width=250, height=35)
                    # submit button
                    btn = tk.Button(upset_frame, text="  Submit ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [inserting()])
                    btn.place(x=440, y=380)

                    def inserting():

                        job_name = job_name_text.get()
                        location = location_text.get()
                        description = job_desc_text.get()
                        skills = job_skill_text.get()
                        if job_name != "" and location != "" and description != "" and skills != "":
                            req3 = requests.post(
                                "http://127.0.0.1:8000/insert?job_name=" + job_name + "&location=" + location + "&description=" + description + "&skills=" + skills)
                            print(req3.status_code)
                            res = req3.json()
                            tkinter.messagebox.showinfo("message", res)
                            insert_table()
                        else:
                            tkinter.messagebox.showinfo("message", "Mandratory field missing....")
                            insert_table()

                    # back button
                    def removethis():
                        root1.destroy()

                    btn2 = tk.Button(upset_frame, text="  Back   ", fg="black", bd=0, font=("times new roman", 18),
                                     command=lambda: [back_frame()])
                    btn2.place(x=220, y=380)

                    def back_frame():
                        Recruiter(root1)

                def update_table():
                    upset_frame = Frame(self.root1, bg="white")
                    upset_frame.place(x=230, y=80, height=500, width=800)
                    # job id
                    job_id_label1 = tk.Label(upset_frame, text="job id:", font=("times new roman", 13, "bold"),
                                             fg="black",
                                             bg="white").place(x=50, y=80)
                    job_id_text = tk.StringVar()
                    self.txt_user1 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_id_text)
                    self.txt_user1.place(x=50, y=120, width=250, height=35)
                    # job name
                    job_name_label1 = tk.Label(upset_frame, text="job name:", font=("times new roman", 13, "bold"),
                                               fg="black",
                                               bg="white").place(x=50, y=170)
                    job_name_text = tk.StringVar()
                    self.txt_user2 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_name_text)
                    self.txt_user2.place(x=50, y=210, width=250, height=35)
                    # location
                    job_location_label1 = tk.Label(upset_frame, text="location:", font=("times new roman", 13, "bold"),
                                                   fg="black",
                                                   bg="white").place(x=50, y=260)
                    job_location_text = tk.StringVar()
                    self.txt_user3 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_location_text)
                    self.txt_user3.place(x=50, y=300, width=250, height=35)
                    # description
                    job_desc_label1 = tk.Label(upset_frame, text="description:", font=("times new roman", 13, "bold"),
                                               fg="black",
                                               bg="white").place(x=400, y=80)
                    job_desc_text = tk.StringVar()
                    self.txt_user4 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_desc_text)
                    self.txt_user4.place(x=400, y=120, width=250, height=35)
                    # skills
                    job_skills_label1 = tk.Label(upset_frame, text="skills:", font=("times new roman", 13, "bold"),
                                                 fg="black",
                                                 bg="white").place(x=400, y=170)
                    job_skill_text = tk.StringVar()
                    self.txt_user5 = Entry(upset_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=job_skill_text)
                    self.txt_user5.place(x=400, y=210, width=250, height=35)
                    # submit button
                    btn = tk.Button(upset_frame, text="  Submit ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [updating()])
                    btn.place(x=440, y=380)

                    def updating():
                        job_id = job_id_text.get()
                        job_name = job_name_text.get()
                        location = job_location_text.get()
                        description = job_desc_text.get()
                        skills = job_skill_text.get()
                        req3 = requests.put(
                            "http://127.0.0.1:8000/update?job_id=" + job_id + "&job_name=" + job_name + "&location=" + location + "&description=" + description + "&skills=" + skills)
                        print(req3.status_code)
                        res = req3.json()
                        tkinter.messagebox.showinfo("message", res)
                        update_table()

                    # back button
                    def removethis():
                        root1.destroy()

                    btn2 = tk.Button(upset_frame, text="  Back   ", fg="black", bd=0, font=("times new roman", 18),
                                     command=lambda: [back_frame()])
                    btn2.place(x=220, y=380)

                    def back_frame():
                        Recruiter(root1)

                def delete():
                    delete_frame = Frame(self.root1, bg="white")
                    delete_frame.place(x=230, y=80, height=500, width=700)
                    job_id_label1 = tk.Label(delete_frame, text="enter job id for delete record:",
                                             font=("times new roman", 13, "bold"), fg="black",
                                             bg="white").place(x=250, y=180)
                    delete_text = tk.StringVar()
                    self.txt_user1 = Entry(delete_frame, font=("times new roman", 12), bg="lightgray",
                                           textvariable=delete_text)
                    self.txt_user1.place(x=250, y=240, width=250, height=35)
                    btn = tk.Button(delete_frame, text="  Submit  ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [deleting()])
                    btn.place(x=410, y=380)
                    btn = tk.Button(delete_frame, text="  Back  ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [back_button()])
                    btn.place(x=250, y=380)

                    def back_button():
                        Recruiter(root1)

                    def deleting():
                        deletevalue = delete_text.get()

                        try:
                            req2 = requests.delete("http://127.0.0.1:8000/delete?job_id_var=" + deletevalue)
                            print(req2.status_code)
                            print(req2.json())
                            res = req2.text
                            tkinter.messagebox.showinfo("mesg", res)
                            delete()
                        except Exception as e:
                            print(e)

                    # closing frame
                    def removethis(self):
                        root1.destroy()

                        # listing job_table

                def job_list_table():
                    list_frame = Frame(self.root1, bg="white")
                    list_frame.place(x=230, y=80, height=500, width=800)
                    btn = tk.Button(list_frame, text="  Back  ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [back_button()])
                    btn.place(x=280, y=380)

                    def back_button():
                        Recruiter(root1)

                    columns = ('job_id', 'job_name', 'location', 'description', 'skills')
                    table_list1 = ttk.Treeview(list_frame, columns=columns, show='headings')
                    table_list1.column("job_id", anchor=CENTER, width=120)
                    table_list1.column("job_name", anchor=CENTER, width=150)
                    table_list1.column("location", anchor=CENTER, width=150)
                    table_list1.column("description", anchor=CENTER, width=150)
                    table_list1.column("skills", anchor=CENTER, width=150)
                    table_list1.heading("job_id", text="job ID", anchor=CENTER)
                    table_list1.heading("job_name", text="job name", anchor=CENTER)
                    table_list1.heading("location", text="location", anchor=CENTER)
                    table_list1.heading("description", text="description", anchor=CENTER)
                    table_list1.heading("skills", text="skills", anchor=CENTER)
                    table_list1.pack(pady=10)
                    req = requests.get("http://127.0.0.1:8000/select/")
                    records = req.json()
                    print(records)
                    for j in range(0, len(records)):
                        list = []
                        val = records[j]
                        value = val.values()
                        list.append(value)
                        for i, (job_id, job_name, location, description, skills) in enumerate(list):
                            table_list1.insert("", 'end', values=(job_id, job_name, location, description, skills))

                    table_list1.pack(pady=20)

                def applicant_list():
                    applicant_login = Frame(self.root1, bg="white")
                    applicant_login.place(x=230, y=80, height=500, width=800)
                    btn = tk.Button(applicant_login, text="  Back  ", fg="black", bd=0, font=("times new roman", 18),
                                    command=lambda: [back_button()])
                    btn.place(x=250, y=380)

                    def back_button():
                        Recruiter(root1)

                    columns = (
                        'job_id', 'first_name', 'last_name', 'email_id', 'it_skills', 'qualification', 'yearofexp')
                    table_list = ttk.Treeview(applicant_login, columns=columns, show='headings')
                    table_list.column("job_id", anchor=CENTER, width=100)
                    table_list.column("first_name", anchor=CENTER, width=100)
                    table_list.column("last_name", anchor=CENTER, width=100)
                    table_list.column("email_id", anchor=CENTER, width=100)
                    table_list.column("it_skills", anchor=CENTER, width=100)
                    table_list.column("qualification", anchor=CENTER, width=100)
                    table_list.column("yearofexp", anchor=CENTER, width=100)
                    table_list.heading("job_id", text="job id", anchor=CENTER)
                    table_list.heading("first_name", text="first_name", anchor=CENTER)
                    table_list.heading("last_name", text="last name", anchor=CENTER)
                    table_list.heading("email_id", text="email id", anchor=CENTER)
                    table_list.heading("it_skills", text="It skills", anchor=CENTER)
                    table_list.heading("qualification", text="Qualification", anchor=CENTER)
                    table_list.heading("yearofexp", text="year of exp", anchor=CENTER)
                    table_list.pack(pady=10)
                    req = requests.get("http://127.0.0.1:8000/select applicant records")
                    records = req.json()
                    for j in range(0, len(records)):
                        list = []
                        val = records[j]
                        value = val.values()
                        list.append(value)
                        for i, (job_id, first_name, last_name, job_name, email_id, it_skills, yearofexp) in enumerate(
                                list):
                            table_list.insert("", 'end', values=(
                                job_id, first_name, last_name, job_name, email_id, it_skills, yearofexp))

                    table_list.pack(pady=20)


root = Tk()
ob = login(root)
root.mainloop()
