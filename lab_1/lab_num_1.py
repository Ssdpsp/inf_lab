a=list(map(int,input("введите через пробел цифры числа 9сс").split()))[::-1]
#-4 -3 -2 -1 0 1 2 3 4
#получим число в виде [1, -2, -3, 0, -4]
dec=0
for i in range (len(a)):
    dec+= a[i]*9**i
print(dec)
