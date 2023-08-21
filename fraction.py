'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.'''

def process_fractions(fract1_str, fract2_str):
    # Преобразуем дроби из строк в числа
    num1, den1 = map(int, fract1_str.split("/"))
    num2, den2 = map(int, fract2_str.split("/"))

    # Вычисляем сумму дробей
    sum_fract_num = num1 * den2 + num2 * den1
    sum_fract_den = den1 * den2
    sum_fract = (sum_fract_num, sum_fract_den)

    # Вычисляем произведение дробей
    prod_fract_num = num1 * num2
    prod_fract_den = den1 * den2
    prod_fract = (prod_fract_num, prod_fract_den)

    return sum_fract, prod_fract

# Пример использования функции
fract1_str = "3/4"
fract2_str = "2/3"

sum_fract, prod_fract = process_fractions(fract1_str, fract2_str)

print(f"Сумма дробей {fract1_str} и {fract2_str} - {sum_fract[0]}/{sum_fract[1]}")
print(f"Произведение дробей {fract1_str} и {fract2_str} - {prod_fract[0]}/{prod_fract[1]}")