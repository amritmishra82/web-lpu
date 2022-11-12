#defining  function
def pr():
    print("Hii I am a user defined function pr")
pr() #calling of a function


#Parametrised function, function capable of accepting value
def pr(name):
    print("Hii my name is " +name)
pr("Amrit")


def pr(first_name, last_name):
    print("Hii my name is "+first_name+" " +last_name)
pr("Amrit","Mishra")


def pr(name1, name2, name3):
    print("My name is "+name3)
pr(name1 ="Amrit", name2 ="Mishra", name3 ="LPU")


def pr(name):
    for i in name:
        print(i)
name = ["Amrit", "Mishra", "LPU"]
pr(name)


 #return
def pr(n):
   return n*5
print(pr(5))


#recursion function calls itself to perform a task
def factorial(x):
    if x==1:
        return 1
    else:
        return (x * factorial(x-1))
factorial(4)
print(factorial(4)