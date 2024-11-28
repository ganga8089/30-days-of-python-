n=int(input("Enter a number:"))
list=["apple","banana","orange","mango","grapes","pineapple"]
result=[]
for i in list:
    lenght=len(i)
    if lenght>n:
        result.append(i)
print("words longer than",n,"are:",result)

