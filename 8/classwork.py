# ? task 1 
def draw_tree(size):
    if size <3:
        print('error')
    else:
        for i in range(1, size + 1 ):
            print("*" * i)
draw_tree(1)

# ? task 2

# def draw_box(widh, height):
#     for i in range(height):
#         print('*' * widh )
# draw_box(2,10)



# ? task 3
# def clear_text_from_uppercase(text):
#     new_text = ''
#     for letter in text:
#         if letter. isupper():pass
#         else: new_text = new_text + letter
#     return new_text
# print(clear_text_from_uppercase('dsjdbcbBHbHBHBHBHjjjJJBBHBhbhbhbhbHBHBHBHBHBHbhbHGFFFGhhhnnn'))


# ? task 4

# def show_devisior(num):
#     for i in range(1, num+1):
#         if num % i == 0:
#             print(i)
#         # else:
#             # pass

# print(show_devisior(24))

# def f(x):
    # return x * x + x + 3
# print(f(2))