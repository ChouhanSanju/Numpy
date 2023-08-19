#1.

import numpy as np

# 4D array in the format [month[week[day[min,max]]]]
# Month in the order of Nov,Dec,Jan & Feb.
# Weeks in the oreder of W1,W2,W3 & W4.
# Days in the order of Mon,Tue,Wed,Thu,Fri,Sat & Sun

temp=np.array([[[[6,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],[[7,27],[12,29],[11,29],[-13,23],[15,28],[15,20],[8,32]],[[5,21],[12,18],[-1,12],[12,20],[25,29],[17,22],[12,19]],[[-2,15],[0,12],[2,18],[13,24],[10,16],[12,18],[0,17]]],[[[8,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],[[7,27],[12,29],[11,29],[-15,23],[15,31],[15,30],[8,30]],[[5,21],[12,18],[-12,12],[12,20],[25,27],[17,28],[12,19]],[[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]],[[[9,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],[[7,27],[12,29],[11,29],[15,23],[-13,31],[15,30],[8,30]],[[5,21],[12,18],[-1,12],[12,20],[25,27],[17,28],[12,19]],[[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]],[[[6,23],[14,20],[6,27],[14,22],[8,22],[6,32],[14,29]],[[7,27],[12,29],[11,29],[-13,23],[15,31],[15,30],[8,30]],[[5,21],[12,18],[-1,12],[12,20],[25,27],[17,28],[12,19]],[[-2,15],[0,12],[2,18],[13,24],[10,20],[12,24],[0,17]]]])

month=['November','December','January','February']
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print(temp)


#2.
print("Dimension:-",temp.ndim)
print("Shape:-",temp.shape)


#3.
print(f'# In the format of [month[week 1[day[min,max]]]] :- \n{temp[:,0,:]}')


#4.
print(f'# Temp for tuesday of each month :- \n{temp[:,:,1]}')


#5.
print(f'# Max temp for all the week days of dec and feb :- \n{temp[1:4:2,:,:,1]}')


#6.
print(f'# Formate [week,day]\n# wk1=0,wk2=1,wk3=2,wk4=3\n# mon=0,tue=1,wed=2,thus=3,fri=4,sat=5,sun=6\n{np.where(temp[0,:,:,0]<8)}')


#7.
print('Cross 20 Degrees in Dec & Jan')

for i in [1,2]:
     for j in range(4):
            if np.any(temp[i,j]>20):
                print(f'{month[i]} Week-{j+1}')


#8.
if np.any(temp<0) or np.any(temp>30):
    print('Yes.Absurd value is present.')
else:
    print('No any absurd value.')


#12.
for i in range(1,4):
    mean=[]
    a=np.mean(temp[i],axis=1)
    b=np.mean(a,axis=0)
    mean.append(b[1])
print(f'Average max temperature for the winter month: {np.round(np.mean(mean),2)}')


#13.
b=np.mean(temp[1],axis=1)
c=b.reshape(8)
print('Average minimum temperatures for December in Jaipur :')
print(np.round(c[:8:2],1))


#14.
print(f'Overall avg temp for the months Dec & Jan: {np.round(np.mean(temp[1:3]),2)}')


#15.
for i in range(1,3):
    print(f'Least temperature in {month[i]}- {np.min(temp[i])}')
    min_temp=np.min(temp[i])
    frmt=np.argwhere(temp[i] == min_temp)
    print(f'{day[frmt[0,1]]}\Week-{frmt[0,0]+1}/{month[i]}')


#16.
print(f'Max temperature in Feb - {np.max(temp[3])}')
max_temp=np.max(temp[3])
frmt=np.argwhere(temp[3] == max_temp)
print(f'{day[frmt[0,1]]}/Week-{frmt[0,0]+1}/Feb')


#17.
loc=np.argwhere((temp[0,:,:,1])<(np.mean(temp[0])))
for i in range(loc.shape[0]):
    print(f'Week-{loc[i,0]+1} {day[loc[i,1]]}')


#18.
print(temp.reshape(4,56))


#19.
print(f'Temp data in Fahrenheit:\n{temp*(9/5)+32}')

#20.
avg=np.mean(temp[1],axis=1)
avg2=np.mean(avg,axis=1)
print(f'Dec month average weekly temp in descending order: {np.round(np.sort(avg2)[::-1],1)}')


#21.
temp_3days=temp[:,:,:3]
x=np.mean(temp_3days,axis=2)
y=np.mean(x,axis=1)
z=np.mean(y,axis=1) # calculate 3 days avg weekly temp for each month
ovrall_mean=np.mean(temp[1:4]) # calculate overall avg temp of wintere
base=np.append(z,ovrall_mean)
print(np.sort(base)[::-1])


#22.
diff=(temp[:,:,:,1]-temp[:,:,:,0]).reshape(4,4,7,1)
print('Difference Between temperatures:- \n',diff)


#23.
winter_maxdiff=[]
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,6):
            x=temp[i,j,k+1,1]-temp[i,j,k,1]
            winter_maxdiff.append(x)
print(winter_maxdiff)


#24.
winter_mindiff=[]
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,6):
            x=temp[i,j,k+1,0]-temp[i,j,k,0]
            winter_mindiff.append(x)
print(winter_mindiff)


#25.
array=np.array((winter_maxdiff,winter_mindiff))
array