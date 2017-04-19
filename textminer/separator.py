import re


def words(input):
    matches = re.findall(r'[A-Za-z0-9\-]*[A-Za-z][A-Za-z0-9]*', input)
    if len(matches) != 0:
        return matches


def phone_number(input):
    m = re.search(r'[(]*(?P<area>[0-9]{3})[\D]*'
                  r'(?P<first>[0-9]{3})[\D]*(?P<last>[0-9]{4})', input)
    if m:
        return {'area_code': m.group('area'),
                'number': m.group('first') + "-" + m.group('last')}

    return m


def money(input):
    m = re.search(r'^(?P<curr>[$]{1})'
                  r'(?P<amnt>[0-9]+([.]{1}[0-9]{2})*$'
                  r'|([0-9]+([,]{1}[0-9]{3})+([.]{1}[0-9]{2})*))', input)
    if m:
        return {'currency': m.group('curr'),
                'amount': float(re.sub(',', '',  m.group('amnt')))}
    # return m


def zipcode(text):
    m = re.search(r'^(?P<first5>[0-9]{5})'
                  r'([-](?P<plus4>[0-9]{4})){0,1}$', text)
    if m:
        return {'zip': m.group('first5'),
                'plus4': m.group('plus4')}
    # return m


def date(input):
    pattern = r'(?P<month>[0-9]{1,2})(?P<day>[?/]{1}[0-9]+)(?P<year>[?/]{1}[0-9]+)'
    m = re.search(pattern, input)


    n = re.search(r'^(?P<year>[0-9]{4})'
                  r'(?P<month>[-]{1}[0-9]{2})'
                  r'(?P<day>[-]{1}[0-9]+)', input)
    if m:
        return {'month': int(re.sub('/', '',  m.group('month'))),
                'day': int(re.sub('/', '',  m.group('day'))),
                'year': int(re.sub('/', '',  m.group('year')))}
    if n:
        return {'month': int(re.sub('-', '',  n.group('month'))),
                'day': int(re.sub('-', '',  n.group('day'))),
                'year': int(re.sub('-', '',  n.group('year')))}
