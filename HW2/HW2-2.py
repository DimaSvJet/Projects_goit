from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
    
    def __str__(self):
        return "Name:" + super().__str__()


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.tel_number = None
    
    def check_tel_number(self, value):
        if type(value) == str and value.isdigit() and len(value) == 10:
            self.tel_number = value
            return self.tel_number
        else:
            self.tel_number = None

class Record:
    def __init__(self, name:Name):
        self.name = name
        self.phone = None
        self.phones = []

    def add_phone(self, phone:Phone):
        if Phone.check_tel_number(self, phone):
            self.phones.append(Phone(phone))
    
    def find_index_phone(self, phone):
        find_phone = next((i for i, tel in enumerate(self.phones) if tel.value == phone), None)
        return find_phone
    
    def remove_phone(self, phone):
        index_phone_to_remove = self.find_index_phone(phone)
        if index_phone_to_remove >= 0:
            self.phones.pop(index_phone_to_remove)
    
    def change_phone(self, old_phone, new_phone):
        index_phone_to_change = self.find_index_phone(old_phone)
        if index_phone_to_change >= 0:
            if Phone.check_tel_number(self, new_phone):
                self.phones[index_phone_to_change] = new_phone
    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
        
    def list_phones(self):
        return self.phones[:]

class AddressBook(UserDict):
    def add_contact(self, contact):
        contact_data = {
            "name": contact.name,
            "phones": [phone for phone in contact.phones]
        }
        self.data[contact.name] = contact_data
        print(f"Your contact {contact.name} has been added to AddressBook")
    
    def find_contact(self, name):
        if name in self.data:
            print(f'{self.data[name]}')
            return self.data[name] 
        else:
            print('This contact is absent')

    def remove_contact(self, name):
        if self.find_contact(name):
            del self.data[name]
            print(f'Contact {name} has been removed')


contact_1 = Record('Ivan')
contact_1.add_phone('0506088243')
contact_1.add_phone('0665871943')
contact_1.remove_phone('0506088243')
contact_1.change_phone('0665871943', '0506088243')
print(contact_1)
my_AddressBook = AddressBook()
my_AddressBook.add_contact(contact_1)
my_AddressBook.find_contact('Ivan')
my_AddressBook.remove_contact('Ivan')
my_AddressBook.remove_contact('Ivan')