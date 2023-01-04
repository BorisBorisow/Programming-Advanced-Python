def negatives_positives(numbers):
    negative = [x for x in numbers if x < 0]
    positive = [x for x in numbers if x >= 0]

    def sum_negatives(negative):
        return sum(negative)

    def sum_positives(positive):
        return sum(positive)

    def who_is_stronger(positive, negative):
        if abs(sum(positive)) > abs(sum(negative)):
            return "The positives are stronger than the negatives"
        else:
            return "The negatives are stronger than the positives"

    return f"""{sum_negatives(negative)} 
{sum_positives(positive)}
{who_is_stronger(positive, negative)}"""

numbers = list([int(x) for x in input().split()])
print(negatives_positives(numbers))

