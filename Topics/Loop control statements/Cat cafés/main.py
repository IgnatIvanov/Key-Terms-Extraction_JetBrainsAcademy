cafe_name = ""
cafe_cats = 0

while True:
    in_str = input()
    if in_str == "MEOW":
        break
    else:
        str_2 = in_str.split()
        if int(str_2[1]) > cafe_cats:
            cafe_cats = int(str_2[1])
            cafe_name = str_2[0]
print(cafe_name)