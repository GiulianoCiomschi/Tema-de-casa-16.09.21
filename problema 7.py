Zi=["Luni","Marti","Miercuri","Joi","Vineri","Simbata","Duminica"]
Venit=[240,150,160,550,570,900,1500]
#a
print('Venitul săptămânal al întreprinderii este', sum(Venit), 'lei')
#b
print('Media venitului zilnic este', round(sum(Venit)/7,3), 'lei')
#c
x=[]
venit_mare=max(Venit)
for i in range(len(Zi)):
    if Venit[i]==venit_mare:
        x.append(Zi[i])
print("Ziua în care s-a obţinut cel mai mare venit este", x)
#d
y=[]
venit_mic=min(Venit)
for i in range(len(Zi)):
    if Venit[i]==venit_mic:
        y.append(Zi[i])
print("Ziua cu venitul cel mai mic este", y)