import datetime
import random

AVERAGE_LIFESPAN = 80
SMOKER_PENAL = 10
DRINKER_PENAL = 5
SEDENTARY_PENAL = 3
year_lost = 0

def print_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_S_N(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + "[S/N]")
    return response == "S"

print_underscores("Averigua cuanto te queda de vida")
print("Introduce tus datos: ")

birth_date = input("Fecha de nacimineto [dd/mm/yyyy]: ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

if ask_S_N("Fumas?"):
    year_lost += SMOKER_PENAL
if ask_S_N("Bebes alcohol?"):
    year_lost += DRINKER_PENAL
if ask_S_N("Haces deporte?"):
    year_lost += SEDENTARY_PENAL

base_lifespam = random.randint(AVERAGE_LIFESPAN / 2, AVERAGE_LIFESPAN)
lifespam = base_lifespam - year_lost
death_day = birth_date + datetime.timedelta(days=lifespam*365)
days_to_death = death_day - datetime.datetime.now()

print("El día de tu muerte es: {}".format(death_day.strftime("%d/%m/%Y")))
print("Faltan {} dias para tu muerte". format(days_to_death.days))