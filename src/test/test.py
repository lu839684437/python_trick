'''
Created on 2018-9-10

@author: xxlu
'''
from _collections import defaultdict

class My_Print():
    def __repr__(self,):
        return repr('0')
#     def __init__(self,):
#         self.value =0
#     def __str__(self,):
#         return '局部打印'
test  = My_Print()
print(test.__dict__)
test_list = []
test_list.append(test.__dict__)
print(test_list)

#反向遍历
test = [x for x in range(10)]
for _ in reversed(test):
    print(_)
for index,value in enumerate(reversed(test)):
    print(index,value)
test = [2,3,1]
for _ in sorted(test):
    print(_)
for _ in sorted(test,reverse = True):
    print(_)
test = ['nohao','no','haodehen']
for _ in sorted(test,key = len,reverse = True):
    print(_)

def test1(list1):
    for index,value in enumerate(list1):
        if value =='1':
            break
    else:
        return -1 #没有break时候执行，有break时候不再执行
    return index
#计数器方法
test = ['ni','wo','ta','zi','zi']
num_dict ={}
for _ in test:
    num_dict[_] = num_dict.get(_,0)+1
print(num_dict)

num_dict1 = defaultdict(list)
for _ in test:
    num_dict1[len(_)].append(_)
print(num_dict1)

def test2():
    x,y = 0,1
    num = 0
    while num < 100:
        x,y = y,x+y
        num +=1
    print(x,y)
test2()