def is_book_isbn_Validation (isbn):
    tostr = str(isbn)
    num = tostr.replace('-','')
    if(not(num.isnumeric())):
        return 0
    length = len(num)
    if(not((length==10) or (length==13))):
        return 0
    if(length==10):
        num = "978"+num
    num = int(num)
    result = 0
    for x in range(6):
        r = num % 10
        result = result+(r * 1)
        num = int(num / 10)
        r = num % 10
        result = result + (r * 3)
        num = int(num / 10)
    result = result + (num)
    if (result % 10 == 0):
        return result
    return 0