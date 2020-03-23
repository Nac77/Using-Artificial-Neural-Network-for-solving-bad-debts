import random

greetings = ['Hi','hi','Hello','hello','hiya','yo','Hola']
random_greeting = random.choice(greetings)

msg1 = ['Welcome to the bad debt predictor!','You have come to the bad debt predictor..']
random_msg1 = random.choice(msg1)

msg2 = ['I can help predict if your loan will get approval.','We can find out if your loan will get approved']
random_msg2 = random.choice(msg2)

msg3 = ['Go ahead,you can ask me how...','Ask me how?','You can ask me how..']
random_msg3 = random.choice(msg3)

firstquestion = ['How?','how','How','HOW','Why','WHY','why','why?']

msg4 = ['Do you want to apply for a loan?','Do you want to request a new loan?','Would you like to test my skills and apply for a loan?']
random_msg4 = random.choice(msg4)

answer1 = ['Yes','yes','Ya','okay','Okay','YES','Alright','alright']
answer2 = ['No','nah','no','nope','no thanks']
answer5 = ['why','why?','Why','Why?','WHY','WHY?']

msg5 = ['Enter your Aadhar number','Please enter your aadhar number','Lets start with your aadhar number']
random_msg5 = random.choice(msg5)

msg6 = ['Please give your PAN number','PAN number','Enter your PAN number','Please enter your PAN number']
random_msg6 = random.choice(msg6)

msg7 = ['What is your CIBIL score?','Enter your CIBIL score: ','Please give your CIBIL score']
random_msg7 = random.choice(msg7)

msg8 = ['Do you own your own home?','Are you a home owner?']
random_msg8 = random.choice(msg8)

answer3 = ['No','no','not yet','Not,yet.','nope','Nope']
answer4 = ['Yes','yes','ya','YEP','yep']

print(random_greeting)
user_input1 = raw_input(">>> ")
print(random_msg1)
print("\n"+random_msg2)
print("\n"+random_msg3)
user_input2 = raw_input(">>> ")

if user_input2 in firstquestion:
	print("I'll take a few details from you such as your Aadhar number, CIBIL score, PAN number and analyse your loan history to predict loan approval or disapproval.")
		
	print("\nWHY CIBIL SCORE?")
	print("\nIt is a three digit numeric summary of your credit history. A CIBIL report has detailed history about the credit you have availed from credit cards, automobile loans to home loans.\n")
	print("\nWHY AADHAR NUMBER AND PAN NUMBER?")
	print("\nIt gives me a better understanding of you as an individual according to your financial history.\n")
			
	
	print("\n"+random_msg4)
	

while True:
		user_input3 = raw_input(">>> ")

		if user_input3 in answer1:
			print("Alright let's get started.")
			print(random_msg5)
			user_input4 = raw_input(">>> ")
			if (not user_input4.isdigit()) or len(user_input4)!=12:
				print("Please enter correct value, has to be 12 digits.")
			else:
				print("Your aadhar number is:"+user_input4+"\n")
	

			print(random_msg6)
			user_input5 = raw_input(">>> ")
			if len(user_input5)!=10:
				print("Please enter the correct PAN number,has to be 10 digits.")
			else:
				print("Your PAN number is:"+user_input5)
			
	
			print(random_msg7)
			user_input6 = raw_input(">>> ")
			if len(user_input6)!=3:
				print("Please enter your correct score.")
			else:
				print("Your score is: "+user_input6)


			print("We're almost done, just need a few personal details.")
			print("\n"+random_msg8)
			user_input7 = raw_input(">>> ")
			if user_input7 in answer3:
				print("Is your home on rent/mortgaged/other")
				user_input8 = raw_input(">>> ")	
			elif user_input7 in answer4:
				flag = 1;
				print("Status: home owner")
			
			print("What is your profession?")
			print("\n 1) Government Job \n 4)Service \n 3)Retired \n 4)Student \n 5)HouseWife/HouseHusband \n 6)Other")
			user_input9 = raw_input(">>> ")
	
			print("What is your Annual Income")
			user_input10 = raw_input(">>> ")
			if not user_input10.isdigit():
				print("Please enter income accurately")
			print("These are the details we have gathered from you.")
			aadhar = user_input4
			pan = user_input5
			cibil = user_input6
			if flag==1:
				homestatus = 'owner'
			else:
				homestatus = user_input8
			profession = user_input9
			annualinc = user_input10

			print("\n"+"Aadhar: "+aadhar) 
			print("\n"+"PAN: "+pan)
			print("\n"+"CIBIL: "+cibil)
			print("\n"+"Hometatus: "+homestatus)
			print("\n"+"Proffession: "+profession)
			print("\n"+"Annual Income: "+annualinc+"\n")

			print("Your details are being analysed and you'll get the result in just a minute...")
			break
			
		elif user_input3 in answer2:
			print("Bye!, have a great day.") 
			break

		else:
			print("I do not understand.")
			
		
		
else:
	print("Bye!, have a great day.")
