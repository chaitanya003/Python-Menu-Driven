import getpass
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
os.system('tput setaf 3')
print("\t\t\t\t\t\t\t\t\t\t\t welcome to the world of Automation")
os.system('tput setaf 6')

p=getpass.getpass("Enter your password:")
def cored():
  nn_ip = input('Enter NameNode ip and hadoop port eg. hdfs://1.2.3.4:9000:')
  print(nn_ip)
  os.system('echo \<configuration\> >> core-site.xml')
  os.system('echo \<property\> >> core-site.xml')
  os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
  os.system("echo \<value\>{}\<\/value\> >> core-site.xml".format(nn_ip))
  os.system('echo \<\/property\> >> core-site.xml')
  os.system("echo \<\/configuration\> >> core-site.xml")
def hdfsd():
  dndir = input('Enter directory name you want to create for datanode:')
  print(dndir)

  os.system('echo \<configuration\> >> hdfs-site.xml')
  os.system('echo \<property\> >> hdfs-site.xml')
  os.system("echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml")
  os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(dndir))
  os.system('echo \<\/property\> >> hdfs-site.xml')
  os.system("echo \<\/configuration\> >> hdfs-site.xml")

  os.system("mkdir {}".format(dndir))
def data():
  dir = input('Enter directory name where java and hadoop file resides:')
  print(dir)
  os.system('rpm -i {}/jdk-8u171-linux-x64.rpm'.format(dir))
  os.system("rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force".format(dir))
  cored()
  hdfsd()
  os.system("hadoop-daemon.sh start datanode")
  os.system("jps")
def core_n():
  nn_ip = input('Enter NameNode ip and hadoop port eg. hdfs://1.2.3.4:9000:')
  print(nn_ip)
  os.system('echo \<configuration\> >> core-site.xml')
  os.system('echo \<property\> >> core-site.xml')
  os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
  os.system("echo \<value\>{}\<\/value\> >> core-site.xml".format(nn_ip))
  os.system('echo \<\/property\> >> core-site.xml')
  os.system("echo \<\/configuration\> >> core-site.xml")
def hdfs_n():
  dndir = input('Enter directory name you want to create for datanode:')
  print(dndir)

  os.system('echo \<configuration\> >> hdfs-site.xml')
  os.system('echo \<property\> >> hdfs-site.xml')
  os.system("echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml")
  os.system("echo \<value\>{}\<\/value\> >> hdfs-site.xml".format(dndir))
  os.system('echo \<\/property\> >> hdfs-site.xml')
  os.system("echo \<\/configuration\> >> hdfs-site.xml")
  os.system("mkdir {}".format(dndir))
def name():
  dir = input('Enter directory name where java and hadoop file resides:')
  print(dir)
  os.system('rpm -i {}/jdk-8u171-linux-x64.rpm'.format(dir))
  os.system("rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force".format(dir))
  core_n()
  hdfs_n()
  os.system("hadoop-daemon.sh start datanode")
  os.system("jps")
def yum():
  i = input('Enter folder_name/repo_name u want to mount to :')
  os.system('mkdir \/{}'.format(i))
  os.system('mount \/dev\/cdrom \/dvd')
  os.system('touch \/etc\/yum.repos.d\/{}\.repo'.format(i))
  os.system('echo \[dvd\] \>\> \/etc\/yum.repos.d\/dvd.repo')
  os.system('echo baseurl\=file\\\:\/\/{}\/BaseOS \>\> \/etc\/yum.repos.d\/dvd.repo'.format(i))
  os.system('echo gpgcheck\=0 \>\> \/etc\/yum.repos.d\/dvd.repo')
  os.system('echo \[dvd1\] \>\> \/etc\/yum.repos.d\/dvd.repo')
  os.system('echo baseurl\=file\\\:\/\/{}\/AppStream \>\> \/etc\/yum.repos.d\/dvd.repo'.format(ip,i))
  os.system('echo gpgcheck \= 0 \>\> \/etc\/yum.repos.d\/dvd.repo')
  os.system('echo mount \/dev\/cdrom {} \>\> \/etc\/rc.d\/rc.local'.format(i))
  os.system('chmod +x \/etc\/rc.d\/rc.local')
  os.system('yum clean all')
  os.system('yum repolist')
def partition():
  a1=input('enter dick name:')
  os.system('fdisk /dev/{}'.format(a1))

