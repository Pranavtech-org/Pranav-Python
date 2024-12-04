#create dictionary and search

D={"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
a=input("enter a month:")
print(D[a])
print("june + july is:",D["june"]+D["july"])
print("december + january + february is:" ,D["december"]+D["february"]+D["january"])


#print all monts with 31 days
#print all monts with 30 days

D={"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
#a=input("Enter the month you want to search for: ")
#print(D[a])
print("June + July is: ",D["June"]+D["July"])
print("December + January + February is: ",D["January"]+D["December"]+D["February"])
for k,v in D.items():
    if v==30:
        print(k,v)
    elif v==31:
        print(k,v)


#display all products cost <1000

product={"milk":100,"bread":200,"flour":999,"water":500,"books":1100,"car":2000}
for k,v in product.items():
    if v>=200 and v<=600:
        print(k,v)


#input a value and remove

D={"milk":100,"bread":200,"flour":999,"water":500,"books":1100,"car":2000}
D.pop("car")
print(D)


#write a program to enter name of employee and their salaries as input and store them  in a disctionary
D=dict()
for i in range(2):
    a=input("enter a employee name:")
    b=input("salary:")
    D[a]=b
    print(D)
x=D.values()
print(x)
print("maximum",max(D.values()))
print("minimum",min(D.values()))




