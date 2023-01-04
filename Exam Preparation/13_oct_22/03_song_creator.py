def add_songs(*args):
    songs = {}

    for arg in args:
        title, lyrics = arg
        # songs[title] = songs.get(title, []) + [lyrics]
        if title not in songs:
            songs[title] = []

        songs[title].extend(lyrics)

    output = []
    for song, lyr in songs.items():
        output.append("- " + song)
        output.extend(lyr)

    return '\n'.join(output)
    return os.linesep(output )

print(add_songs(("Bohemian Rhapsody", []), ("Just in Time", ["Just in time, I found you just in time",
                                                             "Before you came, my time was running low",
                                                             "I was lost, the losing dice were tossed",
                                                             "My bridges all were crossed, nowhere to go"])))
