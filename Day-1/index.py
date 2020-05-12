# Collatz Sequesnce

def Collatz(number):
    if number == 1:
        return 1 
    elif number%2==0:
        number=number//2
        print(number)
        Collatz(number)
    elif number%2==1:
        number=3*number+1
        print(number)
        Collatz(number)


type_num=input()

try:
    Collatz(int(type_num))
except ValueError:
    print("Use an Integer")
        


    





