def sorting_dictionaries(list_of_dicts, sort_key):
    return sorted(list_of_dicts, key=lambda x: x.get(sorting_keys))
input_dictionaries = input("Enter a list of dictionaries in JSON format: ")
list_of_dicttionaries = eval(input_dictionaries)
sorting_keys = input("Enter the key to sort the list of dictionaries: ")
sorted_dictionaries = sorting_dictionaries(list_of_dicttionaries, sorting_keys)
for item in sorted_dictionaries:
    print(item)
