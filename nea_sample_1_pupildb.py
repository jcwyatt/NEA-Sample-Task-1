import csv


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
	
	with open ("tutGroup.csv") as f:
		rawData = csv.reader(f)
		parseData = list(rawData)
		
		#request search ID from user (list maximum allowed value to prevent errors)
		pupilID = input("Enter ID number of pupil to be displayed (0-" + str(len(parseData)-1) + "): ")
	
		#find the index of the list containing the pupil being sought:
		#(read up on enumerate() if this makes no sense)
		for count, i in enumerate(parseData):
			try:
				i.index(pupilID)
				#do this if successfully found pupilID (store count value):
				pupilRec = count	
			except:
				continue
		#print out the correct pupils data with headings from first row of the csv
		for i in range (0,9):
			print (parseData[0][i] + ": " + parseData[pupilRec][i])
		



def showEmails():
	with open ("tutGroup.csv") as f:
		rawData = csv.reader(f)
		parseData = list(rawData)

		for count, i in enumerate(parseData):
			print (	parseData[count][0],
					parseData[count][1],
					parseData[count][2],
					(" "*(22-len(parseData[count][0])-len(parseData[count][1])-len(parseData[count][2]))),
					parseData[count][8])






def logout():
	print("Logging Out")
	exit()






def authenticate():
	username = ""
	password = ""
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

	input("\npress enter to display manu.\n")
	print("\n=========================")
	print("          Menu           ")
	print("=========================\n")
	print("Option              Press")
	print("------              -----")
	print("Add new student         1")
	print("Show all data           2")
	print("Search by pupil ID      3")
	print("Report: Gender Split    4")
	print("Report: Email address   5")
	print("Report: DOB - sorted    6")
	print("Logout                  7")

	menuchoice = input("\nchoose (1-7): ")
	
	if menuchoice =="7":
		logout()
	if menuchoice =="2":
		showall()
	if menuchoice =="4":
		reportGender()
	if menuchoice =="3":
		searchID()
	if menuchoice =="5":
		showEmails()
	else:
		menusystem()

	menusystem()


def main():
	authenticate()

	menusystem()



main()