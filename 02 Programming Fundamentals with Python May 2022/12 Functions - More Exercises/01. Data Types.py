def data_type(type, text):
    if type == 'int':
        print(int(text) * 2)
    elif type == 'real':
        print(f'{float(text) * 1.5:.2f}')
    elif type == 'string':
        print(f'${text}$')


data_type(input(),input())