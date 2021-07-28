# 要在字符串中插入变量的值，
# 可在前引号前加上字母f，
# 再将要插入的变量放在花括号内。
# 这样，当Python显示字符串时，将把每个变量都替换为其值。
#
# 这种字符串名为f字符串。
# f是format（设置格式）的简写，
# 因为Python通过把花括号内的变量替换为其值来设置字符串的格式。


first_name="ada"

last_name="lovelace"

full_name=f"{first_name} {last_name}"

print(full_name)