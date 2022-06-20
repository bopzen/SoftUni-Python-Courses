electrons = int(input())
shell = 1
list_electrons = []
while electrons > 0:
    electrons_per_shell = 2 * shell ** 2
    if electrons_per_shell <= electrons:
        list_electrons.append(electrons_per_shell)
    else:
        list_electrons.append(electrons)
    shell += 1
    electrons -= electrons_per_shell
print(list_electrons)