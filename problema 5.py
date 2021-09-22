#Exercitiul 5
x=[2,4,-5,8,10]
y=x
#a
print(x[0]+x[1]+x[2])
#b
print(sum(y))
#c
p=1
for i in range(0,len(x)):
    p=p*x[i]
print(p)
#d
print(abs(x[2]))
#e
print(x[0]+y[0])