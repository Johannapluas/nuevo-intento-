# palabra reselvada continue (salte hacia el siglo for)
# y no se ejecute lo que esta adebajo del continue
j= 0 

for i in range (10):
    j += 2
    print('i:', i ,'j:',j )
    if j >= 2 and j<=18:
     continue
    print('el valor de j:', j )
