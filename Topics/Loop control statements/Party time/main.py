party_list = []

while True:
    name = input()
    if name == ".":
        break
    else:
        party_list += [name]

print(str(party_list))
print(len(party_list))