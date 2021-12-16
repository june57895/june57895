
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def pythonfile ():
    global PT_snake
def snakegame(): 
    global snakeprofile
    snakeprofile=Toplevel()
    snakeprofile.title("snake")
    snakeprofile.geometry('600x600+500+100')
    menusnake = Menu(snakeprofile) 
    snakeprofile.config(menu=menusnake)
    snakemenu =Menu(menusnake, tearoff=0)
    menusnake.add_cascade(label='SNAKE&LADDER',menu=snakemenu)
    
def shane_game():
     print ('game')
     
def leaderboard():
    global leaderboard
    leaderboard=Toplevel()
    lbl=label(leaderboard,text="position ").pack
    #print('position')
def about():
    print('snake and ladder')
    
def option():
    global Help
    Helpprofile=Toplevel()
    Helpprofile.title("option")
    print('This game is concise of rise and fall you may go up the ladder or down the snake')
def setting():
    global Settingprofile
    settingprofile=Toplevel()
    settingprofile.title("setting")
    lbl_settingfile = Label(window, text="Don't Have an Account? Create an Account")
    print('volume,sound,base')
    
def scores():
    print('scores')
    
def edit():
    print('rub')
    
def Help():
    global Helpprofile
    Helpprofile=Toplevel()
    Helpprofile.title("Help")
    lbl_helpprofile = Label(window, text="Don't Have an Account? Create an Account")
    print ('This game Is concise of rise And fall you may go up the ladder or down the snake')
def Exit():
    global Exitprofile
    Exitprofile=Toplevel()
    Exitprofile.title("Exit")

def userprofile():
    global userprofilewin
    userprofilewin=Toplevel()
    userprofilewin.title('clyan livingston')
    userprofilewin.geometry('600x600+500+100')

    menubar = Menu(userprofilewin) 
    userprofilewin.config(menu=menubar)
    filemenu =Menu(menubar, tearoff=0)
    menubar.add_cascade(label='SNAKE&LADDER',menu=filemenu)
    filemenu.add_separator()
   
    filemenu.add_command(label='NEW',command=snakegame)
    filemenu.add_command(label='CONTINUE',command=snakegame)
    filemenu.add_command(label='RESTART',command=snakegame)
    
    filemenu.add_separator()
   
    filemenu.add_command(label='LEADER BOARD',command=leaderboard)
    filemenu.add_command(label="SCORES",command=scores)
   

    filemenu.add_separator()
    
   
    filemenu.add_command(label="OPTION",command=option) 
    filemenu.add_command(label='ABOUT',command=about)
    filemenu.add_command(label='HELP',command=Help)
    
    filemenu.add_separator()

    filemenu.add_command(label ="Edit",command=edit)
    filemenu.add_command(label="setting",command=setting)
    


    filemenu.add_command(label='Exit', command=Exit)
    
    tk.Label(userprofilewin, text='Welcome '+signin_username.get(), font ="algerian 20 bold"). place(x=100, y=10)

    userprofilewin.mainloop()
    
def login():
    loginfile = open('clyan_register.txt','r')
    for line in loginfile:
        if':' in line:
            key,value=line.split(':',1)
            cvalue = len(value)-1
            value = value[0:cvalue]
            user_dictionary[key] = value
        else:
            pass
    temp_username=user_dictionary.get('username')
    temp_password=user_dictionary.get('password')
    if(temp_username == signin_username.get() and temp_password ==signin_pwd.get()):
        userprofile()
    else:
        messagebox.showinfo('information','incorrect password or username')     
    loginfile.close()    

