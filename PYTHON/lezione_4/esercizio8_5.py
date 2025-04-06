#esercizio8-5
def describe_city(country: str= "Italia", city: str = "Roma"):
    print(f"{city} è in {country}")

describe_city()
describe_city(city="Milano nebbiosa")
describe_city(country="Egitto", city="Sharm El Sheikh")