def web_server():
  os.system('yum install httpd')
  os.system('systemctl start httpd')
  os.system('systemctl enable httpd')
def docker_launch():
  i=input("enter image name to launch OS:")
  j=input('enter name of your os to launch:')
  os.system('docker run -it --name {} {}'.format(j,i))
def docker_start():
  k=input('enter name of os to start and attach:')
  os.system('docker start {}'.format(k))
  os.system('docker attach {}'.format(k))
def docker_delete():
  l=input('enter the os name to terminate')
  os.system('docker stop {}'.format(l))
  os.system('docker rm {}'.format(l))
def docker_image():
  m=input('enter the name of OS image which you want to use (with version , if version not mention then it consider latest version.)')
  os.system('docker pull {}'.format(m ))
def docker_conf():
  os.system('yum install docker-ce --nobest')
  os.system('systemctl enable docker')
  os.system('systemctl status docker')
if p!='saket30':
  print('oops! you have entered wrong password')
  exit()

else:
  while True:
    print("choose your requirements\n\n")
    print('option 1: for date command')
    print('option 2: for cal command')
    print('option 3: for configure yum')
    print('option 4: for configure web server')
    print('option 5: for configure docker')
    print('option 6: for new OS image')
    print('option 7: to launch new OS')
    print('option 8: to start and attach existing OS')
    print('option 9: to see all docker images existing')
    print('option 10:to terminate an OS')
    print('option 11:to terminate all OS')
    print('option 12:to configure data node')
    print('option 13:to configure name node')
    print('option 14:for partition ')
    print('option 0 : to quit')
    print("Please your requirements............. we are listening.....", end="")
    r=sr.Recognizer()

    with sr.Microphone() as source:
      print('say something......')
      audio=r.listen(source)
      print("we go it, plzzzz wait")
    ch=r.recognize_google(audio)
    if(("date" in ch) or ('one' in ch) or ('first' in ch)) and (("run" in ch) or ("execute" in ch)):
      os.system("date")
    elif(("cal" in ch) or ('two' in ch) or ('second' in ch)) and (("run" in ch) or ("execute" in ch)):
      os.system('cal')
    elif(("yum" in ch) or ('three' in ch) or ('third' in ch)) and (("run" in ch) or ("execute" in ch)):
      yum()
    elif(("webserver" in ch) or ('four' in ch) or ('fourth' in ch)) and (("run" in ch) or ("execute" in ch)):
      web_server()
    elif(("docker" in ch) or ('five' in ch) or ('fifth' in ch)) and (("run" in ch) or ("execute" in ch)):
      docker_conf()
    elif(("image" in ch) or ('six' in ch) or ('sixth' in ch)) and (("run" in ch) or ("execute" in ch)):
      docker_image()
    elif(("launch new OS" in ch) or ('seven' in ch) or ('seventh' in ch)) and (("run" in ch) or ("execute" in ch)):
      docker_launch()
    elif(("start" in ch) or ('eight' in ch) or ('eighth' in ch)) and (("run" in ch) or ("execute" in ch)):
      docker_start()
    elif(("existing" in ch) or ('nine' in ch) or ('ninth' in ch)) and (("run" in ch) or ("execute" in ch)):
      os.system('docker ps -a')
    elif(("terminate" in ch) or('delete' in ch) or ('ten' in ch) or ('tenth' in ch)) and (("run" in ch) or ("execute" in ch)):
      docker_delete()
    elif(("terminate" in ch) or('delete' in ch) or ('eleven' in ch) or ('eleventh' in ch)) and (("run" in ch) or ("execute" in ch)) and ('all' in ch):
      os.system('docker rm `docker ps -a -q`')
    elif(("data" in ch) or ('twelve' in ch) or ('twelth' in ch)) and (("run" in ch) or ("execute" in ch)):
      data()
    elif(("name" in ch) or ('thirtheen' in ch) or ('thirtheenth' in ch)) and (("run" in ch) or ("execute" in ch)):
      name()
    elif(("partition" in ch) or ('fourteen' in ch) or ('fourteenth' in ch)) and (("run" in ch) or ("execute" in ch)):
      partition()
    elif(("quit" in ch) or ('zero' in ch) or ('zeroth' in ch)):
      exit()
    else:
      print('sorry canot recognize')

