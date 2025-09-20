def lucky_ticket(number):
    num_str = str(number)

    if len(num_str) != 6 or not num_str.isdigit():
        return "Введите шестизначное число"

    first_half = sum(int(d) for d in num_str[:3])
    second_half = sum(int(d) for d in num_str[3:])

    return "Счастливый билет" if first_half == second_half else "Несчастливый билет"


print(lucky_ticket(123456))
print(lucky_ticket(123321))
