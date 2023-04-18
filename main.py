# StartingNumber_1 = int(input())
# StartingNumber_2 = int(input())


def TurnToBin(int_number):
    turned_number = []
    int_number_res = int_number
    if int_number < 0:
        int_number = int_number * -1
    while int_number > 0:
        turned_number.insert(0, int_number % 2)
        int_number = int_number // 2
    while len(turned_number) < 31:
        turned_number.insert(0, 0)
    if int_number_res < 0:
        turned_number.insert(0, 1)
    else:
        turned_number.insert(0, 0)
    return turned_number


def TurnToRevCode(bin_number):
    for iterator in range(1, 32):
        if bin_number[iterator] == 0:
            bin_number[iterator] = 1
        else:
            bin_number[iterator] = 0
    return bin_number


def TurnToAddCode(bin_number):
    rev_number = TurnToRevCode(bin_number)
    overflow = 0
    one = TurnToBin(1)
    result = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for iterator in reversed(range(1, 32)):
        result[iterator] = rev_number[iterator] + one[iterator] + overflow
        if result[iterator] == 2:
            result[iterator] = 0
            overflow = 1
        elif result[iterator] == 1 | result[iterator == 0]:
            overflow = 0
    return result


def StraightSumBinPositive(turned_number_1, turned_number_2):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    overflow = 0
    # turned_number_1 = TurnToBin(number_1)
    # turned_number_2 = TurnToBin(number_2)
    for iterator in reversed(range(0, 32)):
        result[iterator] = turned_number_1[iterator] + turned_number_2[iterator] + overflow
        if result[iterator] == 3:
            result[iterator] = 1
            overflow = 1
        elif result[iterator] == 2:
            result[iterator] = 0
            overflow = 1
        elif result[iterator] == 1 | result[iterator == 0]:
            overflow = 0
    return result


def SumWithNegative(turned_1, turned_2):
    # turned_1 = TurnToBin(number_1)
    # turned_2 = TurnToBin(number_2)
    if turned_1[0] == 1:
        final_num_1 = TurnToAddCode(turned_1)
    else:
        final_num_1 = turned_1
    if turned_2[0] == 1:
        final_num_2 = TurnToAddCode(turned_2)
    else:
        final_num_2 = turned_2
    result = StraightSumBinPositive(final_num_1, final_num_2)
    return result


def Subtraction(turned_1, turned_2):
    if turned_2[0] == 0:
        turned_2[0] = 1
    else:
        turned_2[0] = 0
    result = SumWithNegative(turned_1, turned_2)
    return result


def MultiplicationItself(number_1, number_2):
    new_number_1 = abs(number_1)
    new_number_2 = abs(number_2)
    turned_1 = TurnToBin(new_number_1)
    # print(turned_1)
    turned_2 = TurnToBin(new_number_2)
    # print(turned_2)
    result = turned_1
    for iterator in range(new_number_2 - 1):
        result = SumWithNegative(result, turned_1)
    if (number_1 < 0 and number_2 > 0) or (number_1 > 0 and number_2 < 0):
        result[0] = 1
    else:
        result[0] = 0
    return result


def Division(turned_1, turned_2):
    turned_1_unsigned, turned_2_unsigned = turned_1[1:], turned_2[1:]
    turned_1_unsigned, turned_2_unsigned = turned_1_unsigned[turned_1_unsigned.index(1):], turned_2_unsigned[
                                                                                     turned_2_unsigned.index(1):]
    quotient = []
    temp_divident = []
    for current_digit in turned_1_unsigned:
        temp_divident += [current_digit]
        max = MaxOfTwoBinNumbers([0] + turned_2_unsigned, [0] + temp_divident)
        if max == [0] + turned_2_unsigned and max != [0] + temp_divident:
            quotient += [0]

            continue
        quotient += [1]
        smth = [0] * (32 - len(turned_2_unsigned)) + turned_2_unsigned[1:]
        sub = TurnBackFromAddToDirect(Subtraction(([0] * (32 - len(temp_divident))) + temp_divident,
                                                  ([0] * (32 - len(turned_2_unsigned))) + turned_2_unsigned))
        temp_divident = TurnBackFromAddToDirect(sub)
    return [int(turned_1[0] + turned_2[0] == 1)] + [0] * (32 - len(quotient) - 1) + quotient


def TurnBackFromAddToDirect(bin_number):
    if bin_number[0] == 0:
        return bin_number
    one = [0] * (len(bin_number) - 1) + [1]
    for i in range(len(bin_number) - 1, -1, -1):
        if bin_number[i] == 0:
            bin_number[i] = 1
        else:
            bin_number[i] = 0
            break
    else:
        bin_number = [1] + [0] * (len(bin_number) - 2) + [1]
    return TurnToRevCode(bin_number)


