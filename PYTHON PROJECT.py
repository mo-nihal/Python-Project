import pyfiglet
import os
import time


def game():
    os.system('cls')
    os.system('color e')

    test_banner="QUIZ GAME"
    test_banner=pyfiglet.figlet_format(test_banner)
    print(test_banner)
    print(
"""1) HISTORY
2) SCIENCE
3) PYTHON
4) C PROGRAMMING
5) TECHNOLOGY """)
    res = int(input("SELECT THE SET OF QUESTIONS YOU WANT (1,2,3,4,5) : "))

    # set 1
    def set1():
        os.system("cls")
        test_banner = "HISTORY"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        
        questions = ["Who was the first President of the United States? ",
                     "What year did the Titanic sink?  ",
                     "Which ancient civilization built the pyramids? ",
                     "Who wrote the Declaration of Independence? ",
                     "What was the primary cause of World War I?",
                     "Which empire was ruled by Genghis Khan? ",
                     "What was the name of the ship that carried the Pilgrims to America? ",
                     "Who was the British Prime Minister during World War II? ",
                     "Which event sparked the beginning of the French Revolution? ",
                     "What was the main purpose of the Berlin Wall? "]

        answers = ["B",
                   "B",
                   "C",
                   "C",
                   "D",
                   "C",
                   "A",
                   "A",
                   "A",
                   "B"]

        options = [["A) Thomas Jefferson","B) George Washington","C) Abraham Lincoln","D) John Adam"],
                   ["A) 1905","B) 1912","C) 1920","D) 1930"],
                   ["A) Romans","B) Greeks","C) Egyptians","D) Mayans"],
                   ["A) Benjamin Franklin","B) John Adams","C) Thomas Jefferson","D) James Madison"],
                   ["A) Economic depression","B) Imperialism","C) Nationalism","D) All of the above"],
                   ["A) Roman Empire","B) Ottoman Empire","C) Mongol Empire","D) Byzantine Empire"],
                   ["A) Mayflower","B) Santa Maria","C) Nina","D) Pinta"],
                   ["A) Winston Churchill","B) Neville Chamberlain","C) Clement Attlee","D) Tony Blair"],
                   ["A) The Storming of the Bastille","B) The Reign of Terror","C) The signing of the Magna Carta","D) The execution of Louis XVI"],
                   ["A) To protect against invasion","B) To separate East and West Berlin","C) To promote tourism","D) To commemorate WWII"]]
        score =[]
        temp = 0        
                
        
        def Check_answer(ans,i):
            if ans.upper() == 'A':
                pass
            elif ans.upper() == 'B':
                pass
            elif ans.upper() == 'C':
                pass
            elif ans.upper() == 'D':
                pass
            else:
                print(f"{ans.upper()} IS NOT AN OPTION")

                
            if len(ans.upper()) != 1 :
                print(f"{ans.upper()} is not there in options")
            if ans.upper() == answers[i]:
                score.append(1)
                return "CORRECT ANSWER"
            else:
                return "INCORRECT ANSWER"

                

            
        for i in range(len(questions)):
            print("                        ")       
            print(f"Q{i+1}) {questions[i]}")
            for j in range(len(options[i])):
                print(options[i][j])
            ans = input("ANSWER (A,B,C,D): ")
            res = Check_answer(ans,i)
            print(res)
            time.sleep(2)

        for i in range(len(score)):
            temp += 1


        percentage = int(temp/len(questions) * 100)
        print("""

        """)
        os.system('cls')
        congra = "Congratulation"
        congra = pyfiglet.figlet_format(congra)
        print(congra)
        print(f"YOU GOT {percentage}% of mark")
        time.sleep(5)




    # set2
    def set2():
        os.system("cls")
        test_banner = "SCIENCE"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        
        questions = ["What is the chemical symbol for gold? ",
                     "Which planet is known as the \"Red Planet\"?  ",
                     "What is the powerhouse of the cell?  ",
                     "What gas do plants absorb from the atmosphere during photosynthesis? ",
                     "What is the most abundant gas in the Earth's atmosphere? ",
                     "Which part of the brain is responsible for regulating balance and coordination? ",
                     "What is the main component of the sun? ",
                     "What type of bond involves the sharing of electron pairs between atoms? ",
                     "Which element has the highest atomic number that occurs naturally?  ",
                     "What is the process by which a liquid turns into a gas?  "]

        answers = ["A",
                   "B",
                   "C",
                   "B",
                   "C",
                   "B",
                   "C",
                   "C",
                   "A",
                   "B"]

        options = [["A) Au",
    "B) Ag",
    "C) Pb",
    "D) Fe"],
                   ["A) Venus",
    "B) Mars",
    "C) Jupiter",
    "D) Saturn"],
                   ["A) Nucleus",
    "B) Ribosome",
    "C) Mitochondria",
    "D) Endoplasmic reticulum"],
                   ["A) Oxygen",
    "B) Carbon Dioxide",
    "C) Nitrogen",
    "D) Hydrogen"],
                   ["A) Oxygen",
    "B) Carbon Dioxide",
    "C) Nitrogen",
    "D) Argon"],
                   ["A) Cerebrum",
    "B) Cerebellum",
    "C) Brainstem",
    "D) Hypothalamus"],
                   ["A) Helium",
    "B) Oxygen",
    "C) Hydrogen",
    "D) Carbon"],
                   ["A) Ionic bond",
    "B) Hydrogen bond",
    "C) Covalent bond",
    "D) Metallic bond"],
                   ["A) Uranium",
    "B) Plutonium",
    "C) Gold",
    "D) Francium"],
                   ["A) Condensation",
    "B) Evaporation",
    "C) Sublimation",
    "D) Precipitation"]]
        score =[]
        temp = 0        
                
        
        def Check_answer(ans,i):
            if ans.upper() == 'A':
                pass
            elif ans.upper() == 'B':
                pass
            elif ans.upper() == 'C':
                pass
            elif ans.upper() == 'D':
                pass
            else:
                print(f"{ans.upper()} IS NOT AN OPTION")


                
            if len(ans.upper()) != 1 :
                print(f"{ans.upper()} is not there in options")
            if ans.upper() == answers[i]:
                score.append(1)
                return "CORRECT ANSWER"
            else:
                return "INCORRECT ANSWER"
                

            
        for i in range(len(questions)):
            print("                        ")       
            print(f"Q{i+1}) {questions[i]}")
            for j in range(len(options[i])):
                print(options[i][j])
            ans = input("ANSWER (A,B,C,D): ")
            res = Check_answer(ans,i)
            print(res)
            time.sleep(2)

        for i in range(len(score)):
            temp += 1


        percentage = int(temp/len(questions) * 100)
        print("""

        """)
        os.system('cls')
        congra = "Congratulation"
        congra = pyfiglet.figlet_format(congra)
        print(congra)
        print(f"YOU GOT {percentage}% of mark")
        time.sleep(5)

    # set3
    def set3():
        os.system("cls")
        test_banner = "PYTHON"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        
        questions = ["What is the output of the following code? \n       print(type([]) == list)",
                     "Which of the following is the correct way to define a function in Python? ",
                     "What is the output of len(\"Hello World\")? ",
                     "Which of the following data types is immutable? ",
                     "What will be the output of the following code? \n          print(3 * 'ab')",
                     "Which of the following is used to create a comment in Python? ",
                     "What will be the output of the following code? \n          x = [1, 2, 3]\n          print(x * 2)",
                     "Which of the following is a mutable data type in Python? ",
                     "What is the purpose of the self keyword in Python? ",
                     "Which of the following statements will create a dictionary in Python? "]

        answers = ["A",
                   "C",
                   "B",
                   "D",
                   "C",
                   "C",
                   "B",
                   "C",
                   "A",
                   "A"]

        options = [["A) True","B) False","C) None","D) Error"],
                   ["A) function myFunc():","B) def myFunc[]:","C) def myFunc():","D) define myFunc():"],
                   ["A) 10","B) 11","C) 12","D) 13"],
                   ["A) List","B) Dictionary","C) Set","D) Tuple"],
                   ["A) abab","B) ab3","C) ababab","D) Error"],
                   ["A) // This is a comment","B) /* This is a comment */","C) # This is a comment","D) <!-- This is a comment -->"],
                   ["A) [1, 2, 3, 2]","B) [1, 2, 3, 1, 2, 3]","C) [2, 4, 6]","D) Error"],
                   ["A) String","B) Tuple","C) List","D) All of the above"],
                   ["A) It refers to the current instance of the class.","B) It refers to the parent class.","C) It is used to define a variable.","D) It is used to create a new class."],
                   ["A) my_dict = {1: \"one\", 2: \"two\"}","B) my_dict = (1, \"one\", 2, \"two\")","C) my_dict = [1, \"one\", 2, \"two\"]","D) my_dict = \"1: one, 2: two\""]]
        score =[]
        temp = 0        
                
        
        def Check_answer(ans,i):
            if ans.upper() == 'A':
                pass
            elif ans.upper() == 'B':
                pass
            elif ans.upper() == 'C':
                pass
            elif ans.upper() == 'D':
                pass
            else:
                print(f"{ans.upper()} IS NOT AN OPTION")

                
            if len(ans.upper()) != 1 :
                print(f"{ans.upper()} is not there in options")
            if ans.upper() == answers[i]:
                score.append(1)
                return "CORRECT ANSWER"
            else:
                return "INCORRECT ANSWER"
                

            
        for i in range(len(questions)):
            print("                        ")       
            print(f"Q{i+1}) {questions[i]}")
            for j in range(len(options[i])):
                print(options[i][j])
            ans = input("ANSWER (A,B,C,D): ")
            res = Check_answer(ans,i)
            print(res)
            time.sleep(2)

        for i in range(len(score)):
            temp += 1


        percentage = int(temp/len(questions) * 100)
        print("""

        """)
        os.system('cls')
        congra = "Congratulation"
        congra = pyfiglet.figlet_format(congra)
        print(congra)
        print(f"YOU GOT {percentage}% of mark")
        time.sleep(5)

    # set4
    def set4():
        os.system("cls")
        test_banner = "C PROGRAMMING"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        
        questions = ["What is the size of int in C? ",
                     "Which of the following is a valid identifier in C? ",
                     "Which of the following is a logical operator in C? ",
                     "What is the purpose of the break statement in C? ",
                     "Which of the following is not a valid data type in C? ",
                     "What is the correct way to declare a constant in C? ",
                     "Which of the following is used for multi-line comments in C? ",
                     "Which of the following is a correct way to declare a function in C? ",
                     "Which of the following is used to allocate memory dynamically in C? ",
                     "Which of the following is a valid way to declare an array in C? "]

        answers = ["D",
                   "B",
                   "D",
                   "A",
                   "C",
                   "C",
                   "B",
                   "A",
                   "A",
                   "A"]

        options = [["A) 1 byte","B) 2 bytes","C) 4 bytes","D) It depends on the compiler"],
                   ["A) 2ndValue","B) second_value","C) second-value","D) second value"],
                   ["A) &&","B) ||","C) !","D) All of the above"],
                   ["A) To exit a loop","B) To terminate a program","C) To skip an iteration","D) To declare a variable"],
                   ["A) int","B) float","C) decimal","D) char"],
                   ["A) const int x = 10;","B) int const x = 10;","C) Both A and B","D) constant int x = 10;"],
                   ["A) // comment","B) /* comment */","C) # comment","D) <!-- comment -->"],
                   ["A) void functionName() {}","B) functionName() void {}","C) void functionName;","D) functionName void() {}"],
                   ["A) malloc()","B) calloc()","C) free()","D) calloc()"],
                   ["A) int arr[10];","B) int arr;","C) array int[10];","D) int[10] arr;"]]
        score =[]
        temp = 0        
                
        
        def Check_answer(ans,i):
            if ans.upper() == 'A':
                pass
            elif ans.upper() == 'B':
                pass
            elif ans.upper() == 'C':
                pass
            elif ans.upper() == 'D':
                pass
            else:
                print(f"{ans.upper()} IS NOT AN OPTION")
            
            if len(ans.upper()) != 1 :
                print(f"{ans.upper()} is not there in options")
            if ans.upper() == answers[i]:
                score.append(1)
                return "CORRECT ANSWER"
            else:
                return "INCORRECT ANSWER"
                

            
        for i in range(len(questions)):
            print("                        ")       
            print(f"Q{i+1}) {questions[i]}")
            for j in range(len(options[i])):
                print(options[i][j])
            ans = input("ANSWER (A,B,C,D): ")
            res = Check_answer(ans,i)
            print(res)
            time.sleep(2)

        for i in range(len(score)):
            temp += 1


        percentage = int(temp/len(questions) * 100)
        print("""

        """)
        os.system('cls')
        congra = "Congratulation"
        congra = pyfiglet.figlet_format(congra)
        print(congra)
        print(f"YOU GOT {percentage}% of mark")
        time.sleep(5)
   
    #set 5
    def set5():
        os.system("cls")
        test_banner = "TECHNOLOGY"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        
        questions = ["What does HTML stand for?",
                     "Who is the co-founder of Microsoft? ",
                     "What year was the first iPhone released? ",
                     "Which programming language is known for its snake logo? ",
                     "What does the acronym “Wi-Fi” stand for?",
                     "Which company developed the first commercial smartphone? ",
                     "What is the main function of a CPU in a computer?",
                     "Which company developed the first computer mouse?",
                     "What does the acronym “USB” stand for? ",
                     "What is the name of the virtual assistant developed by Amazon? "]

        answers = ["A",
                   "B",
                   "B",
                   "B",
                   "A",
                   "B",
                   "C",
                   "C",
                   "B",
                   "C"]

        options = [["A) HyperText Markup Language","B) Hyperlink Text Markup Language","C) Hyper Tool Markup Language","D) Hyper Transfer Markup Language"],
                   ["A) Steve Jobs:","B) Bill Gates","C) Jeff Bezos","D) Elon Musk"],
                   ["A) 2005","B) 2007","C) 2009 ","D) 2010"],
                   ["A) Java","B) Python","C) Ruby","D) C++"],
                   ["A) Wireless Fidelity","B) Wireless Frequency","C) Wireless Frequency","D) None of the above"],
                   ["A) Apple","B) IBM","C) Nokia","D) Samsung"],
                   ["A) Store data","B) Execute Instructions","C) Display graphics","D) Connect to the internet"],
                   ["A) IBM","B) Microsoft","C) Xerox","D) Apple"],
                   ["A) Universal Storage Bus","B) Universal Serial Bus","C) Universal System Bus","D) Unified Storage Bus"],
                   ["A) Siri ","B) Cortana","C) Alexa","D) Google Assistant"]]
        score =[]
        temp = 0        
                
        
        def Check_answer(ans,i):
            if ans.upper() == 'A':
                pass
            elif ans.upper() == 'B':
                pass
            elif ans.upper() == 'C':
                pass
            elif ans.upper() == 'D':
                pass
            else:
                print(f"{ans.upper()} IS NOT AN OPTION")

                
            if len(ans.upper()) != 1 :
                print(f"{ans.upper()} is not there in options")
            if ans.upper() == answers[i]:
                score.append(1)
                return "CORRECT ANSWER"
            else:
                return "INCORRECT ANSWER"
                

            
        for i in range(len(questions)):
            print("                        ")       
            print(f"Q{i+1}) {questions[i]}")
            for j in range(len(options[i])):
                print(options[i][j])
            ans = input("ANSWER (A,B,C,D): ")
            res = Check_answer(ans,i)
            print(res)
            time.sleep(2)

        for i in range(len(score)):
            temp += 1


        percentage = int(temp/len(questions) * 100)
        print("""

        """)
        os.system('cls')
        congra = "Congratulation"
        congra = pyfiglet.figlet_format(congra)
        print(congra)
        print(f"YOU GOT {percentage}% of mark")
        time.sleep(5)



    # response for sets from user
   
    if res == 1:
        set1()
    elif res == 2:
        set2()
    elif res == 3:
        set3()
    elif res == 4:
        set4()
    elif res == 5:
        set5()


    new_game = input("DO YOU WANT TO PLAY QUIZ AGAIN  (YES/NO):  ")
    if new_game.upper() == "YES":
        game()
    else:
        os.system('cls')
        test_banner="THANK YOU!!!!"
        test_banner=pyfiglet.figlet_format(test_banner)
        print(test_banner)
        time.sleep(5)
game()    

    
    
