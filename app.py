from tkinter import *
from tkinter import filedialog
from ftplib import FTP
import webbrowser
import socket
import os
import threading
from pyftpdlib.pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.pyftpdlib.handlers import FTPHandler
from pyftpdlib.pyftpdlib.servers import FTPServer
import random
#for support go to this website
def showCS():
    global cs
    global ss0
    cs.pack(side=TOP)
    ss0.pack_forget()
def showSS():
    global cs
    global ss0
    ss0.pack(side=TOP)
    cs.pack_forget()

def goToSite():
    webbrowser.open_new(r'http://www.google.com/')
def browse():
    folder1=filedialog.askdirectory()
    folderPath.set(folder1)
    folder1=folder1.split('/')
    folder.set(value=('Selected Folder: ' + str(folder1[len(folder1)-1])))
root = Tk()
global ipLabel
global server
global folderPath
folderPath = StringVar()
server=''
def killServer():
    global server
    try:
        server.close_all()
    except:
        pass
    root.destroy()
root.protocol('WM_DELETE_WINDOW', killServer)  # root is your root window
global actionbutton
actionbutton=StringVar()
actionbutton.set('Start Server')
global ss0
global files
files=[]
global cs
global ipEntry
global ftp
global pEntry
global userEntry
global passEntry
global pass1
global user
pass1=''
user=''
global credentialsFlag
credentialsFlag=StringVar()
credentialsFlag.set('')
global folder
folder = StringVar()
folder.set('Selected Folder: ')
global connectionStatusFlag
connectionStatusFlag = StringVar()
connectionStatusFlag.set('')
global ip
ip=''
hostname=socket.gethostname()
ip = socket.gethostbyname(hostname)
global thread
thread=''
def startServer():
    global user
    global pass11
    global ip
    global thread
    global actionbutton
    global connectionStatusFlag
    global credentialsFlag
    if( (actionbutton.get()) == 'Start Server' ):
        user='user' + str(random.randint(1, 1000))
        pass1 = random.randint(1000000, 9999999)
        print(thread)
        thread=threading.Thread(target=threadStartServer, args=[user, pass1])
        thread.start()
        actionbutton.set('Stop Server')
        connectionStatusFlag.set('Server Live')
        credentialsFlag.set('user: ' + str(user) + ' password: ' + str(pass1) + ' IP: ' + str(ip))
    else:
        server.close_all()
        #thread.kill()
        actionbutton.set('Start Server')
        connectionStatusFlag.set('')
        credentialsFlag.set('')

def threadStartServer(user, pass1):
    global server
    global ip
    authorizer = DummyAuthorizer()
    authorizer.add_user(username=user, password=pass1, perm="elr", homedir=folderPath.get())
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((ip, str(portEntry.get())), handler)
    server.serve_forever()
def download():
    global mylist
    global files
    sel=mylist.curselection()
    if(sel):
        filename = files[sel[0]]
        path = os.getcwd()
        localfile = open(path +'\\'+ filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        localfile.close()
def connectToServer():
    global cs6
    global ipEntry
    global userEntry
    global passEntry
    global cs7
    global scrollbar
    global mylist
    global files
    global ftp
    i=0
    try:
        ftp = FTP('')
        ftp.connect(str(ipEntry.get()),int(pEntry.get(), 10))
        ftp.login(str(userEntry.get()), str(passEntry.get()))
    except:
        i=1
    if(i==0):
        if(len(files) != 0):
            mylist.pack_remove()
        mylist = Listbox(cs6, yscrollcommand = scrollbar.set, selectmode=SINGLE, width=60 )
        mylist.pack( side = LEFT, fill = BOTH)
        scrollbar.config( command = mylist.yview )
        i=1
        files = []
        try:
            files = ftp.nlst()
        except:
            if str(resp) == "550 No files found":
                print ("No files in this directory")
            else:
                raise
        for f in files:
            mylist.insert(i, f)
            i=i+1
        cs6.grid(row=6)
        cs7.grid(row=7)
#cd documents\python_socket_programming\
#frame for connection
cs = Frame(root)
cs.pack(side = TOP)
cs1 = Frame(cs)
cs1.grid(row=1)
ipLabel=Label(cs1, text="IP address (127.0.0.1 for local server)", relief=FLAT, padx=5, pady=5)
ipLabel.grid(row=1, column=1)
ipEntry=Entry(cs1)
ipEntry.grid(row=1, column=2)
cs2=Frame(cs)
cs2.grid(row=2)
pLabel=Label(cs2, text="Port Number", relief=FLAT, padx=5, pady=5)
pLabel.grid(row=1, column=1)
pEntry=Entry(cs2)
pEntry.grid(row=1, column=2)
cs4=Frame(cs)
cs4.grid(row=3)
userLabel=Label(cs4, text="User Name", relief=FLAT, padx=5, pady=5)
userLabel.grid(row=1, column=1)
userEntry=Entry(cs4)
userEntry.grid(row=1, column=2)
cs3=Frame(cs)
cs3.grid(row=4)
passLabel=Label(cs3, text="Password", relief=FLAT, padx=5, pady=5)
passLabel.grid(row=1, column=1)
passEntry=Entry(cs3)
passEntry.grid(row=1, column=2)
cs5=Frame(cs)
cs5.grid(row=5)
connect = Button(cs5, text="Connect", command=connectToServer)
connect.grid(row=1, column=1)
cs6=Frame(cs)
global scrollbar
scrollbar = Scrollbar(cs6)
scrollbar.pack( side = RIGHT, fill = Y )
global mylist
global cs7
cs7=Frame(cs)
downloadButton=Button(cs7, text='Download', command=download)
downloadButton.grid(row=1, column=1)

#frame for server setup
ss0 = Frame(root)
ss0.pack(side = TOP)
ss = Frame(ss0)
ss.grid(row=1)
buttonLabel= Label(ss, text='Select the folder you want to set up as a Server', relief=FLAT, padx=5, pady=5)
buttonLabel.grid(row=1, column=1)
folderLocation=Button(ss, text='Browse', command=browse)
folderLocation.grid(row=1, column=2)
ss2 = Frame(ss0)
ss2.grid(row=2)
folderLabel=Label(ss2, textvariable=folder, relief=FLAT)
folderLabel.grid(row=1, column=1)
ss3 = Frame(ss0)
ss3.grid(row=3)
portLabel= Label(ss3, text='Enter port number', relief=FLAT, padx=5, pady=5)
portLabel.grid(row=1, column=1)
global portEntry
portEntry=Entry(ss3)
portEntry.grid(row=1, column=2)
ss4 = Frame(ss0)
ss4.grid(row=4)
start = Button(ss4, textvariable=actionbutton, command=startServer)
start.grid(row=1, column=1)
ss5=Frame(ss0)
ss5.grid(row=5)
connectionStatus = Label(ss5, textvariable=connectionStatusFlag, relief=FLAT, padx=5, pady=5)
connectionStatus.grid(row=1, column=1)
ss6=Frame(ss0)
ss6.grid(row=6)
credentials = Label(ss6, textvariable=credentialsFlag, relief=FLAT, padx=5, pady=5)
credentials.grid(row=1, column=1)#ADD data into this label

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Commands', menu=filemenu)
filemenu.add_command(label='Connect to Server', command=showCS)
filemenu.add_command(label='Set up a server', command=showSS)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=goToSite)
root.title('Samtech fileSharing')
root.geometry('450x450')
cs.pack_forget()
root.mainloop()
