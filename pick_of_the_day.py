from users import users
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # поточна дата
    current_date = datetime.now().date()

    # день поточного тижня, коли починається понеділок
    monday = current_date + timedelta(days=-current_date.weekday())

    # дата через тиждень
    next_week = monday + timedelta(weeks=1)

    birthday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }


    for user in users:
        name = user.get("name")
        birthday = user.get("birthday").date()

        if current_date <= birthday < next_week:
            if birthday.weekday() >= 5:  # Вихідний (субота або неділя)
                birthday = birthday + timedelta(days=(7 - birthday.weekday()))  # Переносимо на понеділок

            #день тижня з дати народження
            weekday = birthday.strftime("%A")

            birthday_dict[weekday].append(name)

    for weekday, names in birthday_dict.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

get_birthdays_per_week(users)




