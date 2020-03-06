import re


def change_char(s, p, r):
    return s[:p] + r + s[p + 1:]


def parse_phone_number(text):
    numbers = re.findall(r"\d+", text)

    if numbers is None:
        return None

    res = re.search(r"([87])([7])\d{9}|([7])\d{9}", ''.join(numbers))

    if res is None:
        return None

    phone_number = res.group()

    if phone_number[0] == "8":
        phone_number = change_char(phone_number, 0, "7")

    if len(phone_number) == 10:
        phone_number = "7{0}".format(phone_number)

    return int(phone_number)