import datetime
from collections import defaultdict


users = [
    {"name": "Bill Gates", "birthday": datetime.datetime(1955, 10, 28)},
    {"name": "Bill2", "birthday": datetime.datetime(1955, 10, 22)},
    {"name": "Bil3", "birthday": datetime.datetime(1955, 10, 25)}
]


def get_birthdays_per_week(users):
    current_date = datetime.datetime.today().date()
    birthday_people = defaultdict(list)

    for user in users:
        name = user['name']
        birthday_date = user['birthday'].date()
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

    return birthday_people


print(get_birthdays_per_week(users))
