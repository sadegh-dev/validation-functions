
from re import fullmatch


def is_valid(email):
    """
    (username)@(domainname).(top-leveldomain)
    (string1)@(string2).(2+characters)
    """
    import re
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        pass

