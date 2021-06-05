"""task_1"""
# try:
#     spending = int(input('Enter spanding: '))
#     cost = float(input('Enter cost'))
#     distance = float(input('Enter distance: '))
#     money = spending / 100 * distance * cost
#     if spending <= 0 or cost <= 0 or distance <= 0:
#         raise ValueError
#     print(f"You must pay {money}")
# except ValueError:
#     print('Uncorrect value!')

"""task_2"""
# try:
#     cost_one_minute = float(input('Enter the price for 1 minute: '))
#     conversation_duration = float(input('Enter conversation duration: '))
#     result = cost_one_minute*conversation_duration
#     if cost_one_minute <= 0 or conversation_duration <= 0 :
#         raise ValueError
#     print(f"Вартість вашого дзвінка складає - {result} UAH")
# except ValueError:
#     print('Uncorrect value!')


"""task_3"""

# try:
#     number_of_revolutions = int(input('Enter obert: '))
#     one_revolution_in_day = 686
#     result = (number_of_revolutions*one_revolution_in_day)/365
#     if number_of_revolutions <= 0:
#         raise ValueError
#     print(float('{:.1f}'.format(result)),
#           f'р. стільки часу займе {number_of_revolutions} повних обертів Марсу навколо Сонця')
# except ValueError:
#     print('Uncorrect value!')


"""task_4"""
# try:
#     print("""1 - Переводить температуру з градусів по Цельсію в температуру по Фаренгейту \n2 - Переводить температуру по Фаренгейту у температуру в градусах Цельсію """)
#     take_method = int(input('Ввиберіть потрібний варіант (1/2)'))
#     if take_method == 1:
#         print('Ви вибрали 1 варіант')
#         degrees_сelsius = float(input(
#             'Введіть температуру в градусах по Цельсію, щоб ми конвертували в температуру по Фаренгейту'))
#         result_temp_fahrenheit = degrees_сelsius * 1.8 + 32
#         print(
#             f'Конвертована температура в градуси Фаренгейту - {result_temp_fahrenheit} F')
#     if take_method == 2:
#         print('Ви вибрали 2 варіант')
#         degrees_fahrenheit = float(input(
#             'Введіть температуру в градусах по Фаренгейту, щоб ми конвертували в температуру по Цельсію'))
#         result_temp_degrees_сelsius = (degrees_fahrenheit - 32)/1.8
#         print(
#             f'Конвертована температура в градуси Цельсію - ', float('{:.1f}'.format(result_temp_degrees_сelsius)), 'C')
# except ValueError:
#     print('Uncorrect value')
"""task_5"""
# flag = True
# menu = int(input('Вивести меню калькулятора 1 - так / 2 - ні'))
# while flag:
#     try:
#         if menu == 1:
#             print('Виводимо меню калькулятора', end="...")
#             menu_calculator = int(input(
#                 '\n1:+\n2:-\n3:*\n4:/\n5:**.\nВиберіть ваший варіант'))
#             if menu_calculator == 1:
#                 print('Вибрано дію - ДОДАВАННЯ')
#                 ask = int(
#                     input('Які числа будете вводити 1 - цілі / 2 - дробові'))
#                 if ask == 2:
#                     number_1 = float(input('Введіть перше число: '))
#                     number_2 = float(input('Введіть друге число: '))
#                     result_addition = number_1 + number_2
#                     print(f'{number_1} +{number_2} = {result_addition}')
#                 if ask == 1:
#                     number_1 = int(input('Введіть перше число: '))
#                     number_2 = int(input('Введіть друге число: '))
#                     result_addition = number_1 + number_2
#                     print(f'{number_1} +{number_2} = {result_addition}')
#             if menu_calculator == 2:
#                 print('Вибрано дію - ВІДНІМАННЯ')
#                 ask = int(
#                     input('Які числа будете вводити 1 - цілі / 2 - дробові'))
#                 if ask == 1:
#                     number_1 = int(input('Введіть перше число: '))
#                     number_2 = int(input('Введіть друге число: '))
#                     result_deduction = number_1 - number_2
#                     print(f'{number_1} - {number_2} = {result_deduction}')
#                 if ask == 2:
#                     number_1 = float(input('Введіть перше число: '))
#                     number_2 = float(input('Введіть друге число: '))
#                     result_deduction = number_1 - number_2
#                     print(f'{number_1} - {number_2} = {result_deduction}')
#             if menu_calculator == 3:
#                 print('Вибрано дію - МНОЖЕННЯ')
#                 ask = int(
#                     input('Які числа будете вводити 1 - цілі / 2 - дробові'))
#                 if ask == 1:
#                     number_1 = int(input('Введіть перше число: '))
#                     number_2 = int(input('Введіть друге число: '))
#                     result_multiplication = number_1 * number_2
#                     print(f'{number_1} * {number_2} = {result_multiplication}')
#                 if ask == 2:
#                     number_1 = float(input('Введіть перше число: '))
#                     number_2 = float(input('Введіть друге число: '))
#                     result_multiplication = number_1 * number_2
#                     print(f'{number_1} * {number_2} = {result_multiplication}')
#             if menu_calculator == 4:
#                 print('Вибрано дію - ДІЛЕННЯ')
#                 ask = int(
#                     input('Які числа будете вводити 1 - цілі / 2 - дробові'))
#                 if ask == 1:
#                     number_1 = int(input('Введіть перше число: '))
#                     number_2 = int(input('Введіть друге число: '))
#                     if number_2 == 0:
#                         raise ZeroDivisionError('На 0 ділити не можна!!!')
#                     result_division = int(number_1 / number_2)
#                     print(f'{number_1} / {number_2} = {result_division}')
#                 if ask == 2:
#                     number_1 = float(input('Введіть перше число: '))
#                     number_2 = float(input('Введіть друге число: '))
#                     if number_2 == 0:
#                         raise ZeroDivisionError('На 0 ділити не можна!!!')
#                     result_division = number_1 / number_2
#                     print(f'{number_1} / {number_2} = {result_division}')
#             if menu_calculator == 5:
#                 print('Вибрано дію - ПІДНЕСЕННЯ ДО СТЕПЕНІ')
#                 ask = int(
#                     input('Які числа будете вводити 1 - цілі / 2 - дробові'))
#                 if ask == 1:
#                     number_1 = int(input('Введіть перше число: '))
#                     number_2 = int(input('Введіть степінь: '))
#                     result_elevation_to_the_degree = number_1 ** number_2
#                     print(
#                         f'{number_1} ** {number_2} = {result_elevation_to_the_degree}')
#                 if ask == 2:
#                     number_1 = float(input('Введіть перше число: '))
#                     number_2 = float(input('Введіть степінь: '))
#                     result_elevation_to_the_degree = number_1 ** number_2
#                     print(
#                         f'{number_1} ** {number_2} = {result_elevation_to_the_degree}')

