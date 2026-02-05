"""float(input(..))"""

'''float means integers a built-in function that allows only floats to receive data from the user and run program.'''

marks_math = float(input("enter your math (1-100) marks :"))
marks_sci  = float(input("enter your science (1-100) marks :"))
marks_sst  = float(input("enter your social science(1-100)  marks :"))
marks_eng  = float(input("enter your english (1-100)  marks :"))

total_marks = (marks_math + marks_sci + marks_sst + marks_eng)
print("Your total marks is :", total_marks)

percentage = ((total_marks / 400) * 100 )
print("you percentage is ",percentage)
