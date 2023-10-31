# Joseph Songayab
def add_three_to_digits(number):
    new_number = ''
    for digit in str(number):
        new_number += str((int(digit) + 3) % 10)
    return int(new_number)

def decode(password):
    pw = []
    decoded_pass = []
    string_pass = ""
    for value in password:
        pw.append(int(value))
    for digit in pw:
        digit -= 3
        if digit < 0:
            digit += 10
        decoded_pass.append(digit)
    for value in decoded_pass:
        string_pass += str(value)
    return string_pass

while True:
    num = int(input("Enter number to encode: "))
    output = add_three_to_digits(num)
    print(output)


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
