import os
from flask import app

from src.resources.phone_number_info import is_number_valid, PhoneNumberInfo


class Validator:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def validated_numbers(self):
        phone_info = []
        eligible_prefixes = get_prefixes()
        for number in self.numbers:
            for eligible_prefix in eligible_prefixes:
                number_without_indicator = remove_indicator(number)
                number_prefix = number_without_indicator[:(len(eligible_prefix) - 1)]
                if number_prefix == eligible_prefix.strip('\n'):
                    if is_number_valid(number_without_indicator):
                        phone_info.append(PhoneNumberInfo(number, number_prefix))
                        break
        return phone_info


def remove_indicator(number: str):
    if "+" in number:
        number = number[1:]
    elif number[:2] == "00":
        number = number[2:]
    return number.replace(" ", "")


def get_prefixes():
    file_path = "C:\\Users\\rafae\\PycharmProjects\\talkdesk_challenge\\src\\resources\\prefixes.txt"
    filename = os.path.join(app.instance_path, 'prefixes.txt')

    try:
        f = open(filename, 'r')
    except OSError:
        raise Exception('File path not found')
    lines = f.readlines()
    return lines
