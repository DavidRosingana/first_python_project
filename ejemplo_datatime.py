import datetime

year = int(input("Dime el año: "))
month = int(input("Dime el mes: "))
day = int(input("Dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_rest = user_date - datetime.datetime.now()

print("Faltan {} dias y {} horas".format(time_rest.days, int(time_rest.seconds / 60 / 60)))
print("Mañana es: {}".format(datetime.datetime.now() + datetime.timedelta(days=1)))