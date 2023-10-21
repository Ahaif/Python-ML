kata = (2019, 9, 25, 3, 30)

# Extract individual values from the tuple
year, month, day, hour, minute = kata

# Format the date and time components
formatted_date = f"{month:02d}/{day:02d}/{year}"
formatted_time = f"{hour:02d}:{minute:02d}"

# Combine them and display the result
formatted_datetime = f"{formatted_date} {formatted_time}"
print(formatted_datetime)
