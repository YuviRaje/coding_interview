'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

123



'''


def convert_two(number):
    if number == 0:
        return ''
    single_digit = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'tweleve',
                    13:'thirteen', 14:'fourteen', 15:'fifeteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixety', 7:'seventy', 8:'eighty', 9:'ninety'}


    if number <= 19:
        return single_digit[number]

    elif number < 100:

        return tens[number/10] +' '+ (single_digit[number % 10] if single_digit[number % 10] != 'zero' else ' ')

    else:
        raise Exception ('convert_two() called with 3 digit number')


def convert_three(number):
    hundred = {1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred'}
    if number >= 100:

        return hundred[number/100] + ' '+ (convert_two(number % 100) if convert_two(number%100) != 'zero' else ' ')

    elif number < 100:
        return convert_two(number)
    else:
        raise Exception('conver_three() called with number less than hundred')





def convert_to_english(number):
    if number == 0:
        return 'zero'

    k = 0
    prefix = {0:'', 1: 'thousand', 2: 'million', 3:'billion'}
    result = []
    while number > 0:

        three_digit_number = number % 1000
        if k > 0 and convert_three(three_digit_number) == '':
            result.append('')
        else:
            result.append(convert_three(three_digit_number) +' '+ prefix[k])
        number = number/ 1000
        k += 1
    result.reverse()
    return ''.join(result)


print convert_to_english(2090636000)



