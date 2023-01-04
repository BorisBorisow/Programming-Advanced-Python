# -----------------------------50/100 Points----------------------

# def sorting_cheeses(**cheese_sort):
#     cheese_dict = sorted(cheese_sort.items(), key=lambda x: (-len([1]), x[0]))
#
#     result = []
#
#     for (name, quantities) in cheese_dict:
#         result.append(name)
#         #quantity_dict = sorted(quantities, reverse=True)
#         #result += quantity_dict
#         result.extend(sorted(quantities, reverse=True))
#     return "\n".join([str(x) for x in result])
#
#
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )


# 03. Cheese Showcase

def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for name, pieces in sorted_cheese:
        result += name + '\n'
        sorted_pieces = sorted(pieces, reverse=True)
        result += '\n'.join([str(x) for x in sorted_pieces]) + '\n'

    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)