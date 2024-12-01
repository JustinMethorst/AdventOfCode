# Initialize the arrays for storing the data
first_part_data = []
second_part_data = []

# Open the txt file and read it
with open("C:\\Projects\\AdventOfCode\\2024\\day1data.txt", "r") as file:
    # Loop through each line in the file
    for line in file:
        # Split the line by whitespace
        parts = line.split()
        
        # Ensure that there are at least two parts
        if len(parts) >= 2:
            # Append the first part to the first array
            first_part_data.append(int(parts[0]))  # Assuming data is integers
            # Append the second part to the second array
            second_part_data.append(int(parts[1]))  # Assuming data is integers

# Function to process the arrays (sorting, taking lowest two, and calculating the difference)
def process_arrays(first_data_array, second_data_array):
    # Sort both arrays in ascending order
    first_data_array.sort()
    second_data_array.sort()

    result = []
    
    # Continue processing while there are at least two elements left in both arrays
    while len(first_data_array) >= 1 and len(second_data_array) >= 1:
        # Take the lowest two elements from each array
        lowest_first_array = first_data_array.pop(0)
        lowest_second_array = second_data_array.pop(0)

        # Calculate the difference and store it in the result array
        difference = abs(lowest_first_array - lowest_second_array)
        result.append(difference)
    
    return result
#part two
# Function to process the arrays (sorting, taking lowest two, and calculating the difference)
def process_arrays_two(first_data_array, second_data_array):
    # Sort both arrays in ascending order
    first_data_array.sort()
    second_data_array.sort()

    results = []
    
    # Continue processing while there are at least two elements left in both arrays
    while len(first_data_array) >= 1 and len(second_data_array) >= 1:
        # Take the lowest two elements from each array
        lowest_first_array = first_data_array.pop(0)
        # print(lowest_first_array)

        # Calculate the difference and store it in the result array
        times_in_list = second_data_array.count(lowest_first_array)
        sumresult = lowest_first_array * times_in_list
        
        results.append(sumresult)
    
    return results
    
# Process the first and second arrays
# difference = process_arrays(first_part_data, second_part_data)
# total_difference = sum(difference)
part_two_total = process_arrays_two(first_part_data, second_part_data)

# Output the results for testing
# print("Differences:", difference)
# print("Total Difference part one:", total_difference)
print("Total Difference part two", sum(part_two_total))

