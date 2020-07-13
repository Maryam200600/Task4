# Напишите код, который запишет  данные в файлы ниже.
# Например данные офисы Google:
# google_kazakstan.txt
# google_paris.txt
# google_uar.txt
# google_kyrgystan.txt
# google_san_francisco.txt
# google_germany.txt
# google_moscow.txt
# google_sweden.txt
# Когда пользователь скажет «Привет»
# Ваш код должен сообщать и давать выбор из перечисленных офисов. 
# После этого должен получить жалобу от пользователя и записать ее в файл, выбранный пользователем.

print('Hello!')
print('************************')
print('* Cities:              *')
print('* 1.Kazakstan          *')
print('* 2.Paris              *') 
print('* 3.UAR                *')
print('* 4.Kyrzystan          *')
print('* 5.San-francisko      *')
print('* 6.Germany            *')
print('* 7.Moscow             *')
print('* 8.Sweden             *')
print('************************')
name_city=input('Enter tour city:')
if name_city=='1':
    file1=open('google_kazakstan.txt','a')
elif name_city=='2':
    file1=open('google_paris.txt','a')
elif name_city=='3':
    file1=open('google_uar.txt','a')
elif name_city=='4':
    file1=open('google_kyrzystan.txt','a')
elif name_city=='5':
    file1=open('google_san-francisko.txt','a')
elif name_city=='6':
    file1=open('google_germany.txt','a')
elif name_city=='7':
    file1=open('google_moscow.txt','a')
elif name_city=='8':
    file1=open('google_sweden.txt','a')
else:
    print('error!')
file1.write('\n'+input('enter your complaint:'))
file1.close()