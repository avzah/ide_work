import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0 # количество попыток

while True:
    count += 1
    predict_number = int(input('Какое число загадано от 1 до 100? Введите сюда: '))
    
    if predict_number > number:
        print('Ваше число больше искомого! Попробуйте ещё!')
        
    elif predict_number < number:
        print('Ваше число меньше искомого! Попробуйте ещё!')
        
    else:
        print(f'Вы угадали число {number}  за {count} попыток')
        break
    
    