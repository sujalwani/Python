def fahrenheit(cel):
    return (cel*9)/5+32

cel = int(input("Enter the temperature in cel : "))
far = fahrenheit(cel)
print(f"Temp in {cel} is in {far} ")