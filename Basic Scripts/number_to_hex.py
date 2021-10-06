hex_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
def number_to_hex(number_to_convert: int):
    result = number_to_convert
    hexadecimal = ""
    while result != 0:
        remainder = hex_numbers[result % 16]
        hexadecimal = str(remainder) + hexadecimal
        result = int(result / 16)
    print(hexadecimal)

if __name__ == "__main__":
    num= int(input("Enter number in decimal:\n"))
    number_to_hex(num)
 #added user input