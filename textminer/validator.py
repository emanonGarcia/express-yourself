import re


def binary(string):
    return re.findall(r'^([0-1]+)$', string)


def binary_even(string):
    return re.findall(r'^([0-1]+0)$', string)


def hex(string):
    return re.findall(r'^[A-Fa-f0-9]+$', string)


def word(string):
    return re.search(r'^\b[\w-]*[a-zA-Z]+\b$', string)


def words(string, count=None):
    result = re.findall(r'\b[\w]*[-]*[A-Za-z]+\b', string)
    return len(result) == count if count else result


def phone_number(string):
    return re.search(r'[(]?[0-9]{3}[)]?[\D]?[0-9]{3}[\D]?[0-9]{4}', string)


def money(string):
    return re.search(r'^\${1}[0-9]{1,3}?(\,?[0-9]{3})*(\.[0-9]{2})?$', string)


def zipcode(string):
    return re.search(r'^[0-9]{5}(-[0-9]{4})?$', string)


def date(string):
    return re.search(r'^[0-9]{1,4}[-/][0-9]{1,2}[-/][0-9]{2,4}', string)
