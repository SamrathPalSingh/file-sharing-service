from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('./') #replace with your directory

def uploadFile():
 filename = 'testfile.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'messanger.py' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'w')
 ftp.retrlines('RETR ' + filename, localfile.write)
 ftp.quit()
 localfile.close()

#uploadFile()
downloadFile()
