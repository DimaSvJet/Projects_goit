from collections import UserDict

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
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return change_contact(args, contacts)
    else: 
        contacts[name] = phone
        return "Contact added."

@input_error("Give me name and phone, please.")
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return add_contact(args, contacts)
    
@input_error("Enter user name, please.")
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return f'{phone}'
    else:
        return "Sorry, we don't have contact with that name"

def show_all(contacts):
    contacts_list = ''
    for i, (name, phone) in enumerate(contacts.items(), start = 1):
        contacts_list += '{}. {} : {}\n'.format(i, name, phone)
    return contacts_list

def main():
    contacts = {}
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
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

