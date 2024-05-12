''' Игра Угадай число
Компьютер сам загадывает и угадывает числа
'''


import numpy as np


def random_predict(number:int=1) -> int:
    """Угадываем число случайным образом

    Args:
        number (int, optional): Загаданное число. По умолчанию, равно 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if predict_number == number:
            break
    return(count)

def score_game(random_predict) -> int:
    """За какое колиечество попыток алгоритм в среднем из 1000 подходов угадывает число

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] #список для сохранения числа попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # формируем 1000 случайных чисел
    for number in random_array:
        
        count_ls.append(random_predict(number))
        
    print(count_ls[:20])
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score

if __name__ == '__main__':
    score_game(random_predict)
    # RUN