def MaxOfTwoBinNumbers(num1: list, num2: list, signed=False) -> list:
    if signed:
        return num1 if int("".join(str(x) for x in num1), 2) \
                       > int("".join(str(x) for x in num2), 2) else num2
    return num1 if int("".join(str(x) for x in num1[1:]), 2) \
                   > int("".join(str(x) for x in num2[1:]), 2) else num2


def TurnToInt(bin_number):
    number = int("".join(str(x) for x in bin_number[1:]), 2)
    number *= -1 if bin_number[0] == 1 else 1
    return number


def RightPrintOfBinNumber(bin_number):
    output_number = ""
    for current_number in bin_number:
        output_number = output_number + str(current_number)
    return str(output_number)


# StartingNumber_1_Turned = TurnToBin(StartingNumber_1)
# StartingNumber_2_Turned = TurnToBin(StartingNumber_2)
# print(StartingNumber_1_Turned)
# print(StartingNumber_2_Turned)
# print(StraightSumBinPositive(StartingNumber_1_Turned, StartingNumber_2_Turned))
# StartingNumber_1_Turned_Rev = TurnToRevCode(StartingNumber_1_Turned)
# StartingNumber_2_Turned_Rev = TurnToRevCode(StartingNumber_2_Turned)
# print(StartingNumber_1_Turned_Rev)
# print(StartingNumber_2_Turned_Rev)
# StartingNumber_1_Turned_Add = TurnToAddCode(StartingNumber_1_Turned_Rev)
# StartingNumber_2_Turned_Add = TurnToAddCode(StartingNumber_2_Turned_Rev)
# print(StartingNumber_1_Turned_Add)
# print(StartingNumber_2_Turned_Add)
# print(SumWithNegative(StartingNumber_1_Turned, StartingNumber_2_Turned))
# print(Subtraction(StartingNumber_1_Turned, StartingNumber_2_Turned))
# print(MultiplicationItself(StartingNumber_1, StartingNumber_2))
# result = Division(StartingNumber_1_Turned, StartingNumber_2_Turned)
# print(StartingNumber_1_Turned)
# print(TurnToInt(StartingNumber_1_Turned))
print("\033[34m{}".format("_MENU_\n-----"))
while True:
    operation_selector = input('please, choose an operation:\n1 - sum\n2 - subtraction\n3 - multiplying\n4 - divisi'
                                   'on\n5 - finish the work ;)\n')

    if operation_selector == '1':
        print("\033[34m{}".format("Your choice: Sum"))
        starting_number_1 = int(input('input first number:\n'))
        starting_number_2 = int(input('input second number:\n'))
        starting_number_1 = TurnToBin(starting_number_1)
        starting_number_2 = TurnToBin(starting_number_2)
        result = TurnBackFromAddToDirect(SumWithNegative(starting_number_1, starting_number_2))
        print("- The result in binary code: ", RightPrintOfBinNumber(result))
        print("- The result in decimal: ", TurnToInt(result))
        print("----------------------------------------------------")

    elif operation_selector == '2':
        print("\033[34m{}".format("Your choice: Subtraction"))
        starting_number_1 = int(input('input first number:\n'))
        starting_number_2 = int(input('input second number:\n'))
        starting_number_1 = TurnToBin(starting_number_1)
        starting_number_2 = TurnToBin(starting_number_2)
        result = TurnBackFromAddToDirect(Subtraction(starting_number_1, starting_number_2))
        # print(result)
        print("- The result in binary code: ", RightPrintOfBinNumber(result))
        print("- The result in decimal: ", TurnToInt(result))
        print("----------------------------------------------------")

    elif operation_selector == '3':
        print("\033[34m{}".format("Your choice: Multiplying"))
        starting_number_1 = int(input('input first number:\n'))
        starting_number_2 = int(input('input second number:\n'))
        # starting_number_1 = TurnToBin(starting_number_1)
        # starting_number_2 = TurnToBin(starting_number_2)
        result = MultiplicationItself(starting_number_1, starting_number_2)
        # print(result)
        print("- The result in binary code: ", RightPrintOfBinNumber(result))
        print("- The result in decimal: ", TurnToInt(result))
        print("----------------------------------------------------")

    elif operation_selector == '4':
        print("\033[34m{}".format("Your choice: Division"))
        starting_number_1 = int(input('input first number:\n'))
        starting_number_2 = int(input('input second number:\n'))
        starting_number_1 = TurnToBin(starting_number_1)
        starting_number_2 = TurnToBin(starting_number_2)
        result = Division(starting_number_1, starting_number_2)
        # print(result)
        print("- The result in binary code: ", RightPrintOfBinNumber(result))
        print("- The result in decimal: ", TurnToInt(result))
        print("----------------------------------------------------")

    elif operation_selector == '5':
        print("Thanks for the interaction, have a good day :)")
        break

    else:
        print("Ooops, you entered a wrong symbol, try again")
        print("----------------------------------------------------")




