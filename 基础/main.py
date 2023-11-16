import string

# 生成小写字母
lowercase_letters = string.ascii_lowercase

# 生成大写字母
uppercase_letters = string.ascii_uppercase

print("小写字母:", lowercase_letters)
print("大写字母:", uppercase_letters)


uppercase_to_lowercase = dict(zip(string.ascii_uppercase, string.ascii_lowercase))
lowercase_to_uppercase = dict(zip(string.ascii_lowercase, string.ascii_uppercase))

print("大写字母转小写字母的字典:", uppercase_to_lowercase)
print("小写字母转大写字母的字典:", lowercase_to_uppercase)


from collections import OrderedDict
