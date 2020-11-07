import os
import getpass

os.system("tput setaf 3")
print("\t\t WELCOME TO AWS MENU DRIVEN PROGRAM !!!!") 

os.system("tput setaf 5")
pswd=getpass.getpass("ENTER PASSWORD:")
os.system("tput setaf 7")
if pswd=="automation":
 os.system("tput setaf 7")
 while True:
  def s3b():
   bn=input("ENTER BUCKET NAME:")
   r=input("ENTER REGION:")
   os.system(" aws s3api create-bucket --bucket {bucket}  --region {region} --create-bucket-configuration  LocationConstraint={region}".format(bucket=bn,region=r))
 

  def strs3():
   bn=input("ENTER BUCKET NAME:")
   print("LIST OF OBJECTS PRESENT IN {bucket}".format(bucket=bn))
   os.system("aws s3 ls s3://{bucket} ".format(bucket=bn))
   op=input("ADD AN OBJECT (Y/N):")
   if op=="Y":
    lc=input("ENTER location:")
    os.system("aws s3 ls s3://{bucket} ")
    os.system("aws s3 sync {location} s3://{bucket} --acl public-read".format(location=lc,bucket=bn))
   else:
    exit()

  def ls():
   os.system('aws s3api list-buckets --query "Buckets[].Name"')

  def dlt():
   bn=input("ENTER BUCKET NAME:")
   r=input("ENTER REGION:")
   os.system("aws s3api delete-bucket --bucket {bucket} --region {region}".format(bucket=bn,region=r))

  def delo():
   bn=input("ENTER BUCKET NAME:")
   on=input("ENTER OBJECT NAME:")
   os.system("aws s3 rm s3://{bucket}/{oname}".format(bucket=bn,oname=on))

  def vol():
   vt=input("ENTER VOLUME TYPE:")
   s=input("ENTER SIZE OF VOLUME:")
   az=input("ENTER AVAILABILITY ZONE:")
   os.system("aws ec2 create-volume --volume-type {vtype} --size {sz} --availability-zone {avz}".format(vtype=vt,sz=s,avz=az))

  def dvol():
   vi=input("ENTER VOLUME ID:")
   os.system("aws ec2 delete-volume --volume-id {vid}".format(vid=vi))

  def aconf():
   os.system("aws configure")

  def cfd():
   dn=input("ENTER DOMAIN NAME:")
   os.system("aws cloudfront create-distribution --origin-domain-name {}".format(dmn=dn))

  def ckp():
   kn=input("ENTER KEY NAME:")
   os.system("aws ec2 create-key-pair --key-name {knm}".format(knm=kn))

  def dkp():
   kn=input("ENTER KEY NAME:")
   os.system("aws ec2 delete-key-pair --key-name {knm}".format(knm=kn))

  def dskp():
   kn=input("ENTER KEY NAME:")
   os.system("aws ec2 describe-key-pairs --key-name {knm}".format(knm=kn))

  def lins():
   ii=input("ENTER IMAGE ID:")
   it=input("ENTER INSTANCE TYPE:")
   kn=input("ENTER KEY NAME:")
   sg=input("ENTER SECURITY GROUP ID:")
   si=input("ENTER SUBNET ID:")
   os.system("aws ec2 run-instances --image-id {ii} --count 1 --instance-type {it} --key-name {kn} --security-group-ids {sg} --subnet-id {si}".format(imgi=ii,inst=it,kyn=kn,scg=sg,snt=si))


  def tins():
   ii=input("ENTER IMAGE ID:")
   os.system("aws ec2 terminate-instances --instance-ids {}".format(imgi=ii))


  print("Press 1: for creating bucket")
  print("Press 2: for adding object")
  print("Press 3: for bucket list")
  print("Press 4: for deleting bucket")
  print("Press 5: for deleting object of bucket")
  print("Press 6: for creating a volume")
  print("Press 7: for deleting a volume")
  print("Press 8: for configuring aws")
  print("Press 9: for cloudfront distribution")
  print("Press 10: for creating key-pair") 
  print("Press 11: for deleting key-pair") 
  print("Press 12: for describing key-pair") 
  print("Press 13: for launching an instance")
  print("Press 14: for terminating an instance")
  print("Press 0:  for exit")
  c=input()
  if c=="1":
   s3b()
  elif c=="2":
   strs3()
  elif c=="3":
   ls()
  elif c=="4":
   dlt()
  elif c=="5":
   delo()
  elif c=="6":
   vol()
  elif c=="7":
   dvol()
  elif c=="8":
   aconf()
  elif c=="9":
   cfd()
  elif c=="10":
   ckp()
  elif c=="11":
   dkp()
  elif c=="12":
   dskp()
  elif c=="13":
   lins()
  elif c=="14":
   tins()
  elif c=="0":
   exit()
  else:
   exit()
 else:
  os.system("tput setaf 3")
  print("ENTER CORRECT PASSWORD")
  os.system("tput setaf 7")