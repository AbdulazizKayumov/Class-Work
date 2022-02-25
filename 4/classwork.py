year = int(input('Введите год: '))
if year % 400: 
    print('Високосный')
elif year % 100:
    print('Не високосный')    
elif year % 4:
    print('Високосный')
else:
    print('Не високосный')

year = int(input('Введите год: - '))
if year % 400 == 0:
    print('Високосный')
elif year % 4 == 0:
    if year % 100 != 0:
        print('Високосный')    
    else:
      print('Не високосный')    
else:
    print('Не висоосный')          
