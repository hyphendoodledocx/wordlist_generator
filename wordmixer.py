#!/usr/bin/env python

keywords=['']
def getkeywords() :
	global keywords
	try:
		num_of_keywords=int(input("Enter the number of keywords you are going to use : "))
		integer=10
		for i in range(num_of_keywords) :
			ipt=input("Enter Keyword No."+str(i+1)+" : ")
			keywords.append(ipt)
		print("The keywords you entered are the following : ")
		for i in keywords :
			print(i)
	except:
		print("Enter information properly without violating variable type rules")
		getkeywords()

def mix():
	new_keywords=[]
	global keywords
	for i in keywords :
		for j in keywords :
			new_keywords.append(i+j)
	keywords=new_keywords
	print("Completed.")
def addnum():
	new_keywords=[]
	global keywords
	addr=['','1','12','123','1234','12345','123456']
	for i in keywords :
		for j in addr :
			new_keywords.append(i+j)
	keywords=new_keywords
	print("Completed.")

def getparameters() :
	global keywords
	try :
		mixq=input("Enable Mixing? If enabled, the wordlist will contain words with combinations of the keywords you have given. Also, enabling this feature will substantially increase time use.[Y/N]")
		if(mixq=='Y'or mixq=='y') :
			print("You have enabled mixing")
			print("Processing mix...")
			mix()
			mixq=True
		else :
			print("You have disabled mixing")
			mixq=False
		usenum=input("Enable numbers? If enabled, the wordlist will append consecutive number strings such as 1234 to the keywords. [Y/N]")
		if(usenum=='Y' or usenum=='y') :
			print("You have enabled numbers")
			print("Adding numbers...")
			addnum()
			usenum=True
		else :
			print("You have disabled numbers")
			usenum=False

	except ValueError:
		print("Enter information properly without violating variable type rules")

def printlistviaconsole():
	hquery="Would you like the wordlist printed on console? (standard output) [Y/N]"
	query=input(hquery)
	if(query=='y' or query=='Y') :
		for i in keywords:
			print(i)
		print("\nCompleted")

def printlistviafile() :
	global keywords
	jquery="Will you make a wordlist file as output?[Y/N]"
	query=input(jquery)
	if(query=='y' or query=='Y') :
		fname=input("Enter the wordlist file name u will use (ex. douchebag.txt) : ")
		if(len(fname)<=1 ):
			print("Since your filename is so short, I automatically named it to douchebag.txt")
			fname="douchebag.txt"
		ofile=open(fname,'w')
		for i in keywords:
			ofile.write(i)
			ofile.write("\n")
		print("Completed writing wordlist file and saved it as "+fname)
		ofile.close()
		printlistviaconsole()
		
	else :
		printlistviaconsole()
getkeywords()
getparameters()
printlistviafile()
print("bye")


