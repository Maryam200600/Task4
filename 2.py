# Найти минимальное  число которое отсуствует в данном нам списке и вывести на 
# экран.


def min_no(list1,m,l):
    newlist=[]
    for i in range(m,l):
        if  i not in list1:
            newlist.append(i)
    x=min(newlist)
    print('Минимальный отсутствующий элемент=', x)
list1=[9,10,11,17]
c=min(list1)
h=max(list1)
print(list1)
min_no(list1,c,h)