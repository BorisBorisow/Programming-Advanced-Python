def start_spring(**kwargs):
    spring_elements = {}
    result = []
    for value, key in kwargs.items():
        if key not in spring_elements:
            spring_elements[key] = [value]
        else:
            spring_elements[key].append(value)

    sorted_spring_elements = sorted(spring_elements.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_spring_elements:
        result.append(f"{key}:")

        for v in sorted(value):
            result.append(f"-{v}")
    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
