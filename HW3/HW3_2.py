from collections import UserDict, defaultdict
import datetime

class Birthday:
    def __init__(self, day, month, year):
        self.birthday = datetime.datetime(day, month, year)

    def __str__(self):
        return self.birthday.strftime('%d-%m-%Y')

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
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError
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
        self.birthday = None

    def add_phone(self, phone:Phone):
        if Phone.check_tel_number(self, phone):
            self.phones.append(phone)
    
    def find_index_phone(self, phone):
        find_phone = next((i for i, tel in enumerate(self.phones) if tel == phone), None)
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

    def add_birthday(self, day, month, year):
        try:
            self.birthday = Birthday(day, month, year)
        except ValueError:
            print("Invalid date. Please enter a valid date in the format: DD-MM-YYYY")


    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
        
    def list_phones(self):
        return self.phones[:]

class AddressBook(UserDict):
    def add_contact(self, contact):
        contact_data = {
            "name": contact.name,
            "phones": [phone for phone in contact.phones],
            "birthday": contact.birthday
        }
        self.data[contact.name] = contact_data
        print(f"Your contact {contact.name} has been added to AddressBook")
    
    def find_contact(self, name):
        if name in self.data:
            contact_data = self.data[name]
            formatted_data = {
                "name": contact_data["name"],
                "phones": contact_data["phones"],
                "birthday": contact_data["birthday"].__str__()
            }
            print(formatted_data)
            return self.data[name] 
        else:
            print('This contact is absent')

    def remove_contact(self, name):
        if self.find_contact(name):
            del self.data[name]
            print(f'Contact {name} has been removed')
    
    def show_birthday(self, name):
        if name in self.data:
            contact_data = self.data[name]
            birthday_datetime = contact_data["birthday"].birthday
            formatted_data = {
                "name": contact_data["name"],
                "birthday": birthday_datetime.strftime('%d-%m')
            }
            print(formatted_data)
        else:
            print('This contact is absent')


    def get_birthdays_per_week(self):
        current_date = datetime.datetime.today().date()
        birthday_people = defaultdict(list)

        for user_data in self.data.values():
            name = user_data['name']
            birthday_date = user_data['birthday'].birthday.date()
            birthday_this_year = birthday_date.replace(year=current_date.year)

            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(
                    year=birthday_this_year.year + 1)

            delta_days = (birthday_this_year - current_date).days
            if delta_days < 7:
                number_day_of_week = birthday_this_year.weekday()
                if number_day_of_week in (5, 6):
                    birthday_people['Monday'].append(name)
                else:
                    birthday_people[birthday_this_year.strftime('%A')].append(name)

        clean_result = dict(birthday_people)
        print(clean_result)
