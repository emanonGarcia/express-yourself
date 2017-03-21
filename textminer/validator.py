import re

def binary(bin_num):
    if len(bin_num) > 0:
        raw = re.findall(r'[0-1]+', bin_num)
        if bin_num in raw:
            if int(raw[0], 2) == int(bin_num, 2):
                return True
    else:
        return False

def binary_even(bin_num):
    if binary(bin_num) and int(bin_num, 2) % 2 == 0:
        return True
