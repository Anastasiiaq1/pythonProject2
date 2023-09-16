
def buble_sort(array):
    for j in range(1, len(array)):
        for i in range(1,len(array)):
            if int(array[i-1])>int(array[i]):
                array[i-1],array[i]= array[i],array[i-1]
    return array


def find_position(array,number):
    positions=0
    for i in range(1,len(array)-2):
        if int(array[i]) < int(number) and int(array[i+1])>=int(number):
            positions=i+1
            break
    if positions == 0:
        print('Значения, удовлетворяющего условию, не найдены')
    else:
        print('Позиция элемента, удовлетворяющего условию: ', positions)




try:
    sequence = input('Введите последовательность значений через пробел: ').split(' ')

    for i in sequence:
        if not i.isdigit():
            raise ValueError('Вы ввели некоррентые данные. Водите только целочисленные значения!')



    number = input("Введите число: ")
    if not number.isdigit():
        raise ValueError('Вы ввели некоррентые данные. Водите только целочисленные значения!')


    print('\nВы ввели следующую последовательность значений: ', end=' ')
    for i in sequence:
        print(int(i),end=' ')
    print(f'\nВы ввели следующую число(): {number}',)
except:
    print('error')


print('\nМассив отсортирован: ', *buble_sort(sequence))
find_position(sequence, number)



