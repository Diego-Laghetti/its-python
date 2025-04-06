#esercizio6-11
cities = {
    "Rome": {
        "country": "Italy",
        "population": "2,7 million",
        "fact": "Rome is known for its iconic Colosseum."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is the largest metropolitan area in the world by population."
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Paris is known for its iconic Eiffl Tower."
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")