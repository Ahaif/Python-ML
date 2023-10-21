kata = (0, 4, 132.42222, 10000, 12345.67)

# Extract individual values from the tuple
val1, val2, val3, val4, val5 = kata

# Format the values as per the specified format
formatted_val1 = f"{val1:02d}"
formatted_val2 = f"{val2:02d}"
formatted_val3 = f"{val3:.2f}"
formatted_val4 = f"{val4:.2e}"
formatted_val5 = f"{val5:.2e}"

# Create the final formatted string
formatted_string = f"module_{formatted_val1}, ex_{formatted_val2} : {formatted_val3}, {formatted_val4}, {formatted_val5}"

# Print the formatted string
print(formatted_string)
