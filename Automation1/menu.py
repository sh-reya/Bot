
import os
while True:
  import getpass
  print("\t\t\t WELCOME TO THE AUTOMATED MENU")

  os.system("clear")
  print("""
  \n
  press 1: to run date
  press 2: to run cal
  press 3: to run reboot
  press 4: to exit
  press 5: to configure webserver
  press 6: to check the status of the webserver
  """)

  password = getpass.getpass("Enter the password")

  if password != "shreya" :
    print("Try again")
    exit()

  r=input("How do you want to use the menu? Remote login or Local login?")

  ch=input("Enter your choice : ")
  print(ch)

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
    else:
      print("Invalid Choice")
  else:
    print("Not supported")
