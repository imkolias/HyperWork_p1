# var for save middle result
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
     elif m_number == 10:
         print("Are you sure? It is only one digit! (y / n)")
     elif m_number == 11:
         print("Don't be silly! It's just one number! Add to the memory? (y / n)")
     elif m_number == 12:
         print("Last chance! Do you really want to embarrass yourself? (y / n)")


# проверка введенных цифры (isonedigit)
def is_one_digit(v):
#    print('this is DigitCheck =', v)
    if -10 < v < 10:
        try:
            if v == int(v):
#                print('----> T one digit')
                return True

        except:
#            print('----> F one digit')
            return False


    # if (-10 < v < 10) and v == int(v):
    #     print('----> T one digit')
    #     return True
    # else:
    #     print('----> F one digit')
    #     return False


# проверка данных
def check(v1, v2, v3):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"


    if is_one_digit(v1) == True and is_one_digit(v3) == True:
        msg += msg_6
    if (v1 == 1 or v3 == 1) and v2 =='*':
        msg += msg_7
    if (v1 == 0 or v3 == 0) and (v2 == '*' or v2 == '+' or v2 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


# запрашиваем ввод у пользователя
def user_input_func():
    print("Enter an equation")
    calc = str(input())
    return calc


# проверяем ввод данных для расчета от пользователя на корректность
def input_processing(calc_inp):
    x, oper, y = calc_inp.split()

    # проверяем введенные данные на то цифры это или нет
    try:
        x = float(x)
    except:
        if x != 'M':
            msg_print(1)
            return False
        else:
            x = float(middle_result)

    try:
        y = float(y)
    except:
        if y != 'M':
            msg_print(1)
            return False
        else:
            y = float(middle_result)

    # x, oper, y = calc_inp.split()
    #
    # # проверяем введенные данные на то цифры это или нет
    # try:
    #     x = float(x)
    #     y = float(y)
    # except:
    #     if (x != 'M' and x == int(x)) or (y != 'M' and y == int(y)):
    #         msg_print(1)
    #         return False
    #     if x == 'M':
    #         x = float(middle_result)
    #     if y == 'M':
    #         y = float(middle_result)




    # проверяем oper является ли корректным математическим оператором
    if oper != '+' and oper != '-' and oper != '/' and oper != '*':
        msg_print(2)
        return False

    # проверка на ленивость
    check(x, oper, y)

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
    msg_index = 10

    while save_result_opt != 'y':

        msg_print(4)

        save_result_opt = str(input())
        if save_result_opt == 'y':

            ###
            # print('Check digit right before save result', middle_result)
            if is_one_digit(temp_result) == True:

                while True:
                    msg_print(msg_index)
                    one_dig_answer = str(input())
                    if one_dig_answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            middle_result = temp_result
                            break

                    elif one_dig_answer == 'n':
                        break
            else:
                middle_result = temp_result
                break

            ###

        elif save_result_opt == 'n':
            break
        else:
            continue


# основной цикл который работает пока есть неправильные данные на входе
while True:
    final_result = input_processing(user_input_func())
    if final_result is False:
        continue
    else:
        print(final_result)

        # функция сохранения промежуточного результата
        save_midl_result(final_result)

        # спрашиваем пользователя будет ли он еще раз чтото считать
        msg_print(5)
        if str(input()) == 'y':
            continue
        else:
            break
