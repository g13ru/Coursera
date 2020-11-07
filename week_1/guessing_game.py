number = random.randint(10, 50)

while True:
  answer = input('Введите число: ')
  if not answer:
    break

  if not answer.isdigit():
    print('Введите ЧИСЛО !')
    continue
  
  user_answer = int(answer)

  if user_answer > number:
    print('Загаданное число меньше')
  elif user_answer < number:
    print('Загаданное число больше')
  else:
    print('Верно!')
    #break
