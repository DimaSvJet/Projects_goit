def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return change_contact(args, contacts)
    else: 
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return add_contact(args, contacts)

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