first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = list(zip(first, second))
ln = range(len(first))

first_result = ((len(x) - len(y)) for x, y in zp if len(x) != len(y))
second_result = (False if len(first[i]) != len(second[i]) else True for i in ln)

print(list(first_result))
print(list(second_result))
