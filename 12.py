color=[]
n=int(input('Enter total no of colors:'))
print('Enter colors')
for i in range(n):
    ch=input()
    color.append(ch)
print(f'First color is : {color[0]}\n Last color is : {color[-1]}')
