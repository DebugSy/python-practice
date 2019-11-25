# encoding=utf-8

"""
列表的操作
"""


# 列表访问
def listPrint():
    list2 = 'hello ' * 3
    print list2
    print list1[0]
    print list1[4]
    print list1[-1]
    print list1[-2]
    list1[2] = 300
    print list1

    for index in range(len(list1)):
        print list1[index]

    for element in list1:
        print element

    enumer = enumerate(list1)
    for (index, element) in enumer:
        print (index, element)


# 列表操作
def crud():
    list1.append(200)
    print list1

    list1.insert(1, 400)
    print list1


# 排序
def sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)  # 按字母顺序排序
    print list2
    list3 = sorted(list1, reverse=True)
    print list3
    list4 = sorted(list1, key=len)
    print list4

    list5 = list1.sort(reverse=True)
    print list5  # None
    print list1


# 生成式与生成器
def gen():
    f = [x for x in range(1, 10)]
    print f
    f = [x + y for x in 'ABCDE' for y in '1234567'] # 生成式基础语句结构：[exp for iter_var in iterable例如：a=[f(x) for x in range(10)]
    print f
    f = [x ** 2 for x in range(1, 1000)]
    print f
    import sys
    print(sys.getsizeof(f))

    f = (x ** 2 for x in range(1, 1000))  # 这里创建的是一个生成器对象，不是列表。是用（）引起的
    print sys.getsizeof(f)
    print f


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, 100]
    print (list1)

    result = fib(20)
    for s in result:
        print s
