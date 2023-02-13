import re

from constant.days_info import list_days
from models import timezone
from models.amount_hour import AmountHour


def read_data_file(path_file):
    try:
        with open(path_file) as f:
            lines_read = f.readlines()

        return True, lines_read
    except FileNotFoundError:
        return False, None


def validate_amount_payment(info_payment, amount_hour_value, index_line):
    validate_line = re.findall(
        "([a-zA-Z]+)(=)((MO|TU|WE|TH|FR|SA|SU)([0-2]([0-9]))(:)(0([0-2]))(-)([0-2]([0-9]))(:)(0([0-1]))(,|.{0}))+",
        info_payment)

    if len(validate_line) == 0:
        return "The line number {0} is not valid for process".format(index_line)

    amount_payment = 0
    amounts_worked = get_worked_days(info_payment.split('=')[1])
    person_worked = info_payment.split('=')[0]
    for item_worked in amounts_worked:
        for item_amount in amount_hour_value:
            if item_worked.day_name == item_amount.day_name and item_worked.hour == item_amount.hour:
                amount_payment = amount_payment + item_amount.amount
                break

    return 'The amount to pay : {0} is {1}'.format(person_worked, amount_payment)


def get_worked_days(info_payment):
    amounts_worked = []

    for item_payment in info_payment.split(','):
        day_name_payment = item_payment[0:2]
        hours_payment = item_payment[2:].split('-')
        get_amount_hour(timezone.Timezone(hours_payment[0], hours_payment[1], 0), amounts_worked, day_name_payment)

    return remove_duplicates_hour(amounts_worked)


def validate_exist_hour(current_hour, amounts_worked):
    for item in amounts_worked:
        if item.hour == current_hour.hour and item.day_name == current_hour.day_name:
            return True
    return False


def remove_duplicates_hour(amounts_worked):
    amounts_worked_result = []
    for item_amount in amounts_worked:
        if validate_exist_hour(item_amount, amounts_worked_result) is False:
            amounts_worked_result.append(item_amount)

    return amounts_worked_result


def define_amount_hour(list_days_info):
    amount_hour_value = []

    for index_day in range(len(list_days_info)):
        get_amount_hour(list_days_info[index_day].morning, amount_hour_value, list_days_info[index_day].name_day)
        get_amount_hour(list_days_info[index_day].noon, amount_hour_value, list_days_info[index_day].name_day)
        get_amount_hour(list_days_info[index_day].night, amount_hour_value, list_days_info[index_day].name_day)

        result_validate = is_list_empty(amount_hour_value, list_days_info[index_day])

        if len(result_validate) > 0 :
            raise Exception(','.join(result_validate))

    return amount_hour_value


def is_list_empty(amount_hour_value, current_day):
    hours_of_day = list(filter(lambda item_day: item_day.day_name == current_day.name_day, amount_hour_value))
    alerts = []
    for index_hour in range(0, 24):
        if len(list(filter(lambda hour_find: hour_find.hour == index_hour, hours_of_day))) == 0:
            alerts.append("The day {0} not contain hour {1}".format(current_day.name_day, index_hour))

    return alerts


def get_amount_hour(timezone_day, amount_hour_value, name_day):
    try:
        start_hour_int = int(timezone_day.start_hour.split(':')[0])
        end_hour_int = int(timezone_day.end_hour.split(':')[0])

        if end_hour_int > start_hour_int:
            for index_hour in range(start_hour_int, end_hour_int):
                amount_hour_value.append(AmountHour(index_hour, timezone_day.amount_hour, name_day))
        else:
            for index_hour in range(start_hour_int, 24):
                amount_hour_value.append(AmountHour(index_hour, timezone_day.amount_hour, name_day))

        return None
    except AttributeError:
        message = "Invalid values for defined amounts"
        print(message)
        return message
    except ValueError:
        message = "The hour parametrized is invalid"
        print(message)
        return message


if __name__ == "__main__":
    result, lines_file = read_data_file('files/data.txt')

    if result:
        amount_hour_by_day = define_amount_hour(list_days)
        for index_line in range(len(lines_file)):
            print(validate_amount_payment(lines_file[index_line], amount_hour_by_day, index_line))
    else:
        print("File not found or not exist")
