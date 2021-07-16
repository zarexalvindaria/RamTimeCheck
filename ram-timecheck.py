from tkinter import *
import tkinter as tk
import time
from datetime import datetime
import os
import csv
from csv import writer


def register():  # User Registration Window module
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Ram Time Check Register")
    register_screen.geometry("300x280")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="", font="Helvetica 11").pack()
    Label(register_screen, text="Please enter your details below", font="Helvetica 11").pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username * ", font="Helvetica 11")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Password * ", font="Helvetica 11")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='•')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, font="Helvetica 11", command=register_user).pack()


def login():  # User login module
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Ram Time Check Login")
    login_screen.geometry("300x280")
    Label(login_screen, text="").pack()
    login_instructions = '''Please enter your
details below to login'''

    Label(login_screen, padx=10, text=login_instructions, font="Helvetica 11").pack(side="top")
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    username_login_entry = Entry(login_screen, textvariable=username_verify)

    Label(login_screen, text="Username * ", font="Helvetica 11").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font="Helvetica 11").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='•')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, font="Helvetica 11", command=login_verify).pack()


def register_user():  # User Registration Setup module
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    reg_message = '''Registration successful!
    You can now log in.'''
    Label(register_screen, padx=15, text=reg_message, fg="green", font=("Helvetica", 11)).pack()


def append_list_as_row(file_name, list_of_elem):  # module which allows appending the logs to file
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, quoting=csv.QUOTE_ALL)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def login_verify():  # Verifying if user exists
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:  # confirms if password matches
            delete_user_not_found_screen()  # closes the login screen
            login_sucess()  # confirms login success

        else:
            password_not_recognised()
    else:
        user_not_found()


def login_sucess():  # creates the login success screen and serves as login Success Window module
    global login_success_screen
    global save_log_in

    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Ram Time Check")
    login_success_screen.geometry("300x590")
    Label(login_success_screen, text="").pack()
    login_message = 'Welcome, ' + username1 + '!'  # Greetings
    Label(login_success_screen, text=login_message, font="Helvetica 11").pack()
    Label(login_success_screen, text="").pack()
    save_log_in = Button(login_success_screen, text="Time in", width=7, font="Helvetica 11", command=save_login)
    save_log_in.pack()  # Time in button
    Button(login_success_screen, text="Time out", width=7, font="Helvetica 11", command=logout).pack()  # Timeout button
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Show your time ins", width=15, font="Helvetica 11", command=print_log_in).pack()
    Button(login_success_screen, text="Show your time outs", width=15,
           font="Helvetica 11", command=print_log_out).pack()
    Label(login_success_screen, text="").pack()
    open_clock()


def save_login():  # appends the login to the csv file
    global user_timein

    user_timein = datetime.now()
    time_in = user_timein.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    userlogin = username1 + "_timein.csv"  # creates the csv file containing logs
    log_ins = []  # creates the list of log ins
    log_ins.append(time_in)  # appends the time in to the list
    append_list_as_row(userlogin, log_ins)  # appends the log ins to the file
    user_timein = ''  # sets time in to null
    Label(login_success_screen, text="Time in saved!", font="Helvetica 12").pack()
    save_log_in["state"] = tk.DISABLED  # disables the login button


def logout():  # outputs if the user is not registered
    global time_out
    global userlogouts
    user_timeout = datetime.now()
    time_out = user_timeout.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    userlogouts = username1 + "_timeout.csv"
    log_outs = []  # creates the logout list
    log_outs.append(time_out)
    append_list_as_row(userlogouts, log_outs)
    Label(login_success_screen, text="Time out saved!", font="Helvetica 12").pack()
    login_success_screen.after(800, lambda: login_success_screen.destroy())  # closes the app after 80 milliseconds
    login_screen.destroy()


def print_log_in():  # outputs the logs
    Label(login_success_screen, text="Hi " + username1 + ", Here are your time in logs!", font="Helvetica 11").pack()
    with open(str(username1 + "_timein.csv")) as f:
        reader1 = csv.reader(f)
        for row in reader1:
            login = (" ".join(row))
            Label(login_success_screen, text=login, font="Helvetica 10").pack()
    Label(login_success_screen, text="-------------------------------").pack()


def print_log_out():  # shows the time outs
    Label(login_success_screen, text="Hi " + username1 + ", Here are your time out logs!", font="Helvetica 11").pack()
    with open(str(username1 + "_timeout.csv")) as f:
        reader2 = csv.reader(f)
        for row in reader2:
            logout = (" ".join(row))
            Label(login_success_screen, text=logout, font="Helvetica 10").pack()
    Label(login_success_screen, text="-------------------------------").pack()


def password_not_recognised():  # outputs if the password is incorrect
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():  # pop ups for unregistered users
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Not Found")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found", font="Helvetica 11").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def close_login_screen():  # terminates the login screen
    login_screen.destroy()


def delete_login_success():  # terminates the login screen
    login_success_screen.destroy()
    login_screen.destroy()


def delete_password_not_recognised():  # outputs if the password is incorrect
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():  # outputs if the user is not registered
    login_screen.destroy()


def digiclock():  # creates the digital clock
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, digiclock)


def open_clock():  # creates the digital clock window and triggers its opening
    global clock
    open_clock = Toplevel(main_screen)
    open_clock.title("Ram Digital Clock")
    clock = Label(open_clock, fg="#293A82", font=("Helvetica", 45, "bold"))
    clock.grid(row=3, column=2, pady=10, padx=10)
    digiclock()

    digi = Label(open_clock, image=logo)
    digi.grid(row=0, column=2)
    capt = str("#BeARam!")
    caption = Label(open_clock, text=capt, fg="#293A82", font="Helvetica 15 bold")
    caption.grid(row=1, column=2)
    nota = Label(open_clock, text="hours   minutes   seconds", fg="#293A82", font="Helvetica 14 bold")
    nota.grid(row=4, column=2)
    open_clock.mainloop()


def main_account_screen():  # Main screen module
    global main_screen
    global logo

    main_screen = Tk()
    main_screen.geometry("300x280")
    main_screen.title("Ram Time Check")
    logo = tk.PhotoImage(file="ram.gif")  # creates the logo
    tk.Label(main_screen, padx=10, text="", height="1", width="10", font="Helvetica 11").pack(side="top")
    tk.Label(main_screen, image=logo).pack(side="top")
    tk.Button(main_screen, padx=10, text="Login", height="1", width="10", font="Helvetica 11",
              command=login).pack(side="top")
    tk.Button(main_screen, padx=10, text="Register", height="1", width="10", font="Helvetica 11",
              command=register).pack(side="top")

    main_screen.mainloop()


main_account_screen()  # runs the application
