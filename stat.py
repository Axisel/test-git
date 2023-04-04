import math

def calculate_standard_deviation(numbers):
    # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Calculate the variance
    variance = sum([((num - mean) ** 2) for num in numbers]) / len(numbers)

    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)

    # Create a summary string
    summary = f"The standard deviation of the list {numbers} is {standard_deviation:.2f}"

    # Return the summary string
    return summary