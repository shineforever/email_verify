import hashlib, random, string


def get_token(id, name, time):
    data = "%s%s%s" % (id, name, time)
    hash_md5 = hashlib.md5(data)
    return hash_md5.hexdigest()


def get_authcode(length=20):
    char_set = list(string.digits + string.ascii_letters)
    random.shuffle(char_set)
    return "".join(char_set[:length])