#             flag = False
#         if menu == 2:
#             print('Програму закрито')
#             break
#     except ValueError:
#         print('Uncorrect value!')
#         break
"""task_6"""
# flag = True
# while flag:
#     try:
#         ask_money = float(input('Cкільки у вас коштів?'))
#         bag = ask_money
#         if ask_money < 50:
#             print('У вас недостаньо коштів!! Атракціони від 50UAH')
#             break
#         if ask_money >= 150 and ask_money < 300:
#             print(
#                 'Вам доступний Атракціон №1 - вартість 50UAH \nВам доступний Атракціон №2 - вартість 100UAH\nВам доступний атракціон №3 - вартість 150UAH')
#             ask_for_pay = int(input('1-Сплатити /2 - Вихід'))
#             if ask_for_pay == 2:
#                 break
#             if ask_for_pay == 1:
#                 ask_atraction_take = int(input(
#                     '1 - Атракціон №1 \n2 - Атракціон №2\n3 - Оплатити Атракціон №3\n4 - Оплатити два.\nВиберіть ваш варіант'))
#                 if ask_atraction_take == 1:
#                     result = bag - 50
#                     print(
#                         f'Куплено квиток на Атракціон №1, залишилось коштів {result} UAH')
#                 if ask_atraction_take == 2:
#                     result = bag - 100
#                     print(
#                         f'Куплено квиток на Атракціон №2, залишилось коштів {result} UAH')
#                 if ask_atraction_take == 3:
#                     result = bag - 150
#                     print(
#                         f'Куплено квиток на Атракціон №3, залишилось коштів {result}')
#                 if ask_atraction_take == 4:
#                     result = bag - 150
#                     print(
#                         f'Куплено квиток на Атракціон №1,№2 залишилось коштів {result} UAH')
#         if ask_money >= 50 and ask_money < 100:
#             print('Вам доступний Атракціон №1 - вартість 50UAH')
#             ask_for_pay = int(input('1-Сплатити /2 - Вихід'))
#             if ask_for_pay == 1:
#                 result = bag - 50
#                 print(
#                     f'Куплено квиток на Атракціон №1, залишилось коштів {result}')
#         if ask_money >= 100 and ask_money < 150:
#             print(
#                 'Вам доступний Атракціон №1 - вартість 50UAH \nВам доступний Атракціон №2 - вартість 100UAH')
#             ask_for_pay = int(input('1-Сплатити /2 - Вихід'))
#             if ask_for_pay == 2:
#                 break
#             if ask_for_pay == 1:
#                 ask_atraction_take = int(
#                     input('1 - Атракціон №1 \n2 - Атракціон №2\nВиберіть ваш варіант'))
#                 if ask_atraction_take == 1:
#                     result = bag - 50
#                     print(
#                         f'Куплено квиток на Атракціон №1, залишилось коштів {result} UAH')
#                 if ask_atraction_take == 2:
#                     result = bag - 100
#                     print(
#                         f'Куплено квиток на Атракціон №1, залишилось коштів {result} UAH')
#         if ask_money >= 300:
#             print('Вам доступний Атракціон №1 - вартість 50UAH \nВам доступний Атракціон №2 - вартість 100UAH\nВам доступний атракціон №3 - вартість 150UAH')
#             ask_for_pay = int(input('1-Сплатити /2 - Вихід'))
#             if ask_for_pay == 2:
#                 break
#             if ask_for_pay == 1:
#                 ask_atraction_take = int(input(
#                     '1 - Атракціон №1 \n2 - Атракціон №2\n3 - Оплатити Атракціон №3\n4 - Оплатити 1,2\n5 - Оплатити 2-3\n6 - Оплатити всі!\nВиберіть ваш варіант'))
#                 if ask_atraction_take == 1:
#                     result = bag - 50
#                     print(
#                         f'Куплено квиток на Атракціон №1, залишилось коштів {result} UAH')
#                 if ask_atraction_take == 2:
#                     result = bag - 100
#                     print(
#                         f'Куплено квиток на Атракціон №2, залишилось коштів {result} UAH')
#                 if ask_atraction_take == 3:
#                     result = bag - 150
#                     print(
#                         f'Куплено квиток на Атракціон №3, залишилось коштів {result}')
#                 if ask_atraction_take == 4:
#                     result = bag - 150
#                     print(
#                         f'Куплено квиток на Атракціон №1,№2 залишилось коштів {result} UAH')
#                 if ask_atraction_take == 5:
#                     result = bag - 250
#                     print(
#                         f'Куплено квиток на Атракціон №1,№2 залишилось коштів {result} UAH')
#                 if ask_atraction_take == 6:
#                     result = bag - 300
#                     print(
#                         f'Куплено квиток на Атракціон №1,№2 залишилось коштів {result} UAH')
#         flag = False
#     except ValueError:
#         print('Uncorrect value !!!')

