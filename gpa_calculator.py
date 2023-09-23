n=int(input("Enter a Number of subject:"))
credit=[]
grade=[]
for i in range(n):
    cre=int(input("Enter subject credit:"))
    gra=input("Enter your subject Grade:")
    credit.append(cre)
    grade.append(gra)

value={
    "o":10,
    "a+":9,
    "a":8,
    "b+":7,
    "b":6,
    "u":0
}

mark=0
for i in range(n):
    mark+=value[grade[i]]*credit[i]

cretot=0
for i in range(n):
    if(grade[i]=="u"):
        credit[i]=0
    cretot+=credit[i]

total=mark/cretot
print("your GPA is",total)