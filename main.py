arr = [16,-2,-5,8,-9,11,23,56,-7,6,12,-1,8,31,78] # массив
sum = 0 #переменная1
for i in range(len(arr)):
    if arr[i] < 0 and i % 3 == 0:
        sum += arr[i]
print(i)
