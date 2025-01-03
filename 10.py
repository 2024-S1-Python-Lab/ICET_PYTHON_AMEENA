n1=int(input('Enter number 1:'))
n2=int(input('Enter number 2:'))
n3=int(input('Enter number 3:'))

if n1>n2 and n1>n3:
    print(f'Largest no is {n1}')
elif n2>n1 and n2>n3:
    print(f'Largest no is {n2}')
else:
    print(f'Largest no is {n3}')
