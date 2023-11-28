import datetime

def get_birthdays_per_week(users):

    current_date = datetime.date.today()
    people_with_birthday_next_week = []
    people_with_birthday_next_week_dict = {}
    message = (f'Today is {current_date.strftime("%A %d %B %Y")}\n')
    message += ('The following people have their birthdays next week:\n')

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_weeks = (birthday_this_year - current_date).days // 7

        if delta_weeks == 0 and (birthday_this_year.weekday() in (5, 6)):
            people_with_birthday_next_week.append(["Monday", name])
        elif delta_weeks == 1 and not (birthday_this_year.weekday() in (5, 6)):
            people_with_birthday_next_week.append(
                [birthday_this_year.strftime('%A'), name])

    for employee in people_with_birthday_next_week:
        day = employee[0]
        if day not in people_with_birthday_next_week_dict:
            people_with_birthday_next_week_dict[day] = []
        people_with_birthday_next_week_dict[day].append(employee[1])


    for key, value in people_with_birthday_next_week_dict.items():
        message += "{:<15}: {:<}\n".format(key, ', '.join(value))

    return message



if __name__ == "__main__":
    from faker import Faker

    fake = Faker()

    def get_fake_users(amount):
        users_list = []
        for i in range(amount):
            mock = {
                "name": fake.name(),
                "birthday": fake.date_object()
            }
            users_list.append(mock)
        return users_list

    users = get_fake_users(200)
    print(get_birthdays_per_week(users))