def types_of_file(type_of_extension_list, filenames):
    types_of_extension_pairs = type_of_extension_list.split(';')
    extension_to_type = {}
    result = {}

    for pair in types_of_extension_pairs:
        extension, file_type = pair.split(',')
        extension_to_type[extension] = file_type

    for filename in filenames:
        file_parts = filename.split('.')
        if len(file_parts) > 1:
            extension = file_parts[-1]
            file_type = extension_to_type.get(extension, 'unknown')
            result[filename] = file_type
        else:
            result[filename] = 'unknown'

    return result

extension_type_list = input("Enter extensions and its type values : ")
filenames = input("Enter a list of filenames separated by spaces: ").split()

file_types = types_of_file(extension_type_list, filenames)
for filename, file_type in file_types.items():
    print(f"{filename}: {file_type}")
