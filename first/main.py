

# write your code here
middle_result = 0


# функция выдачи ошибок пользователю
def msg_print(m_number):
    if m_number == 1:
        print("Do you even know what numbers are? Stay focused!")
    elif m_number == 2:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    elif m_number == 3:
        print("Yeah... division by zero. Smart move...")
    elif m_number == 4:
        print("Do you want to store the result? (y / n):")
    elif m_number == 5:
        print("Do you want to continue calculations? (y / n):")


# запрашиваем ввод у пользователя
def user_input_func():
    print("Enter an equation")
    calc = str(input())
    return calc


# проверяем ввод на корректность
def input_processing(calc_inp):
    x, oper, y = calc_inp.split()

    # проверяем введенные данные на то цифры это или нет
    try:
        x = float(x)
        y = float(y)
    except:
        if x == 'M': x = middle_result
        elif y == 'M': y = middle_result
        else:
            msg_print(1)
            return False

    # проверяем oper является ли корректным оператором математическим
    if oper != '+' and oper != '-' and oper != '/' and oper != '*':
        msg_print(2)
        return False

    # считаем с учетом заданных параметров
    if oper == '/' and y != 0:
        return x / y
    elif oper == '*':
        return x * y
    elif oper == '-':
        return x - y
    elif oper == '+':
        return x + y
    else:
        if oper == '/' and y == 0:
            msg_print(3)
            return False

# сохранение результата
def save_midl_result(temp_result):
    global middle_result
    save_result_opt = ''

    while save_result_opt != 'y':

        msg_print(4)

        save_result_opt = str(input())
        if save_result_opt == 'y':
            middle_result = temp_result
            break
        elif save_result_opt != 'n' and save_result_opt != 'y':
            continue
        else:
            break


# основной цикл который работает пока есть неправильные данные на входе
while True:
    final_result = input_processing(user_input_func())
    if final_result == False:
        continue
    else:
        print (final_result)

        save_midl_result(final_result)


        # спрашиваем пользователя будет ли он еще раз чтото считать
        msg_print(5)
        if str(input()) == 'y':
            continue
        else: break