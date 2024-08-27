def calculator():
    while True:
        try:
            a, b = float(input('Введите первое число: ')), float(input('Введите второе число: '))
            znak = input('Введите знак операции: "+", "-", "*", "/" или введите "exit" для завершения программы ')

            if znak == 'exit':
                break
            
            if znak == '+':
                res = a + b
            elif znak == '-':
                res = a - b
            elif znak == '*':
                res = a * b
            elif znak == '/':
                res = a / b
            else:
                print('Некорректная операция!')
                continue

            print(f'Результат: {res}')

        except ZeroDivisionError:
            print('Ошибка: Деление на ноль!')
        except ValueError:
            print('Ошибка: Некорректные данные')
        finally:
            print('Программа завершена!')


calculator()
