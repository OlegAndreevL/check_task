import numpy as np
def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    mn, mx = 1, 100
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    while predict_number != number:
        count += 1
        if predict_number > number:
            mx = predict_number
            predict_number = mx - (mx-mn)//2
        elif predict_number < number:
            mn = predict_number
            predict_number = (mx - mn)//2 + mn
    # print(count)        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return(score)

score_game(random_predict)