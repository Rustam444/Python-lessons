prices = {
    "Laptop": 700,
    "Phone": 350,
    "Camera": 1200
    }
son=0
natija=prices["Laptop"]
for keys, value in prices.items():
    if value>son:
        son=value
        natija=keys
print(f"{natija} narxi: {son}")