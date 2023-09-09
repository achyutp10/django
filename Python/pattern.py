x = int(input('How many: '))

def pattern(x):
  for i in range(0,x):
    for j in range(0,i+1):
      print('*', end=' ')
    print()

pattern(x)