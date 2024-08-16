# Write a python program using function to convert Celsius to Fahrenheit.

def conversion():
    c = float(input("Enter a celsius reading : "))
    f = (c * (9/5))+ 32
    return f"The final value of celcis into farenhite is {round(f,2)}°F "

f = conversion()
print(f)