num=int(input("enter the number"))
count = 0
i=2
while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
if count==0:
        print("prime")
else:
    print(" not a prime")