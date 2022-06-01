count=int(input('Введите любое число  '))
day=count//86400
day_1=day%86400
hour=day_1//3600
hour_1=day_1%3600
min=hour_1//60
min_1=hour_1%60
sec=min_1
print(day, 'дней', hour, 'часов', min, 'минут', sec, 'секунд')
