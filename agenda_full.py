import pickle
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CSV = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CSV, ACTION_EXIT]

def ask_correct_opt(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("Elige un opción: ")

    return int(selected_action)

def show_menu():
    print("Acciones disponibles")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar contacto")
    print("4 - Exportar contactos de fichero CSV")
    print("5 - Salir")
    return ask_correct_opt(MENU_OPTIONS)


def add_contact(contacts):
    print("\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Telefono: "),
        "mail": input("Email: ")
        }
    contacts.append(contact)
    print("{} ha sido añadido".format(contact["name"]))
    sleep(2)

def remove_contact(contacts):
    pass


def find_contact(contacts):
    print("\n\nBuscar contacto:\n")
    search_term = input("Indique contacto ")
    found_contacts = []

    print("He encontrado los siguientes contactos: ")
    contact_indexes = []
    contact_counter = 0


    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{}  -  {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_correct_opt(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No existen contactos")
        return

    print("Datos del contacto {}".format(found_contacts[contact_index]))
    print("Nombre: {name}, Telefono: {phone}, Email: {mail}\n\n".format(**found_contacts[contact_index]))
    sleep(2)

def export_contact():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente")

def main():
    contacts = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:

        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)

        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)

        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)

        elif action == ACTION_EXPORT_CSV:
            export_contact()

        action = show_menu()

    save_contacts(contacts)
    print("Bye bye")

if __name__ == "__main__":
    main()

