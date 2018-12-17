

def index2base62(index):
    if index < 0:
        raise ValueError('the value should be greater than 0')
    elif 0 <= index <= 9:
        return str(index)
    elif index <= 35:
        return str(unichr(index + 55))
    elif index <= 61:
        return str(unichr(index + 61))
    else:
        raise ValueError('the index should be no greater than 61')


def base622index(base62):
    if 'A' <= base62 <= 'Z':
        print ord(base62)
        return ord(base62) - 55
    elif 'a' <= base62 <= 'z':
        print ord(base62)
        return ord(base62) - 61
    elif '0' <= base62 <= '9':
        return int(base62)


def base2int(base):
    result = 0
    total_length = len(base)
    for i in range(len(base)):
        result += base622index(base[i]) * pow(62,(total_length - i -1))
    return result



if __name__ == '__main__':
    # try:
    #     print index2base62(67)
    # except ValueError, e:
    #     print e.message
    # i = 10
    # reminder = i
    # result=''
    # while i != 0:
    #     reminder = i % 62
    #     i = i / 62
    #     result += index2base62(reminder)
    # print result[::-1]

    print base2int('1A')
