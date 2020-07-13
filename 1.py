# Написать функцию season, принимающую 1 аргумент — номер месяца
#  (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(mounth):
    if  mounth==12 or mounth>=1 and mounth<=2:
        return 'winter'
    elif mounth>=3 and mounth<=5:
        return 'spring'
    elif mounth>=6 and mounth<=8:
        return 'summer'
    elif mounth>=9 and mounth<=11:
        return 'autumn'
    else:
        return 'error'
x=int(input('enter season: '))
print(season(x))