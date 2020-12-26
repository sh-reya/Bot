import os
import getpass
print("\t\t\t WELCOME TO THE AUTOMATED MENU")
os.system("espeak-ng 'WELCOME TO THE AUTOMATED MENU' ")
while True:
  os.system("sleep 2")
  os.system("clear")

  password = getpass.getpass("Enter the password")

  if password != "shreya" :
    print("Try again")
    exit()

  r=input("How do you want to use the menu? Remote login or Local login?")


  print("""
  \n
  press 1: to run date
  press 2: to run cal
  press 3: to run reboot
  press 4: to exit
  press 5: to configure webserver
  press 6: to check the status of the webserver
  press 7: to activate the slave
  press 8: to activate the master
  press 9: to activate the docker
  press 10:to check the status of docker
  press 11:to stop the docker
  press 12:to check the hadoop cluster report
  press 13:to check the available docker images
  press 14:to launch docker container
  press 15"to download new docker image
  """)

  

 

  ch=input("Enter your choice : ")
  

  if r== "local" :
    if int(ch)==1:
      os.system("date")
    elif int(ch)==2:
      os.system("cal")
    elif int(ch)==3:
      os.system("reboot")
    elif int(ch)==4:
      exit()
    elif int(ch)==5:
      os.system("systemctl start httpd")
    elif int(ch)==6:
      os.system("systemctl status httpd")
    elif int(ch)==7:
      os.system("hadoop-daemon.sh start datanode")
    elif int(ch)==8:
      print("Please choose the remote login for configuring the master")
    elif int(ch)==9:
      os.system("systemctl start docker")
    elif int(ch)==10:
      os.system("systemctl status docker")
    elif int(ch)==11:
      os.system("systemctl stop docker")
    elif int(ch)==12:
      os.system("hadoop dfsadmin -report")
    elif int(ch)==13:
      os.system("docker images")
    elif int(ch)==14:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("docker run -it {}:{}". format(img,ver))
    elif int(ch)==15:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("docker pull {}:{}". format(img,ver))
      
    else:
      print("Invalid Choice")


  elif r== "remote" :
    ip=input("enter the desired IP: ")
    if int(ch)==1:
      os.system("ssh {} date". format(ip))
    elif int(ch)==2:
      os.system("ssh {} cal". format(ip))
    elif int(ch)==3:
      os.system("ssh {} reboot". format(ip))
    elif int(ch)==4:
      exit()
    elif int(ch)==5:
      os.system("ssh {} systemctl start httpd". format (ip))
    elif int(ch)==6:
      os.system("ssh {} systemctl status httpd". format (ip))
    elif int(ch)==7:
      print("Please choose the local login to configure the datanode")
    elif int(ch)==8:
      os.system("ssh {} hadoop-daemon.sh start namenode". format (ip))
    elif int(ch)==9:
      os.system("ssh {} systemctl start docker". format (ip))
    elif int(ch)==10:
      os.system("ssh {} systemctl status docker". format (ip))
    elif int(ch)==11:
      os.system("ssh {} systemctl stop docker". format (ip))
    elif int(ch)==12:
      os.system("ssh {} hadoop dfsadmin -report". format (ip))
    elif int(ch)==13:
      os.system("ssh {} docker images". format (ip))
    elif int(ch)==14:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("ssh {} docker run -it {}:{}". format(img,ver). format(ip))
    elif int(ch)==15:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("ssh {} docker pull {}:{}". format(img,ver). format(ip))
    else:
      print("Invalid Choice")
  else:
    print("Not supported")
