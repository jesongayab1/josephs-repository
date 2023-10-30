def add_three_to_digits(number):
    new_number = ''
    for digit in str(number):
        new_number += str((int(digit) + 3) % 10)
    return int(new_number)

while True:
    num = int(input("Enter number to encode: "))
    output = add_three_to_digits(num)
    print(output)


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
