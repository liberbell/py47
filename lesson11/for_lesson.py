names = ["bob", "alex", "eric", "ed", "aletha"]
# print(names[0] + " san")
# print(names[1] + " san")
# print(names[2] + " san")
# print(names[3] + " san")
# print(names[4] + " san")

# for i in range(len(names)):
#     print(names[i] + " san")

# for name in names:
#     print(name + " san")

last_names = ["Clapton", "Mary", "Denvor", "Lenon", "Sheeran"]
first_names = ["Bob", "John", "Ed", "Eric", "Alex"]

# print(last_names[0] + first_names[0] + " san")
# print(last_names[1] + first_names[1] + " san")
# print(last_names[2] + first_names[2] + " san")
# print(last_names[3] + first_names[3] + " san")
# print(last_names[4] + first_names[4] + " san")

# for i in range(len(last_names)):
#     print(last_names[i] + first_names[i] + " san")

for last_name, first_name in zip(last_names, first_names):
    print(last_name, first_name + " san")

for i, last_name in enumerate(last_names):
    print("Number{} {} san", i, last_name)