arr = [16,-2,-5,8,-9,11,23,56,-7,6,12,-1,8,31,78] # массив
sum = 0 #переменная
for i in range(len(arr)): #цикл
    if arr[i] < 0 and i % 3 == 0:#условие1
        sum += arr[i]
print(i)
