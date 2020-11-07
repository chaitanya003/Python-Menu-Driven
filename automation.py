import os
import getpass

print("==============================================================================")
print("\t\t WELCOME TO AWS MENU DRIVEN PROGRAM !!!!") 
print("==============================================================================")

pswd=getpass.getpass("ENTER PASSWORD:")

if pswd=="automation":
	while True :
		def s3b():
			bn=input("\nENTER BUCKET NAME:")
			r=input("\nENTER REGION:")
			os.system(" aws s3api create-bucket --bucket {}  --region {} --create-bucket-configuration  LocationConstraint=ap-south-1".format(bn,r))

		def strs3():
			bn=input("\nENTER BUCKET NAME:")
			print("\nLIST OF OBJECTS PRESENT IN {}".format(bn))
			os.system("aws s3 ls s3://{}".format(bn))
			op=input("ADD AN OBJECT (y/N):")
			if op=="y":
				lc=input("\nENTER location:")
				os.system("aws s3 ls s3://{}".format(bn))
				os.system("aws s3 sync {} s3://{} --acl public-read".format(lc,bn))
			else:
				exit()

		def ls():
			os.system('aws s3api list-buckets --query "Buckets[].Name"')

		def dlt():
			bn=input("\nENTER BUCKET NAME:")
			r=input("\nENTER REGION:")
			os.system("aws s3api delete-bucket --bucket {} --region {}".format(bn,r))

		def delo():
			bn=input("\nENTER BUCKET NAME:")
			on=input("\nENTER OBJECT NAME:")
			os.system("aws s3 rm s3://{}/{}".format(bn,on))

		def vol():
			vt=input("\nENTER VOLUME TYPE:")
			s=input("\nENTER SIZE OF VOLUME:")
			az=input("\nENTER AVAILABILITY ZONE:")
			os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(vt,s,az))

		def dvol():
			vi=input("\nENTER VOLUME ID:")
			os.system("aws ec2 delete-volume --volume-id {}".format(vi))

		def aconf():
			os.system("aws configure")

		def cfd():
			dn=input("\nENTER DOMAIN NAME:")
			os.system("aws cloudfront create-distribution --origin-domain-name {}".format(dn))

		def ckp():
			kn=input("\nENTER KEY NAME:")
			os.system("aws ec2 create-key-pair --key-name {}".format(kn))

		def dkp():
			kn=input("\nENTER KEY NAME:")
			os.system("aws ec2 delete-key-pair --key-name {}".format(kn))

		def dskp():
			kn=input("\nENTER KEY NAME:")
			os.system("aws ec2 describe-key-pairs --key-name {}".format(kn))

		def lins():
			it=input("\nENTER INSTANCE TYPE:")
			kn=input("\nENTER KEY NAME:")
			
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --count 1 --instance-type {} --key-name {} --subnet-id subnet-37666f5f".format(it,kn))

		def tins():
			ii=input("\nENTER IMAGE ID:")
			os.system("aws ec2 terminate-instances --instance-ids {}".format(ii))

		print('''
		Press 1:  Configuring aws
		Press 2:  Create key-pair 
		Press 3:  Delete key-pair
		Press 4:  Launch an instance
		Press 5:  Create a volume
		Press 6:  Delete a volume
		Press 7:  Describe key-pair 
		Press 8:  Create a bucket
		Press 9:  Bucket list
		Press 10: Adding an object
		Press 11: Delete a bucket
		Press 12: Delete Object of bucket 
		Press 13: For cloudfront distribution
		Press 14: Terminate an instance
		Press 0:  Exit
		''')

		c = int(input("\nEnter your choice :"))		
		if c==1:
			aconf()
		elif c==2:
			ckp()
		elif c==3:
			dkp()
		elif c==4:
			lins()
		elif c==5:
			vol()
		elif c==6:
			dvol()
		elif c==7:
			dskp()
		elif c==8:
			s3b()
		elif c==9:
			ls()
		elif c==10:
			strs3()
		elif c==11:
			dlt()
		elif c==12:
			delo()
		elif c==13:
			cfd()
		elif c==14:
			tins()
		elif c==0:
			exit()
		else:
			exit()

else:
	print("ENTER CORRECT PASSWORD")