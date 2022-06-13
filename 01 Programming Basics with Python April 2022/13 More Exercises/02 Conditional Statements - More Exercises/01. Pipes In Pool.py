volume = int(input())
pipe1_debit = int(input())
pipe2_debit = int(input())
hours = float(input())
pipe1_fill = pipe1_debit*hours
pipe2_fill = pipe2_debit*hours
fill = pipe1_fill + pipe2_fill
if fill <= volume:
    print(f'The pool is {fill/volume*100:.2f}% full. Pipe 1: {pipe1_fill/fill*100:.2f}%. Pipe 2: {pipe2_fill/fill*100:.2f}%."')
else:
    print(f'For {hours} hours the pool overflows with {fill-volume} liters.')