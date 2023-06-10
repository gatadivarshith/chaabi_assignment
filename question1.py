def sorting(list):
    for i in range(len(list)):
        minimum_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minimum_index]:
                minimum_index = j
        list[i], list[minimum_index] = list[minimum_index], list[i]

    return list
inputlist = input("Please enter a list of numbers with (,): ").split(",")
inputlist = [int(num) for num in inputlist]
updated_list = sorting(inputlist)
print("Your updated list is:", updated_list)
