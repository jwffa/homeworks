def generate_hashtag(s):
    a = '#'
    s = s.title()
    if s == "":
        return False
    for i in s:
        if i != ' ':
            a += i
    if len(a) > 140:
        return False
    return a
