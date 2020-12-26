
import os
import getpass
print("\t\t\t WELCOME TO THE AUTOMATED MENU")
os.system("espeak-ng 'WELCOME TO THE AUTOMATED MENU' ")
password = getpass.getpass("Enter the password")

if password != "shreya" :
  print("Try again")
  exit()

r=input("What you prefer? REMOTE login or LOCAL login?  ")

while True:
  os.system("sleep 2")
  os.system("clear")

  

  print("""
  \n
  press 1:  check DATA
  press 2:  view CAL
  press 3:  REBOOT
  press 4:  EXIT
  press 5:  Configure Webserver
  press 6:  Check the STATUS of Webserver
  press 7:  Deactivate the webserver
  press 8:  Activate SLAVE of Hadoop_Cluster
  press 9:  Activate MASTER of Hadoop_Cluster
  press 10: view HADOOP_CLUSTER_REPORT
  press 11: Activate_DOCKER
  press 12: Check STATUS of DOCKER
  press 13: Stop Docker services
  press 14: Enable Docker
  press 15: Disable Docker  
  press 16: Check the available docker images
  press 17: Launch new DOCKER CONTAINER
  press 18: Download required image
  press 19: Download Ansible to initiate automation
  press 20: Check the details of your HARD_DISK
  press 21: Check the partition of Hardisk
  press 22: Check the prononciation of a text
  press 23: Show all the ports in use
  press 24: Ping your Friend
  press 25: Create an file
  press 26: Create a directory
  press 27: List all the files and folder
  press 28: View the contents of the file
  press 29: Remove a file
  press 30: Remove a folder
  press 31: Copy a file
  press 32: Create a file in CLI
  press 33: Capture a packet
  press 34: Check the PROCESS NUMBER of a Program
  press 35: kill a program
  press 36: Open Python terminal
  press 37: Show the details of CPU
  press 38: Check the status of RAM
  press 39: Create a new user
  press 40: Check IP of the system
  press 41: Show the task manager
  press 42: Clear the cache
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
      os.system("systemctl stop httpd")
    elif int(ch)==8:
      os.system("hadoop-daemon.sh start datanode")
    elif int(ch)==9:
      print("Please choose the remote login for configuring the master")
    elif int(ch)==10:
      os.system("hadoop dfsadmin -report")
    elif int(ch)==11:
      os.system("systemctl start docker")
    elif int(ch)==12:
      os.system("systemctl status docker")
    elif int(ch)==13:
      os.system("systemctl stop docker")
    elif int(ch)==14:
      os.system("systemctl enable docker")
    elif int(ch)==15:
      os.system("systemctl disable docker")
    elif int(ch)==16:
      os.system("docker images")
    elif int(ch)==17:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("docker run -it {}:{}". format(img,ver))
    elif int(ch)==18:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("docker pull {}:{}". format(img,ver))
    elif int(ch)==19:
      os.system("pip3 install ansible")
    elif int(ch)==20:
      os.system("fdisk -l")
    elif int(ch)==21:
      os.system("fdisk /dev/xvdf")
    elif int(ch)==22:
      text=input("Enter text: ")
      os.system("espeak-ng '{}'". format(text))
    elif int(ch)==23:
      os.system("netstat -tnlp")
    elif int(ch)==24:
      ip=input("Enter ip you want to ping: ")
      os.system("ping {}". format(ip))
    elif int(ch)==25:
      name=input("Enter file name with extension: ")
      os.system("gedit {}". format(name))
    elif int(ch)==26:
      name=input("Enter name of the directory: ")
      os.system("mkdir {}". format(name))
    elif int(ch)==27:
      #name=input("Enter name of the directory: ")
      os.system("ls")
    elif int(ch)==28:
      name=input("Enter name of the file: ")
      os.system("cat {}". format(name))
    elif int(ch)==29:
      name=input("Enter name of the file you want to remove: ")
      os.system("rm {}". format(name))
    elif int(ch)==30:
      name=input("Enter name of the directory: ")
      os.system("rm -rf {}". format(name))
    elif int(ch)==31:
      n=input("Enter name of the file you want to copy: ")
      m=input("Enter new name: ")
      os.system("cp {} {}". format(n,m))
    elif int(ch)==32:
      n=input("Enter name of the file you want to create: ")
      
      os.system("vim {}". format(n))
    elif int(ch)==33:
      os.system("tcpdump")
    elif int(ch)==34:
      n=input("Enter process name: ")
      os.system("pgrep {}". format(n))
    elif int(ch)==35:
      n=input("Enter process number you want to kill: ")
      os.system("kill {}". format(n))
    elif int(ch)==36:
      os.system("python3")
    elif int(ch)==37:
      os.system("ls cpu")
    elif int(ch)==38:
      os.system("free -m")
    elif int(ch)==39:
      n=input("User Name: ")
      os.system("add user {}". format(n))
    elif int(ch)==40:
      os.system("ifconfig enp0s3")
    elif int(ch)==41:
      os.system("top")
    elif int(ch)==42:
      os.system("echo 3> /proc/sys/vm/drop-caches")
      
    else:
      print("Invalid Choice")


  elif r== "remote" :
    ip=input("enter the desired IP: ")
    if int(ch)==1:
      os.system("ssh {} date". format(ip))
    elif int(ch)==2:
      os.system("ssh {} cal". format(ip))
    elif int(ch)==3:
      os.system("ssh {} reboot". format (ip))
    elif int(ch)==4:
      exit()
    elif int(ch)==5:
      os.system("ssh {} systemctl start httpd". format (ip))
    elif int(ch)==6:
      os.system("ssh {} systemctl status httpd". format (ip))
    elif int(ch)==7:
      os.system("ssh {} systemctl stop httpd". format(ip))
    elif int(ch)==8:
      os.system("ssh {} hadoop-daemon.sh start datanode". format (ip))
    elif int(ch)==9:
      print("Please choose the remote login for configuring the master")
    elif int(ch)==10:
      os.system("ssh {} hadoop dfsadmin -report". format(ip))
    elif int(ch)==11:
      os.system("ssh {} systemctl start docker". format(ip))
    elif int(ch)==12:
      os.system("ssh {} systemctl status docker". format (ip))
    elif int(ch)==13:
      os.system("ssh {} systemctl stop docker". format (ip))
    elif int(ch)==14:
      os.system("ssh {} systemctl enable docker". format(ip))
    elif int(ch)==15:
      os.system("ssh {} systemctl disable docker". format (ip))
    elif int(ch)==16:
      os.system("ssh {} docker images". format (ip))
    elif int(ch)==17:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("ssh {} docker run -it {}:{}". format(img,ver). format (ip))
    elif int(ch)==18:
      img=input("Enter the image you want to launch: ")
      ver=input("Enter the preffered version: ")
      os.system("ssh {} docker pull {}:{}". format(img,ver). format (ip))
    elif int(ch)==19:
      os.system("ssh {} pip3 install ansible". format (ip))
    elif int(ch)==20:
      os.system("ssh {} fdisk -l". format (ip))
    elif int(ch)==21:
      os.system("ssh {} fdisk /dev/xvdf". format (ip))
    elif int(ch)==22:
      text=input("Enter text: ")
      os.system("ssh {} espeak-ng '{}'". format(text). format(ip))
    elif int(ch)==23:
      os.system("ssh {} netstat -tnlp". format(ip))
    elif int(ch)==24:
      ipn=input("Enter ip you want to ping: ")
      os.system("ssh {} ping {}". format(ipn). format(ip))
    elif int(ch)==25:
      name=input("Enter file name with extension: ")
      os.system("ssh {} gedit {}". format(name). format(ip))
    elif int(ch)==26:
      name=input("Enter name of the directory: ")
      os.system("ssh {} mkdir {}". format(name). format(ip))
    elif int(ch)==27:
      #name=input("Enter name of the directory: ")
      os.system("ssh {} ls". format (ip))
    elif int(ch)==28:
      name=input("Enter name of the file: ")
      os.system("ssh {} cat {}". format(name). format(ip))
    elif int(ch)==29:
      name=input("Enter name of the file you want to remove: ")
      os.system("ssh {} rm {}". format(name). format(ip))
    elif int(ch)==30:
      name=input("Enter name of the directory: ")
      os.system("ssh {} rm -rf {}". format(name). format(ip))
    elif int(ch)==31:
      n=input("Enter name of the file you want to copy: ")
      m=input("Enter new name: ")
      os.system("ssh {} cp {} {}". format(n,m). format(ip))
    elif int(ch)==32:
      n=input("Enter name of the file you want to create: ")
      
      os.system("ssh {} vim {}". format(n). format(ip))
    elif int(ch)==33:
      os.system("ssh {} tcpdump". format(ip))
    elif int(ch)==34:
      n=input("Enter process name: ")
      os.system("ssh {} pgrep {}". format(n). format(ip))
    elif int(ch)==35:
      n=input("Enter process number you want to kill: ")
      os.system("ssh {} kill {}". format(n). format(ip))
    elif int(ch)==36:
      os.system("ssh {} python3". format(ip))
    elif int(ch)==37:
      os.system("ssh {} ls cpu". format(ip))
    elif int(ch)==38:
      os.system("ssh {} free -m". format (ip))
    elif int(ch)==39:
      n=input("User Name: ")
      os.system("ssh {} add user {}". format(n). format(ip))
    elif int(ch)==40:
      os.system("ssh {} ifconfig enp0s3". format(ip))
    elif int(ch)==41:
      os.system("ssh {} top". format(ip))
    elif int(ch)==42:
      os.system("ssh {} echo 3> /proc/sys/vm/drop-caches". format (ip))
    else:
      print("Invalid Choice")
  else:
    print("Not supported")
