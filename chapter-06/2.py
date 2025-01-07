#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter the subject1 marks: "))
marks2 = int(input("Enter the subject2 marks: "))
marks3 = int(input("Enter the subject3 marks: "))

each_percent1 = marks1
each_percent2 = marks2
each_percent3 = marks3
total_percent = ((marks1+marks2+marks3)/300)*100

if(each_percent1>=33 and each_percent2>=33 and each_percent3>=33 and total_percent>40):
    print("Congratulations you are passed!!!🎉")
else:
    print("Sorry you are failed!!!🥲")
    
