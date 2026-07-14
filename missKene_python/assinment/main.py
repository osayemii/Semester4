from tempPackage import temp_conversion

input_celsius = float(input("Enter a temperature at celsius to convert to fahrenheit: "))
input_fahren = float(input("Enter a temperature at fahrenheit to convert to celsius: "))

fahrenheit = temp_conversion.Celsius_fahren(input_celsius)
celsius = temp_conversion.Fahren_celsius(input_fahren)

print(f"converted {input_celsius}∘C to {fahrenheit}∘F")
print(f"converted {input_fahren}∘F to {celsius}∘C")