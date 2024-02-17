def reamur_to_celcius( reamur):
    celcius = (5/4)* reamur
    return celcius

def celcius_to_fahrenheit(celcius):
    fahrenheit =(celcius*9/5) + 32
    return fahrenheit

def celcius_to_kelvin(celcius):
    kelvin = celcius +273.15
    
reamur = float(input("Masukkan suhu dalam reamur:"))

celcius = reamur_to_celcius(reamur)
fahrenheit = celcius_to_fahrenheit(celcius)
kelvin = celcius_to_kelvin(celcius)

print("suhu dalam celcius:", celcius)
print("suhu dalam farhenheit:",fahrenheit)
print("suhu dalam kelvin:",kelvin)