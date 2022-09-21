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
    while True:
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
        except ValueError:
            print("неверный тип данных, введите заново")
            continue
        break
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c, mode):
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
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if mode ==2:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
        else:
            result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        if mode ==2:
            if root1>0:
                result.append(math.sqrt(root1))
                result.append(-math.sqrt(root1))
            elif root1==0:
                result.append(root1)
            if root2>0:
                result.append(math.sqrt(root2))
                result.append(-math.sqrt(root2))
            elif root2==0:
                result.append(root2)
        else:
            result.append(root1)
            result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    while True:
        try:
            mode = sys.argv[index]
        except:
            mode = input("Выберите вид уравнения:квалратное 1, биквадратное 2\n")
        if mode=='1' or mode=='2': break
    mode = int(mode)
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
        
    # Вычисление корней
    roots = get_roots(a,b,c, mode)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
            print('Четыре корня: {}; {}; {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
