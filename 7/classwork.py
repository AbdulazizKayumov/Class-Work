# Loop - цикл

# 2 вида циклов:
# while
# for

for i in range(20):
    print(i, end=' ')


# range(stop) -> [0; stop)
# range(start, stop) -> [start; stop)
# range(start, stop, step)   

for i in range(200, 99, -2):
    print(i)

for i in range(1, 11):
    print(f'9 x {i} = (9 * 1)')

def print_mult_table(num, from_num, up_to):
    for i in range(from_num, up_to + 1):
        print(f'{num} x {1} = {num + 1}')

def print_exp_table(num, from_num, up_to):
    for i in range(from_num, up_to + 1):
        print(f'{num}  {i} = {num}')

print_exp_table(44, 7, 13)


for i in range(5, 10):
    print(i / 10)


for letter in 'Aziza':
    print(letter, end=' ')


print('Abdulaziz'.upper())
print('ABDULAZIZ'.lower())
print('A'.isupper())
print('ABdulaziz'.upper().isupper())
print('123.isdigit')

for letter in 'Abdulaziz Kayumov is a boy':
    new_str = ''
    for letter in 'abdulaziz Kayumov is a boy':
        new_str = new_str + letter.swapcase()
    
print(new_str)