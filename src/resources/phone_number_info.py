class PhoneNumberInfo:
    sector = str

    def __init__(self, number: str, prefix: str):
        self.number = number
        self.prefix = prefix

    def get_number(self):
        return self.number

    def get_prefix(self):
        return self.prefix

    def get_sector(self):
        return self.sector

    def set_sector(self, new_sector):
        self.sector = new_sector


def is_number_valid(number: str) -> bool:
    if number.isdigit():
        if len(number) == 3:
            return True
        elif 6 < len(number) < 13:
            return True
        else:
            return False
    else:
        return False
