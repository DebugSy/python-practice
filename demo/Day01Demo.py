#coding=utf-8


def sum():
    sum = 0
    for x in range(101):
        sum += x
        if sum == 30:
            print ("sum is 30")
    print sum

def find_shui_xian_hua():
    nums = range(100, 1000)
    for x in nums:
        if (x%10)**3 + (x//10%10)**3 + (x//100)**3 == x:
            print x

if __name__ == '__main__':
    find_shui_xian_hua()