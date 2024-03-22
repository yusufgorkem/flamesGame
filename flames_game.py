name1 = input("Please enter the name1: ")
set_name1 = name1.lower().replace(" ", "")
name2 = input("Please enter the name2: ")
set_name2 = name2.lower().replace(" ", "")

for i in set_name1:
    for j in set_name2:
        if i == j:
            set_name1 = set_name1.replace(i, "", 1)
            set_name2 = set_name2.replace(j, "", 1)
            break

count = len(set_name1 + set_name2)
if count > 0:
    relation = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    while len(relation) > 1:
        index_to_remove = count % len(relation) - 1
        if index_to_remove > 0:
            left = relation[:index_to_remove]
            right = relation[index_to_remove + 1:]
            relation = right + left
        else:
            relation = relation[:len(relation) - 1]

    print("{} and {} are {}".format(name1, name2, relation[0]))
else:
    print("Please enter different names!")
