def words_sorting(*args):
    words = {word: sum(map(ord, word)) for word in args}
    sorted_words = {}
    result = []

    if sum(words.values()) % 2 == 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        sorted_words = dict(sorted(words.items(), key=lambda x: -x[1]))

    for key, value in sorted_words.items():
        result.append(f"{key} - {value}")

    return "\n".join(result)

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

