import time
from random import randint

list_of_nums = []
count_element = int(input('Input quantity of elements :'))

for i in range(count_element):
    list_of_nums.append(randint(-100000, 100000))
list_sorted = sorted(list_of_nums)
desired_num = int(input('Input desired number :'))
n = 0
# бинарный поиск через цикл
while count_element != 0:
    start = time.time()
    if desired_num != list_sorted[n]:
        count_element -= 1
    elif desired_num == list_sorted[n]:
        print('Index of num {}'.format(desired_num), ':', n)
        print('Time of iterative programs work: ', str(time.time()-start) + 'sec.')
        break
    n += 1
else:
    print('None')
# бинарный поиск через рекурсию

a = list_sorted[0]
b = list_sorted[-1]


def function(list_sorted,desired_num, a, b):
    if b >= a:
        c = a + (b - a) // 2
        if list_sorted[c] == desired_num:
            return c
        elif list_sorted[c] > desired_num:
            return function(list_sorted, desired_num, a, c - 1)
        return function(list_sorted, desired_num, c + 1, b)
    return None


def main():
    start_1 = time.time()

    if function(list_sorted, desired_num,  0, len(list_sorted) - 1) == None:

        print('__________________________________')
        print(function(list_sorted, 0, len(list_sorted) - 1, desired_num))
    else:
        print('__________________________________')
        print('Index of num {}'.format(desired_num), ':', function(list_sorted, desired_num,  0, len(list_sorted) - 1))
        print('Time of recursive programs work: ', str(time.time()-start_1) + 'sec.')
try:
    main()
except MemoryError:
    print('Limit is exceeded!')
except IndexError:
    print('__________________________________')
    print('None')
