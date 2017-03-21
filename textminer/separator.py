import re

def words(input):
    matches = re.findall(r'[A-Za-z0-9\-]*[A-Za-z][A-Za-z0-9]*', input)
    if len(matches) != 0:
        return matches


def phone_number(input):
    nums = re.findall(r'\d', input)
    if len(nums) == 10:
        return dict([('area_code', ''.join(nums[:3]) ), ('number', ''.join(nums[3:6]) + '-' + ''.join(nums[6:]))])


# Unfinished
def money(input):
    currency = re.findall(r'\$', input)
    if len(currency) == 1:
        amount = re.findall(r'[\d\.]+', input)
        if len(amount) > 0:
            if currency[0] == '$' and amount[0].isdecimal():
                return dict([('currency', currency[0]), ('amount', float(amount[0]))])



def zipcode(input):
    if len(input) == 5 or len(input) == 10:
        z_code = re.findall(r'^[0-9]{5}', input)
        z_code = z_code[0]
        if z_code == input:
            plus4 = None
        else:
            plus4 = re.findall(r'[0-9]{4}$', input)
            plus4 = plus4[0]
        return dict([('zip', z_code), ('plus4', plus4)])

def date(input):
    if len(input) >= 8:
        date = re.findall(r'\d*[^/-]', input)
        if '/' in input:
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])
        else:
            month = int(date[1])
            day = int(date[2])
            year = int(date[0])
        return dict([('month', month), ('day', day), ('year', year)])
