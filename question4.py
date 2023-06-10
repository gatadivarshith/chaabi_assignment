def switch_position(dictionary):
    return {v: k for k, v in dictionary.items()}
give_input = input("Enter a dictionary in the format : ")
input_dictionary = eval(give_input)
output_dictionary = switch_position(input_dictionary)
print(output_dictionary)


