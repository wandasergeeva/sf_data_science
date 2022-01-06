"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np 
from numpy import random 

def random_predict(number:int = 1) -> int:
    """Функция, которая угадывает рандомное число из 100 
    С каждым кругом цикла мы сокращаем числовой интервал, в котором может оказаться загаданное число, в два раза  
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # переменная счетчик для учета количства попыток
    min_num = 1 # минимальное возможное число
    max_num = 101 # максимальное возможное число

    while True:
        count +=1
        predict_number = (max_num + min_num) // 2 # сокращаем интервал поиска числа в два раза
        if number < predict_number: # если число в первой половине интервала
            max_num = predict_number
        elif number > predict_number: # если число во второй половине интервала поиска
            min_num = predict_number
        else: # если выполнено условие равенства
            break
    return count


def score_game(random_predict) -> int: 
    """Функция, которая возвращает среднее количество попыток отгадать загаданное число, за 1000 подходов
    
    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток отгадать загаданное число
    #np.random.seed(1) # фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1,101, size=1000) 
    
    for number in random_array:
        count_ls.append(random_predict(number)) #добавляем в список значение количества попыток 
    
    score = int(np.mean(count_ls)) # находим среднее значение количества попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
  
    
if __name__ == '__main__': # чтобы код не выполнялся в ноутбуке сразу
    score_game(random_predict)