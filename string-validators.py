if __name__ == '__main__':
    s = input()

    has_alnum = any([i.isalnum() for i in list(s)])
    has_alpha = any([i.isalpha() for i in list(s)])
    has_digit = any([i.isdigit() for i in list(s)])
    has_lower = any([i.islower() for i in list(s)])
    has_upper = any([i.isupper() for i in list(s)])

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
