import time
from random import randint

list_of_nums = []
count_element = int(input('Input quantity of elements :'))

# создания списка 

for i in range(count_element):
    list_of_nums.append(randint(-1000, 1000))
list_sorted = sorted(list_of_nums)
print(list_sorted)
desired_num = int(input('Input desired number :'))
n = 0

# итеративный способ

def f(count_element,n):
    while count_element != 0:
        if desired_num != list_sorted[n]:
            count_element -= 1
        elif desired_num == list_sorted[n]:
            return n
        n += 1
    else:
        print('None')
# подсчит времени 1
def main_1():
    start = time.time()
    print('Index of num :', f(count_element, n))
    print('Time of iterative programs work:', str(time.time() - start) + ' sec.')
main_1()

a = 0
b = len(list_sorted) - 1

# рекурсивный способ

def function(list_sorted,desired_num, a, b):
    if b < a:
        return None
    else:
        c = (a + b) // 2
        if list_sorted[c] == desired_num:
            return c
        elif list_sorted[c] >= desired_num:
            return function(list_sorted, desired_num, a, c - 1)
        return function(list_sorted, desired_num, c + 1, b)

# подсчит времени 2
def main():
    start_1 = time.time()
    print(function(list_sorted,desired_num, a, b))
    print('Time of recursive programs work:', str(time.time()-start_1) + ' sec.')

main()
