def main(input: str) -> str:
    input = input.replace(" ", "")

    operator = None
    for op in ['+', '-', '/', '*']:
        if op in input:
            operator = op
            break
    if not operator:
        raise Exception('Use only "+, -, /, *" symbols')
    parts = input.split(operator)
    if len(parts) !=2:
        raise Exception('Use no more than two numbers')
    try:
        a = int(parts[0])
        b = int(parts[1])
    except ValueError:
        raise Exception('Numbers must be integers')

    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise Exception('Numbers must be in a range from 1 to 10')

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a // b
    elif operator == '*':
        result = a * b
    else:
        raise Exception('Only +, -, / and * are available')
    return str(result)

user_input = input('Write the arithmetics')

try:
    output = main(user_input)
    print('result: ', output)
except Exception as e:
    print('Error: ', e)