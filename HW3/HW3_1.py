from collections import UserDict
from HW3_2 import AddressBook, Name, Phone, Birthday

def input_error(error_message=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error_message
            except TypeError:
                return error_message
            except IndexError:
                return error_message           
            except KeyError:
                return print("This name doesn't have any number")
        return inner
    return decorator

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error("Give me name and phone, please.")
def add_contact(args, book): #проверить! не работает - ссылается сюда find_contact
    name, phone = args
    contact = book.find_contact(name)
    if contact:
        return change_contact(args, book)
    else: 
        phone_record = Phone(phone) 
        new_contact = Name(name)
        new_contact.add_phone(phone_record) 
        book.add_contact(new_contact)
        return "Contact added."

@input_error("Give me name and phone, please.")
def change_contact(args, book):
    name, phone = args
    contact = book.find_contact(name)
    if contact:
        contact['phone'] = [Phone(phone)]
        return "Contact updated."
    else:
        return add_contact(args, book)
    
@input_error("Enter user name, please.")
def show_phone(args, book):
    name = args[0]
    contact = book.find_contact(name)
    if contact:
        phone = contact['phone'] #!!! Должно быть значение по ключу!!!!
        return f'{phone}'
    else:
        return "Sorry, we don't have contact with that name"

def show_all(book):
    return book.show_all()

def main():
    book = AddressBook() # Создали класс записной книги "book"
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            print("Please, enter your command")
            continue
        else:
            command, *args = parse_input(user_input)

        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))
        
        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

