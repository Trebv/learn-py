temperature = int(input("Temperature: "))
will_rain_input = input("Will it rain (yes/no): ")
will_rain = True if will_rain_input == "yes" else False

print("Wear jeans and a T-shirt")

if temperature <= 20:
    print("I recommend a jumper as well")

if temperature <= 10:
    print("Take a jacket with you")

if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if will_rain:
    print("Don't forget your umbrella!")