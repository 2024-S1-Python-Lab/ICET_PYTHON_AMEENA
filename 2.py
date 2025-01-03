List1=[2,4,-6,-8,9,7]
print(f'List1={List1}')
List2=[i for i in List1 if(i>0)]
print(f'positive list = {List2}')


list1=[1,2,3,4,5,6]
list2=[i**2 for i in list1]
print(f'list1={list1}')
print(f'square of elements in list1={list2}')


word=input('Enter a word:')
listvowel=[i for i in word if i in 'aeiouAEIOU']
print(f'vowels in word are {listvowel}')


w=input("Enter any character:")
Ordinalvalue=[ord(i) for i in w]
print(ordinalvalue)
