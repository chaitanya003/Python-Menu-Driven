import os
import subprocess
import getpass

os.system("tput setaf 5")
print("\n\t*************** Welcome to my LVM Menu Program !!!!*******************")

os.system("tput setaf 3")
passwd = getpass.getpass("\n\t\tENTER PASSWORD : ")
if passwd == "*******" :
	os.system("tput setaf 7")
	while True :

		print('''
		PRESS 1 : Check information about hardisk
		PRESS 2 : To create Physical Volume
		PRESS 3 : To create Volume Group
		PRESS 4 : To create & format & mount the  Partition or LVM
		PRESS 5 : To extend the size of volume 
		PRESS 6 : EXIT
		''')

	
		os.system("tput setaf 3")
		ch = int(input("\nEnter your choice : "))
	
		os.system("tput setaf 7")

		if ch == 1:
			os.system("fdisk -l")

		elif ch == 2:
			os.system("fdisk -l")
			pv1 = input("\nSelect the first hard disk that you want to create as physical volume : ")
			output1 = subprocess.getstatusoutput("pvcreate {}".format(pv1))
			print(output1)
			pv2 = input("\nSelect the second hard disk that you want to create as physical volume : ")
			output2 = subprocess.getstatusoutput("pvcreate {}".format(pv2))
			print(output2)

			os.system("tput setaf 3")
			print("\nPHYSICAL VOLUMES CREATED ...")
			os.system("tput setaf 7")
			os.system("pvdisplay")
		
	
	
		elif ch == 3:
			os.system("pvdisplay")
			vg_name = input("\nEnter name that you want to give to your Volume Group : ")
			pv1 = input("\nEnter first Physical Volume that will give space to Volume Group : ")
			pv2 = input("\nEnter first Physical Volume that will give space to Volume Group : ")
			output2 = subprocess.getstatusoutput("vgcreate  {}  {} {}".format(vg_name,pv1,pv2))
			print(output2)

			os.system("tput setaf 3")
			print("\nVOLUME GROUP")
			os.system("tput setaf 7")
			os.system("vgdisplay")
	
		elif ch == 4 :
			pa = input("\nEnter the LVM size you want to create in GiB (e.g.) 10G : ")
			pa_name = input("\nEnter the name of LVM : ")
			vg = input("\nEnter Volume Group from which you want to create LVM : ")
			output3 = subprocess.getstatusoutput("lvcreate --size {}  --name {}  {}".format(pa, pa_name, vg))
			print(output3)
			
			os.system("tput setaf 2")
			print("\nFormatting LVM !!!")
			os.system("tput setaf 7")
			output4 = subprocess.getoutput("mkfs.ext4  /dev/{}/{}".format(vg, pa_name))
			print(output4)
		

			dir = input("\nEnter the directory to which you want to mount the partition : ")
			output5 = subprocess.getstatusoutput("mount /dev/{}/{} {}".format(vg, pa_name, dir))
			os.system("tput setaf 2")
			print("\nMounting the partition")
			os.system("tput setaf 7")			
			print(output5)

			os.system("tput setaf 3")
			print("\nLOGICAL VOLUMES...")
			os.system("tput setaf 7")
			os.system("lvdisplay")
	
	
		elif ch == 5 :
			lve = input("\nEnter the size how much you want to extend : ")	
			vg1 = input("\nEnter Volume Group from which you want to extend : ")
			pa_name1 = input("\nEnter the name of LVM : ")
			output5 = subprocess.getstatusoutput("lvextend  --size {} /dev/{}/{}".format(lve,vg1,pa_name1))
			print(output5)
	
			os.system("tput setaf 2")
			print("\nFormatting the extend partition... ")
			os.system("tput setaf 7")
			output6 = subprocess.getstatusoutput("resize2fs /dev/{}/{}".format(vg1,pa_name1))
			print(output6)

		else:
			exit()

else :
	os.system("tput setaf 1")
	print("\nENTER CORRECT PASSWORD !!!\n")
	os.system("tput setaf 7")