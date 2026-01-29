print("hi my name is bot, what is your name?")
name=input()
term=[0,3,4,5,7,8,3,20,34]


print("hi ",name," .")
def rand_A(a,c,m,n):
  terms=[0,3,4,5,7,8,3,20,34,42,34]
  return (a*terms[n]+c)/m
i=0
while(i<11):
    
    print("please choose a number to guess")
    x=int(input())
    random=int(rand_A(0.5+(i*i),1.5/(i+1),2*(i+1),i))
    if (x<random):
      print("guess higher")
    
    if (x>random):
      print("guess lower")
    if(x==random):
        print("correct guess")
    print(random)  
    i=i+1
