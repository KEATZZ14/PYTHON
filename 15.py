upper_limit=int(input("enter the upper_limit:"))
lower_limit=int(input("enter the lower_limit:"))
for i in range(upper_limit+1,lower_limit):
    if(i%2==0):
        print(i)
