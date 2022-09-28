# This is a sample Python script.

import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()

    # Переводим строку в действительное число
    while True:
        try:
            coef = float(coef_str)
        except ValueError:
            print("Неверный ввод. Попробуйте еще раз")
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        else:
            break

    return coef

#Определение знака
def get_sign(number):
    if number >= 0:
        return '+'
    return '-'


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_roots_biquadratic(roots):
    '''
    Вычисление корней для биквадратного уравнения исходя из результата функции - [get_roots]
    Args:
        list [float]: массив корней квадратного уравнения

    Returns:
        list [float]: массив корней биквадратного уравнения
    '''

    result = []

    for root in roots:
        if root == 0:
            result.append(root)
        elif root > 0:
            sqRoot = math.sqrt(root)
            result.append(sqRoot)
            result.append(-sqRoot)

    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент - [a]:')
    while a == 0.0:
        print('Коэффициент - [a] в биквадратном уравнении не может равняться нулю')
        a = get_coef(1, 'Введите коэффициент - [a]:')
    b = get_coef(2, 'Введите коэффициент - [b]:')
    c = get_coef(3, 'Введите коэффициент - [c]:')

    # Вычисление корней для квадратного уравнения
    roots = get_roots(a, b, c)

    # Вычисление корней для биквадратного уравнения исходя из результата функции - [get_roots]
    roots = get_roots_biquadratic(roots)

    # Вывод корней
    len_roots = len(roots)

    if len_roots == 0:
        print('У уравнения {}x^4 {} {}x^2 {} {} нет корней'.format(a, get_sign(b), abs(b), get_sign(c), abs(c)))

    elif len_roots == 1:
        print('У уравнения {}x^4 {} {}x^2 {} {} один корень: {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0]))

    elif len_roots == 2:
        print('У уравнения {}x^4 {} {}x^2 {} {} два корня: {}, {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0], roots[1]))

    elif len_roots == 3:
        print('У уравнения {}x^4 {} {}x^2 {} {} три корня: {}, {}, {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0], roots[1], roots[2]))

    elif len_roots == 4:
        print('У уравнения {}x^4 {} {}x^2 {} {} четыре корня: {}, {}, {}, {}'.format(a, get_sign(b), abs(b), get_sign(c), abs(c), roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
