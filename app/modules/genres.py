def getMusicGenres(personality):

    returnArray = ["", ""]

    if personality == "Extraverted":
        returnArray[0] = "Pop"
        returnArray[1] = "Rap"

    elif personality == "Agreeable":
        returnArray[0] = "Alternative Rock"
        returnArray[1] = "R&B"

    elif personality == "Conscientious":
        returnArray[0] = "Dance Pop"
        returnArray[1] = "R&B"

    elif personality == "Emotionally Stable":
        returnArray[0] = "Classic Rock"
        returnArray[1] = "Melodic Rap"

    elif personality == "Open to New Experiences":
        returnArray[0] = "Alternative Rock"
        returnArray[1] = "Country"

    elif personality == "Thinker":
        returnArray[0] = "Background Music"
        returnArray[1] = "Melodic Rap"

    elif personality == "Performer":
        returnArray[0] = "Hip Hop"
        returnArray[1] = "Pop"

    elif personality == "Care Giver":
        returnArray[0] = "Country"
        returnArray[1] = "Mellow Pop"

    return returnArray


def getBookGenres(personality):

    returnArray = ["", ""]

    if personality == "Extraverted":
        returnArray[0] = "Adventure"
        returnArray[1] = "Science Fiction"

    elif personality == "Agreeable":
        returnArray[0] = "nonfiction"
        returnArray[1] = "History"

    elif personality == "Conscientious":
        returnArray[0] = "Thriller"
        returnArray[1] = "Crime"

    elif personality == "Emotionally Stable":
        returnArray[0] = "Biography"
        returnArray[1] = "Poetry"

    elif personality == "Open to New Experiences":
        returnArray[0] = "Dystopia"
        returnArray[1] = "Mystery"

    elif personality == "Thinker":
        returnArray[0] = "Science"
        returnArray[1] = "Dystopia"

    elif personality == "Performer":
        returnArray[0] = "Science Fiction"
        returnArray[1] = "Thriller"

    elif personality == "Care Giver":
        returnArray[0] = "Drama"
        returnArray[1] = "Satire"

    return returnArray


def getMovieGenres(personality):

    returnArray = ["", ""]

    if personality == "Extraverted":
        returnArray[0] = "Adventure"
        returnArray[1] = "Action"

    elif personality == "Agreeable":
        returnArray[0] = "Documentary"
        returnArray[1] = "History"

    elif personality == "Conscientious":
        returnArray[0] = "Action"
        returnArray[1] = "Crime"

    elif personality == "Emotionally Stable":
        returnArray[0] = "Family"
        returnArray[1] = "History"

    elif personality == "Open to New Experiences":
        returnArray[0] = "Horror"
        returnArray[1] = "Mystery"

    elif personality == "Thinker":
        returnArray[0] = "Documentary"
        returnArray[1] = "War"

    elif personality == "Performer":
        returnArray[0] = "Science Fiction"
        returnArray[1] = "Thriller"

    elif personality == "Care Giver":
        returnArray[0] = "Drama"
        returnArray[1] = "Comedy"

    return returnArray


def getNthMovieGenres(personalities):
    allMovieGenres = []
    for i in range(len(personalities)):
        allMovieGenres = allMovieGenres + getMovieGenres(personalities[i])
    print(allMovieGenres)
    return allMovieGenres

def getNthMusicGenres(personalities):
    allMusicGenres = []
    for i in range(len(personalities)):
        allMusicGenres = allMusicGenres + getMusicGenres(personalities[i])
    print(allMusicGenres)
    return allMusicGenres


def getNthBookGenres(personalities):
    allBookGenres = []
    for i in range(len(personalities)):
        allBookGenres = allBookGenres + getBookGenres(personalities[i])
    print(allBookGenres)
    return allBookGenres