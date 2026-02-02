print("hi my name is bot, what is your name?")
name=input()
print("hi ",name,".")
print("what is your grade?")
grade=int(input())
if(grade=>80):
  print("you got an A")
if(grade>=60 && grade<80):
  print("you got an B")
if(grade>=50 && grade<60):
  print("you got an C")
if(grade<50):
  print("you got an F")
