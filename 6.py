list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
#a
if len(list1)==len(list2):
    print('a. The lists have the same length.')
else:
    print('a. The lists have different length.')

#b
if sum(list1)==sum(list2):
    print('b. The lists sum to the same value.')
else:
    print('b. The lists do not sum to the same value.')

#c
common_value=set(list1) & set(list2)
if common_value:
    print(f'c. Common values in both lists:{common_value}.')
else:
    print('c. There are no common values in both lists.')
