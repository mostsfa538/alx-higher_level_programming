#!/usr/bin/python3
for i in range(100):
    print('0{ii}'.format(ii=i) if i < 10 else f'{i}', end='')
    print(', ' if i != 99 else '\n', end='')
