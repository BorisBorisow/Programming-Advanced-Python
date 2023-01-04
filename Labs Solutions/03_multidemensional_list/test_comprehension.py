mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(mm)
print(
    # [v+1 for v in ll]
    # a new list for each list in MD list
    # nested comprehensions
    [[v + 1 for v in row] for row in mm]
)

print(
    # MD comprehension
    # Flattening comprehension
    [
        v + 1 for row in mm for v in row
        # v + 1
        # for row in mm
        #     for v in row
    ]
)