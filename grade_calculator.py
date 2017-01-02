import math

# Define add method to add a new student
def add():
  
    name = raw_input ("Enter a name: ")
   
    score1 = float(raw_input ("Enter exam 1 score: "))
    score2 = float(raw_input ("Enter exam 2 score: "))
    score3 = float(raw_input ("Enter exam 3 score: "))
    
    if 0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100 and name not in gradeBook:
       gradeBook[name] = [score1, score2, score3]
    else: 
       print ("Invalid Input!")

# Define modify method to modify an existing student's score
def modify():
    
    name = raw_input ("Enter a name: ")
    number = int(raw_input ("Exam number to modify (1, 2, 3): "))
    scoreNew = float(raw_input ("Enter new score for it: "))

    if name in gradeBook and (number == 1 or number == 2 or number == 3) and 0 <= scoreNew <= 100:
        for key in gradeBook.keys():
            if key == name: 
               temp = gradeBook[key]
               temp[number-1] = scoreNew
               gradeBook[key] =  temp   
    else:
        print ("Invalid Input!")

# Define retrieve method for all entries, calculate letter grade, and print
def retrieve():
    total = 0
    totalSquare = 0
    # Calculate the mean and standard deviation of the class population
    for key in gradeBook.keys():
        sum = gradeBook[key][0] + gradeBook[key][1] + gradeBook[key][2]
        gradeBook[key].append(sum)
        total += sum
    mean = total/len(gradeBook)
    for key in gradeBook.keys():
        totalSquare += math.pow(gradeBook[key][3]-mean,2)
    standardDeviation = math.sqrt(totalSquare/len(gradeBook))
    print "Mean: ", mean
    print "Standard Deviation: ", standardDeviation

    # Calculate letter grade and append again
    for key in gradeBook.keys():
        if gradeBook[key][3] >= mean + standardDeviation:
           letterGrade = 'A'
        elif gradeBook[key][3] >= mean:
           letterGrade = 'B'
        elif gradeBook[key][3] >= mean - standardDeviation:
           letterGrade = 'C'
        else:
           letterGrade = 'D'
        gradeBook[key].append(letterGrade)

    # Print out the information of students'
    for key in gradeBook.keys():
        print "Name: ", key, ", Exam 1: ", gradeBook[key][0], ", Exam 2: ", gradeBook[key][1], ", Exam 3: ", gradeBook[key][2], ", Letter Grade: ", gradeBook[key][4] 


gradeBook = {}                           # Initialize the empty gradeBook dictionary


while 1:

    # Options Menu
    option = raw_input("Enter an action (add, retrieve, modify, quit): ")

    if option == "add":
       add()

    elif option == "modify":
       modify()

    elif option == "retrieve":
       retrieve()

    elif option == "quit":
       exit()

    else:
       print ("Invalid Option!")
    