"""task_7"""
# user_1 = {
#     'name': 'Anton',
#     'password': 13579,
#     'balance': 1000,
# }
# flag = True

# while flag:
#     try:
#         ask_password = int(input('Введіть пароль : '))
#         if ask_password == user_1['password']:
#             print(f"Раді вас бачити {user_1['name']}")
#             print('Меню:')
#             show_menu = int(
#                 input('\t1:Поточний баланс\n\t2:Зняти гроші\n\t3:Вихід\nВиберіть варінт з меню'))
#             if show_menu == 1:
#                 print(f"На вашому балансі - {user_1['balance']}UAH")
#                 break
#             if show_menu == 2:
#                 ask_sum_money = float(input('Яку суму ви бажаєте зняти: '))
#                 if ask_sum_money > user_1['balance']:
#                     print('Недостатньо коштів на рахунку')
#                     raise ValueError('Недостатньо коштів на рахунку')

#                 if 0 < ask_sum_money <= user_1['balance']:
#                     result = user_1['balance'] - ask_sum_money
#                     print(
#                         f"Знято - {ask_sum_money}UAH ,залишилось на рахунку {result}UAH")
#                     break
#                 else:
#                     print('Некоректно введені дані')
#                     raise ValueError
#             if show_menu == 3:
#                 flag = False

#             else:
#                 print('Некоректо вибраний варіант')
#                 break
#         if ask_password != user_1['password']:
#             print('Неправильно введений пароль')
#             break
#     except ValueError:
#         print('Uncorrect value !!!')
