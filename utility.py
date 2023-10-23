
import re
def util_func_1():
    frequency = [
        123, 107, 94, 90, 88, 85, 83, 77, 77, 76, 72, 70, 69, 66, 60, 54, 52, 51, 51, 49, 46, 40, 40, 37, 34, 19 
    ]
    sum = 0
    for num in frequency:
        sum += num * (num - 1)

    sum_of_all = 1710

    result = sum / (sum_of_all * (sum_of_all - 1))
    print(result)

def util_func_2():
    a = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
         0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
         0.01974, 0.00074]
    sum_result = sum(x * x for x in a)
    print(sum_result)

def get_parts(input_str, k):
    result = [''] * k

    for i in range(k):
        result[i] = ''
        for j in range(i, len(input_str), k):
            result[i] += input_str[j]

    return result
def util_func_3():
    file_path = 'text.txt'

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            pattern = '[^a-zA-Z ]'
            replacement = ''

            file_contents = re.sub(pattern, replacement, file_contents).replace(' ', '')
            parts = get_parts(file_contents, 5)

            for part in parts:
                print(part)
                print()

    except IOError as e:
        print('An error occurred while reading the file:', e)



util_func_1()
print()
util_func_2()
print()
util_func_3()