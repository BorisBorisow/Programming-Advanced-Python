def forecast(*args):
    weather = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = []

    for key, value in args:
        weather[value].append(key)

    for key, value in weather.items():
        for v in sorted(value):
            result.append(f"{v} - {key}")

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
