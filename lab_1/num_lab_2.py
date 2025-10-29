print('Введите числа числа в симметричной системе отсчета по основанию 9 через пробел:')
nums = list(map(int, input().split()))
count = len(nums)
for i in range(len(nums)):
    if nums[i] == -4:
        nums[i] = 0
    elif nums[i] == -3:
        nums[i] = 1
    elif nums[i] == -2:
        nums[i] = 2
    elif nums[i] == -1:
        nums[i] = 3
    elif nums[i] == 0:
        nums[i] = 4
    elif nums[i] == 1:
        nums[i] = 5
    elif nums[i] == 2:
        nums[i] = 6
    elif nums[i] ==3:
        nums[i] = 7
    elif nums[i] == 4:
        nums[i] = 8
sum=0
index = count-1
for num in nums:
    sum += num*9**index
    index -= 1
print(sum)