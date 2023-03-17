import colorgram

color = colorgram.extract('hirst-painting.jpeg', 15)
print(color)

color_list = []
for _ in color:
    color_input = []
    for rgb in _.rgb:
        color_input.append(rgb)
    color_input = tuple(color_input)
    color_list.append(color_input)

print(color_list)