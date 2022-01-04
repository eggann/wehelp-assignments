# 要求一

def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    for x in range(min, max+1):
        sum = sum + x
    print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#------------------------------------------------------------

# 要求二

def avg(data):
    # 請用你的程式補完這個函式的區塊
    for x in data.values():
        continue
    sum = 0
    for y in x:
        sum = sum + y['salary']
    print(sum / (len(y) + 1))
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

#------------------------------------------------------------

# 要求三

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    m = float('-inf')
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            m = max(m, (nums[i]) * (nums[j]))
    print(m)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

#------------------------------------------------------------

# 要求四

def twoSum(nums, target):
    # your code here
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#------------------------------------------------------------

# 要求五
