import os
ftest = open('test.txt', 'w')
for i in range(1,501):
    if i<10:
        name = 'MVI_63521__img' +'0000'+ str(i) + '\n'
    elif i>=10 and i<=99:
        name='MVI_63521__img' +'000'+ str(i)+ '\n'
    else:
        name = 'MVI_63521__img' + '00' + str(i) + '\n'
    ftest.write(name)

ftest.close()

