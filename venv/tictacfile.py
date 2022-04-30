M = ['_', '_', '_',
     '_', '_', '_',
     '_', '_', '_']
vvod = ''
n = None
def my_print(a):
    result = ''
    for i in range(len(a)):
        result += a[i] + ' '
        if i == 2 or i == 5:
            result += ' \n'
    return print(result)
my_print(M)
def pob(a):
    return a[:3] == ['X', 'X', 'X'] or a[:3] == ['0', '0', '0'] \
          or a[3:6] == ['X', 'X', 'X'] or a[3:6] == ['0', '0', '0'] \
          or a[6:] == ['X', 'X', 'X'] or a[6:] == ['0', '0', '0'] \
          or a[0::3] == ['X', 'X', 'X'] or a[0::3] == ['0', '0', '0'] \
          or a[1::3] == ['X', 'X', 'X'] or a[1::3] == ['0', '0', '0'] \
          or a[2::3] == ['X', 'X', 'X'] or a[2::3] == ['0', '0', '0'] \
          or a[0::4] == ['X', 'X', 'X'] or a[0::4] == ['0', '0', '0'] \
          or a[2:7:2] == ['X', 'X', 'X'] or a[2:7:2] == ['0', '0', '0']
def hod(x):
    x = int(input('Номер хода от 0 до 8: '))
    if 0 <= x <= 8 and M[x] == '_':
        M[x] = vvod
    else:
        print('Неверный ход \n')
        hod(x)
for i in range(9):
    if i % 2 == 0:
        vvod = 'X'
    else:
        vvod = '0'
    hod(n)
    print(i)
    my_print(M)
    if pob(M):
        print('Победа игрока ', vvod)
        break
if not pob(M):
   print('Ничья!')