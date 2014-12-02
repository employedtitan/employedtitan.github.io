import os


def whatsmyline(character_name):
    
    #setting up necesarry variables and lists
    total_lines = 0
    times_tried = 0
    
    
    #inputing the script
    script = raw_input("what is the file name?: ")
    
    #catch for non-existant file names
    if not os.path.exists(script):
	print("\nSorry that file does not exist")
	print("try another file name")
	
    else:
	Input = open(script)
	
	
	for line in Input:
	    
	    #making the letters lower case and removing the punctuation so the user won't have to memorize the punctuation and the casing
	    line = line.lower()
	    line = line.strip()
	    
	    line = line.translate(None,r",;:()/\'[]{}.<>?-!")
		
		
	    n = 0
	    
	    #determining if the line is the user's character's line
	    if(line[0:len(character_name)] == character_name):
		
		total_lines = total_lines +1
		
		while(n != 1):
		    
		    print("If you wish to quit at any time please enter 1 \n")
		    print("If you would like a hint please enter 2(this will count as missing the line twice) \n")
		    print("If you would like the entire line enter 3(this will count as missing the line four times)\n")
		    
		    your_line = raw_input("Please input your line: ")
		    
		    #if the user gets the line correct
		    if(your_line == line[len(character_name) + 1: len(line)]):
			
			#the +1 removes the space between the characters name and the line
			print("Good job! That is correct \n")
			n = n + 1
			times_tried = times_tried +1
		    
		    
		    #an exit to the program if the user wishes to quit
		    elif(your_line == "1"):
			return -1
		    
		    #entering a 2 will print half the line for a hint
		    elif(your_line == "2"):
			print(line[0:(len(line)/2)])
			times_tried = times_tried + 2
			           
		    #entering a 3 will print the entire line for an even bigger hint
		    elif(your_line == "3"):
			print(line)
			time_tried = times_tried + 4
			
			
		    #if the user gets the line wrong
		    else:
			print("Sorry that is not your line please try again... \n")
			times_tried = times_tried + 1
    
    #catching if the user input a bad character name
    if(times_tried > 0):
	x = get_accuracy(times_tried, total_lines)
    else:
	print("It seems the character you selected does not exist in this script please restart the program and try again \n")
	return -1
    
    #rating the users knowlage of the lines
    if (x <= 56):
	
	print("It appears that your comprehension of your lines is not very good... \n")
	print("You should continue working")
	
    elif (56 < x <= 80):
	
	print("You've done a good job working on your lines!\n")
	print("But you've still got some work to do, keep going!")
	
    elif (80 < x <= 99):
	
	print("You've done an excellent job on your lines, congradulations\n")
	print("You still have a few lines that aren't quite correct, keep up the good work!")
	
    elif(x == 100):
	
	print("Fantastic Job! You got every single line correct!\n")
	print("Keep going over your lines though you don't want to forget!")
	
	
		
    

def whatsmylinewithcue(character_name):
    
    scriptstorage = []
    total_lines = 0
    times_tried = 0
    
    
    script = raw_input("what is the file name?: ")
    
    if not os.path.exists(script):
	
	print("\nSorry that file does not exist")
	print("try another file name \n")
	
    else:
	
	Input = open(script)
	
	
	for line in Input:
	    
	    scriptstorage.append(line)
	    line = line.lower()
	    line = line.strip()
	    line = line.translate(None,r",;:()/\'[]{}.<>?-!")
	    
	    n = 0
	
	    if(line[0:len(character_name)] == character_name):
		total_lines = total_lines +1
		if(len(scriptstorage) < 3):
		    print("You have the first line \n")
		else:
		    print("Your cue line is: \n")
		    print(scriptstorage[(len(scriptstorage) - 3)])
		
		while(n != 1):
		    
		    print("If you wish to quit at any time please enter 1 \n")
		    print("If you would like a hint please enter 2(this will count as missing the line twice) \n")
		    print("If you would like the entire line enter 3(this will count as missing the line four times)\n")
		    
		    
		    your_line = raw_input("Please input your line: ")
		
		    if(your_line == line[len(character_name) + 1: len(line)]):
			
			print("Good job! That is correct \n")
			n = n + 1
			times_tried = times_tried +1
			
		    #an exit to the program if the user wishes to quit
		    elif(your_line == "1"):
			
			return -1
		    
		    #entering a 2 will print half the line for a hint
		    elif(your_line == "2"):
			print(line[0:(len(line)/2)])
			times_tried = times_tried + 2
						       
		    #entering a 3 will print the entire line for an even bigger hint
		    elif(your_line == "3"):
			print(line)
			time_tried = times_tried + 4		    
		    
		    else:
			
			print("Sorry that is not your line please try again... \n")
			times_tried = times_tried + 1
    
    #catching if the user input a bad character name
    if(total_lines > 0):
	x = get_accuracy(times_tried, total_lines)
    else:
	print("It seems the character you selected does not exist in this script please restart the program and try again \n")
	return -1
    
    #rating the users knowlage of the lines
    if (x <= 56):
	   
	print("It appears that your comprehension of your lines is not very good... \ n")
	print("You should continue working")
	   
    elif (56 < x <= 80):
	   
	print("You've done a good job working on your lines!\n")
	print("But you've still got some work to do, keep going!")
	   
    elif (80 < x <= 99):
	   
	print("You've done an excellent job on your lines, congradulations\n")
	print("You still have a few lines that aren't quite correct, keep up the good work!")
	   
    elif(x == 100):
	   
	print("Fantastic Job! You got every single line correct!\n")
	print("Keep going over your lines though you don't want to forget!")
    



    
def displayscript():
    
    script = raw_input("what is the file name?: ")
    
    if not os.path.exists(script):
	
	print("\nSorry that file does not exist")
	print("try another file name \n")
	
    else:
	
	Input = open(script)
	
	
	for line in Input:
	    
	    print(line)



def get_accuracy(times_tried, total_lines):
    
    accuracy = ((times_tried - total_lines)/times_tried) * 100 

def main():
    
    #input for the character name
    character =  raw_input("what is the name of your character?: ")
    #to catch any capitalization errors
    character = character.lower()
    #random number to start the loop
    choice = 0
    
    while(choice != 4):
        print ("------------------------------")
	print ("  1  -  to run through your lines without cues");
	print ("  2  -  to run through your script with cues");
	print ("  3  -  to print the script out");
	print ("  4 -  to exit");
	print ("---------------------------")
	
	choice = input("please enter your choice: ")
	
	if ((1 <= choice) and (choice <= 4)):
	    choice = choice
	    
	else:
	    badinput = choice
	    
	    choice = BAD
	  
	  

	if(choice == 1):
	    
	    
	    whatsmyline(character)
	    
  
	elif(choice == 2):
	    
	    
	    whatsmylinewithcue(character) 
	    
	    
	elif(choice == 3):
	    
	    displayscript()
	    
	elif(choice == 4):
	    
	    print("Thank you for using my program.")
	    
	else:
	    
	    print("Error:", badinput," is not a valid input please try again \n")
	    
	    
if (__name__ == '__main__'):	    
    main()