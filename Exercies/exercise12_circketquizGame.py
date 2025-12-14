questions = ("1. When India won 2nd ODI World cup?",
             "2. Who is successful caption of Indian Cricket team?",
             "3. Who has bad name in Indian cricket?",
             "4. Who is God of cricket called?",
             "5. Who is Run machine called as?")

options =   (("A. 2011 ", "B. 1983", "C. 2023", "D. 2003 "),
            ("A. MS Dhoni ", "B. kapil Dev", "C. Virat Kohli", "D. Rohit Sharma"),
            ("A. harbhajan ", "B. Gautam", "C. Yuvraj", "D. Ajit"),
            ("A. Dravid", "B. Ganguly ", "C. Kapil", "D. Sachin"),
            ("A. Rohit ", "B. Kohli ", "C. Sachin", "D. Afnan"))

answers = ("A","A","B","D","B")
ans_index = [0,0,1,3,2]

choosen_options = []
counter = 0
Correct_answers = 0

print("Lets play Cricket Quiz Game..!")
for num in questions:     
    print("------------------")
    print(num)
    print("Options: ")
    for i in options[counter]:
        print(i)

    ans = input("Enter your answer ( A, B, C, D): ")
    if(ans == answers[counter]):
        print("Correct answer!")
        Correct_answers += 1
    else:
        print(f"Wrong answer, Correct answer is {options[counter][ans_index[counter]]}")
    choosen_options.append(ans)
    counter += 1


print("================")
print("Correct answers: ", end="")
for i in answers:
    print(i,end=" ")

print()
print("Your answers: ", end="")
for i in choosen_options:
    print(i,end=" ")

print()

print("================")
score = (Correct_answers /len(options)) * 100
print(f"Final Score: {score}")




          