def signin():
    global signin_frame, signin_username, signin_pwd, signin_fname, signin_lname, signin_phone#
    signin_frame = Toplevel()
    signin_username = StringVar()
    signin_pwd= StringVar()
    signin_fname= StringVar()
    signin_lname= StringVar()
    sigin_phone= StringVar()
    
    signin_frame.title("Sign in Section")
    signin_frame.geometry("500x500+500+100")
    signin_img = PhotoImage(file='snake pic.png')
    Label(signin_frame,  image=signin_img).place(x = 140, y = 5)
    Label(signin_frame, text = "username").place(x=120,y=200)
    entry_username = Entry(signin_frame, width=20, textvariable=signin_username)
    entry_username.place(x=120, y=220)
    

    Label(signin_frame, text = "Password").place(x=120,y=260)
    entry_pwd = Entry(signin_frame, width=20, show="*", textvariable=signin_pwd)
    entry_pwd.place(x=120, y=280)
    
    btn_login = PhotoImage(file='login.png')
    tk.Button(signin_frame,  bg='white', image = btn_signin, highlightbackground='white', highlightcolor ='purple',
              highlightthickness=0,  command=login).place (x = 190, y = 410)

    entry_username.focus()
    entry_pwd.focus()
    
    signin_frame.mainloop()
    
def register():
    registerfile = open("clyan_register.txt","w")
    extract_username = reg_username.get()
    extract_pwd = reg_pwd.get()
    extract_fname=reg_fname.get()#
    exract_lname=reg_lname.get()#
    extract_phone=reg_phone.get()#

    user_dictionary['username'] = extract_username
    user_dictionary['password'] = extract_pwd
    user_dictionary['fname'] = extract_fname#
    user_dictionary['lname'] = extract_lname#
    user_dictionary['phone'] = extract_phone#

    for key,value in user_dictionary.items():
        registerfile.write('%s:%s\n'%(key,value))
    registerfile.close()
    messagebox.showinfo("information", "Your account has been successfully created")

    reg_username.set("")
    reg_pwd.set("")
    reg_fname.set("")#
    reg_lname.get("")#
    reg_phone.get("")#

def signup(event):
    global reg_fname, reg_lname, reg_username, reg_pwd, reg_phone
    regwin = Toplevel()
    reg_fname = StringVar()
    reg_lname = StringVar()
    reg_username = StringVar()
    reg_pwd = StringVar()
    reg_phone = StringVar()
    regwin.title("Registration Section")
    regwin.geometry("500x600+500+100")
    img = PhotoImage(file='snake pic.png')
    Label(regwin,  image=img).place(x = 140, y = 5)
    

    Label(regwin, text = "Username").place(x=120,y=200)
    reguname = Entry(regwin, width=20, textvariable=reg_username)
    reguname.place(x=120, y=220)

    Label(regwin, text = "Password").place(x=120,y=260)
    regpwd = Entry(regwin, width=20, show="*",textvariable=reg_pwd)
    regpwd.place(x=120, y=280)

    Label(regwin, text = "First Name").place(x=120,y=320)
    regfname = Entry(regwin, width=20, textvariable=reg_fname)
    regfname.place(x=120, y=340)

    Label(regwin, text = "Last Name").place(x=120,y=380)
    reglname = Entry(regwin, width=20, textvariable=reg_lname)
    reglname.place(x=120, y=400)

    Label(regwin, text = "Phone").place(x=120,y=440)
    regphone = Entry(regwin, width=20, textvariable=reg_phone)
    regphone.place(x=120, y=460)

    reguname.focus()

    Button(regwin, text="Create", command = register).place(x=250, y = 500)
    

    regwin.mainloop()


user_dictionary = { }
window = tk.Tk()
window.title("My GUI ON SNAKE & LADDER")
window.geometry("400x400+500+150")
window['background'] = 'white'
lblimage = PhotoImage(file='snake pic.png')
Label(window, text="Snake and Ladder Game", bg='white',fg='#a68fc2', font =('algerian', 18, 'bold')).place(x=45, y=10)

Label(window, bg='white', image=lblimage).place(x=100, y=40)

btn_signin = PhotoImage(file='signin.png')
tk.Button(window,  bg='purple', image = btn_signin, highlightbackground='black', highlightcolor ='#971F05',
                   highlightthickness=0,  command=signin).place (x = 145, y = 270)

lbl_signup = Label(window, text="Don't Have an Account? Create an Account", bg='#499179',
                                    fg='white',font=('algerian',9,'bold'),cursor="hand2")
lbl_signup.place(x=45, y=330)
lbl_signup.bind("<Button-1>",signup)


window.mainloop()
