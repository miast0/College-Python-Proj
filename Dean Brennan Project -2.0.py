# Dean Brennan
# Python Project
# Test Creator

# Importing the random number generator
import random

# A list is set to the different opperators as to make defining them easier
OPERATORS = ["+", "-", "x", "÷"]
# All variables that will be calld upon later are stored here
OUTPUT_QUESTOINS = ""
OUTPUT_ANSWERS = ""  #

# These variables define the name and amount of questions
questionsLoop = True
while questionsLoop == True:
    questionsLoop = False
    class_name = input("What is the class?:\t")
    person_name = input("What is your name?:\t")
    num_Q = int(input("How many questions?:\t"))
# This choice selects the operator type as 1): Random operators, 2): Specific operators
choice = input("Please select what operators you would like: 1 or 2.\n-------------\n1:Random\n2:Specific\n>>>\t")
# if statement to ensure choice is either one or two
if choice == "1":

    print("Thank you,\n A questions and answers file has been created under ", class_name)
    for i in range(1, (num_Q + 1)):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        divis_Num = random.randint(1, 120)
        # The operator that will be used is randomly selected from the list. This allows for true random questions
        operator_type = OPERATORS[random.randint(0, 3)]
        if operator_type == "+":
            # if the randomly selected operator is +, the following program adds the 2 previously defined random numbers and adds them for a result
            # Afterwards 2 text files are created: answers and questions text files
            result = num1 + num2
            OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
            OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                result) + "\n"
            # Creation of questions text file
            file_questions = open(class_name + " Questions.txt", 'w')
            file_questions.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
            file_questions.close()
            # Creation of answers text file
            file_answers = open(class_name + " Answers.txt", 'w')
            file_answers.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
            file_answers.close()
        elif operator_type == "-":
            # Loop to ensure that the first number is greater than the small number
            subtract_loop = True
            while subtract_loop == True:
                subtract_loop = False
                if num1 >= num2:
                    result = num1 - num2
                    OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
                    OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                        result) + "\n"
                    file_questions = open(class_name + " Questions.txt", 'w')
                    file_questions.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
                    file_questions.close()
                    file_answers = open(class_name + " Answers.txt", 'w')
                    file_answers.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
                    file_answers.close()
                else:
                    num2 = random.randint(1, 12)
                    subtract_loop = True
        elif operator_type == "x":
            result = num1 * num2
            OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
            OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                result) + "\n"
            file_questions = open(class_name + " Questions.txt", 'w')
            file_questions.write(
                "Teacher:\t" + person_name + "\n Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
            file_questions.close()
            file_answers = open(class_name + " Answers.txt", 'w')
            file_answers.write(
                "Teacher:\t" + person_name + "\n Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
            file_answers.close()
        elif operator_type == "÷":
            # Divison loop to ensure that the divisor is smaller than and true to the numerator
            division_loop = True
            while division_loop == True:
                division_loop = False
                if num1 % num2 == 0:
                    result = num1 / num2
                    OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
                    OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                        result) + "\n"
                    file_questions = open(class_name + " Questions.txt", 'w')
                    file_questions.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
                    file_questions.close()
                    file_answers = open(class_name + " Answers.txt", 'w')
                    file_answers.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
                    file_answers.close()

                else:
                    num1 = random.randint(1, 120)
                    division_loop = True
if choice == "2":
    operator_choice = (input("What operators?\t'+'\t '-'\t 'x'\t '/'\n>>>\t"))
    print("Thank you,\n A questions and answers file has been created under ", class_name)
    for i in range(1, (num_Q + 1)):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        divis_Num = random.randint(1, 120)
        if operator_choice == "+":
            # The operator type is set to the OPERATOR list value of 0, aka addition
            operator_type = OPERATORS[0]
            result = num1 + num2
            OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
            OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                result) + "\n"
            file_questions = open(class_name + " Questions.txt", 'w')
            file_questions.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
            file_questions.close()
            file_answers = open(class_name + " Answers.txt", 'w')
            file_answers.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
            file_answers.close()
        elif operator_choice == "-":
            operator_type = OPERATORS[1]
            subtract_loop = True
            # This loop ensures that the subtraction stays positive, if not it retries
            while subtract_loop == True:
                subtract_loop = False
                if num1 >= num2:
                    result = num1 - num2
                    OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
                    OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                        result) + "\n"
                    file_questions = open(class_name + " Questions.txt", 'w')
                    file_questions.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
                    file_questions.close()
                    file_answers = open(class_name + " Answers.txt", 'w')
                    file_answers.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
                    file_answers.close()

                else:
                    num2 = random.randint(1, 12)
                    subtract_loop = True
        elif operator_choice == "x":
            operator_type = OPERATORS[2]
            result = num1 * num2
            OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
            OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                result) + "\n"
            file_questions = open(class_name + " Questions.txt", 'w')
            file_questions.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
            file_questions.close()
            file_answers = open(class_name + " Answers.txt", 'w')
            file_answers.write(
                "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
            file_answers.close()

        elif operator_choice == "/":
            operator_type = OPERATORS[3]
            division_loop = True
            # This is a loop in order to make sure that the divisor is always smaller than, and true to the numerator
            while division_loop == True:
                division_loop = False
                if num1 % num2 == 0:
                    result = num1 / num2
                    OUTPUT_QUESTOINS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t_____" + "\n"
                    OUTPUT_ANSWERS += "Q" + str(i) + "\t" + str(num1) + operator_type + str(num2) + "\t = \t" + str(
                        result) + "\n"
                    file_questions = open(class_name + " Questions.txt", 'w')
                    file_questions.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_QUESTOINS)
                    file_questions.close()
                    file_answers = open(class_name + " Answers.txt", 'w')
                    file_answers.write(
                        "Teacher:\t" + person_name + "\n" + "Class:\t"+class_name+"\n"+ "Maths Test"+ "\n==========================\n" + OUTPUT_ANSWERS)
                    file_answers.close()


                else:
                    num1 = random.randint(1, 120)
                    division_loop = True