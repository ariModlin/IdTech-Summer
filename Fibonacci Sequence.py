all_nums = []
num = int(input("choose the starting number: "))
second_num = 0
for i in range(50):
    fib_num = num + second_num
    all_nums.append(fib_num)
    num = fib_num
    second_num = all_nums[i-1]
print(all_nums)
