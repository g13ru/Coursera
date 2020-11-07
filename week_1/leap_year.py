'''
Определяет високосный год или нет математическиим методом и библиотекой calendar
'''
import calendar

year = int(input('Введите год: '))
print('\n''Первый метод:''\n')
if year % 4 == 0 and (year % 100 != 0 or year %400 != 0):
  print('Високосный год')
else:
  print('Невисокосный год')

print('\n''Второй метод:''\n')

if calendar.isleap(year):
  print('Високосный год')
else:
  print('Невисокосный год')


