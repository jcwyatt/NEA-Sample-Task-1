#Nea task

#autheticate user



#def opencsv():
#	with open ("tutGroup.csv") as f:


def showall():
	with open ("tutGroup.csv") as f:
		print(f.read())


def reportGender():
	with open ("tutGroup.csv") as f:
		data = f.read()
		females = data.count(",F,")
		males = data.count(",M,")

		print("Males:%d Females:%d" % (males,females))

def searchID():
	pupilID = input("Enter ID number of pupil to be displayed e.g. 3: ")
	with open ("tutGroup.csv") as f:
		rawdata = f.read()
		parseData = rawdata.split(",")
		
		j = (parseData.index(pupilID)) #finds matching ID location
		


		for i in range (0,8):
			print (parseData[i+1] + ": " + parseData[j+i]) #prints headings and next 7 items of data


def logout():
	print("Logging Out")
	exit()


def authenticate():
	username=""
	password=""
	tries = 0

	print ("Welcome! \nTutor Group Management System v0.0\n")
	print ("Please login to continue.\n")
	

	while username != "l" or password !="m":
		username = input ("Username: ")
		password = input ("Password: ")

		tries +=1

		if tries == 3:
			print("unauthorised access. Closing.")
			exit()


		
def menusystem():
	print("\n=======================")
	print("=        Menu         =")
	print("=======================\n7")
	print("Option            Press")
	print("------            -----")
	print("Add new student       1")
	print("Show all data         2")
	print("Search by pupil ID    3")
	print("Report: Gender Split  4")
	print("Report: Email address 5")
	print("Report: DOB - sorted  6")
	print("Logout                7")

	menuchoice = input(":")
	
	if menuchoice =="7":
		logout()
	if menuchoice =="2":
		showall()
	if menuchoice =="4":
		reportGender()
	if menuchoice =="3":
		searchID()






def main():
	authenticate()

	menusystem()

main()