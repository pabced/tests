
def checkNumber(num):
    sum = 0
    for i in range(1,num):
        if (num % i == 0):
            sum += i

    type = ''

    if sum == num:
        type = 'PERFECTO'
    elif sum > num:
        type = 'ABUNDANTE'
    else:
        type = 'DEFECTIVO'

    return str(num) + ' - ' + type


def main():

    values = input("Introduzca una lista de números positivos separados por coma ',': ",)

    numberList = values.split(',')

    for value in numberList:
        print(checkNumber(int(value)))

if __name__ == '__main__':
    main()
