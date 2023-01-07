n = int(input("How many Emails you wants to Slice: "))
z = []
for i in range (1,n+1):
    n = str(input("\nEmail: "))
    z.append(n)
for i in z:
    m = i.split("@")
    print(f'\nUsername: {m[0]} and domain: {m[1]}')