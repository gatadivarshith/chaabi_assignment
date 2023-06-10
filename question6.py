def get_sublist(lst, start, end):
    sublist = lst[start:end:2]
    return sublist
input_list = input("Enter elements of the list, separated by spaces: ").split()
starting_index = int(input("Enter the starting index: "))
ending_index = int(input("Enter the ending index: "))
list_of_numbers = [int(element) for element in input_list]
sub_list = get_sublist(list_of_numbers, starting_index, ending_index)
print("Sub-list:", sub_list)
