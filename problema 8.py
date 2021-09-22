ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[-2,-5,-6,-3,0,3,6,7,11,10,10,11,13,13,14,12,11,10,8,6,3,0,-1,-2]
#a
print('Temperatura medie este',round(sum(t)/24,2),'grade Celsius')
#b
max_temp=max(t)
min_temp=min(t)
print("Maximul si minimul temperaturii este", max_temp,'si', min_temp,'grade Celsius')
#c
x=[]
for i in range(len(ora)):
    if t[i]==max_temp:
        x.extend([i])
print("Ora la care s-a înregistrat temperatura maximă este",x)
#d            
y=[]
for i in range(len(ora)):
    if t[i]==min_temp:
        y.append(ora[i])
print("Ora la care s-a înregistrat temperatura minimă este",y)

