def max_calories(input_str):
    # Split the input by blank lines to get each Elf's list of food items
    elf_lists = input_str.strip().split("\n\n")

    # Calculate the total Calories for each Elf
    total_calories = [sum(map(int, elf_list.split("\n"))) for elf_list in elf_lists]

    # Return the maximum total Calories
    return max(total_calories)


def top_three_calories(input_str):
    # Split the input by blank lines to get each Elf's list of food items
    elf_lists = input_str.strip().split("\n\n")

    # Calculate the total Calories for each Elf
    total_calories = [sum(map(int, elf_list.split("\n"))) for elf_list in elf_lists]

    # Sort the list in descending order and sum the top three values
    return sum(sorted(total_calories, reverse=True)[:3])


# Read the data from the file
with open("data.txt", "r") as file:
    input_str = file.read()

# Get the result part one and print it
print(max_calories(input_str))

# Get the result part two and print it
print(top_three_calories(input_str))