# Напишите калькулятор с возможностью находить сумму, разницу, так
# же делить и умножать. (используйте функции).А так же добавьте
# проверку не собирается ли пользователь делить на ноль, если так, то
# укажите на ошибку.

def summa(x,y):
    z=0
    z=x+y
    return z

def difference(x,y):
    z=0
    z=x-y
    return z

def multiplication(x,y):
    z=1
    z=x*y
    return z

def division(x,y):
    z=1
    if y>0:
        z=x/y
        return z
    else:
        return'error'
    

a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=input('enter action:')
if c=='+':
    print(summa(a,b))
elif c=='-':   
    print(difference(a,b))
elif c=='*':
    print(multiplication(a,b))
elif c=='/':
    print(division(a,b))
else:
    print('error')