# coding=utf-8

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


if __name__ == '__main__':
    x = int(input('请输入x的值'))
    y = int(input('请输入y的值'))
    result = gcd(x, y)
    print result
