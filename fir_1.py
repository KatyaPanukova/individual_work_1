# бинарный поиск через цикл
import time
from random import randint

list_of_nums = []
count_element = int(input('Input quantity of elements :'))
for i in range(count_element):
    list_of_nums.append(randint(-1000, 1000))
list_sorted = sorted(list_of_nums)
print(list_sorted)

desired_num = int(input('Input desired number :'))
n = 0
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

def function(list_sorted,desired_num,a = 0):
    if list_sorted == 0:
        return None
    if list_sorted[0] == desired_num:
        return a
    return function(list_sorted[1:], desired_num, a + 1)
def main():
    start_1 = time.time()
    print('__________________________________')
    print('Index of num {}'.format(desired_num), ':', function(list_sorted,desired_num))
    print('Time of recursive programs work: ', str(time.time()-start_1) + 'sec.')
main()