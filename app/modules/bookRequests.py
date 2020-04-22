from googleapiclient.discovery import build

import requests
import json

def search_books(genreSearch, numOfBooks):
    genreType = genreSearch
    fullLink = 'https://www.googleapis.com/books/v1/volumes?q=subject:' + genreType

    res = requests.get(fullLink)

    textFile = res.text
    data = json.loads(textFile)

    finalString = ""
    finalString = data['items']

    counter = 0


    returnList = []

    #loop through string
    for i in finalString:
        if counter < numOfBooks:
            counter = counter + 1
            #print(i)
            d = json.dumps(i)
            s = json.loads(d)

            #print("volume Info")
            #print(s['volumeInfo'])
            nextSection = s['volumeInfo']
            bookObject = {}
            #print("title")
            #print(nextSection['title'])
            bookObject['title'] = nextSection['title']
            #print("authors")
            #print(nextSection['authors'])
            try:
                bookObject['authors'] = nextSection['authors']
            except:
                bookObject['authors'] = ["None"]
            #print("webReaderLink")
            #print(nextSection['infoLink'])
            bookObject['link'] = nextSection['infoLink']
            #print("categories")
            #print(nextSection['categories'])
            bookObject['overview'] = nextSection["description"]
            bookObject['genre'] = nextSection['categories']
            returnList.append(bookObject)
    return returnList

def getAllBooks(genres, numOfBooks):
    bookCollection = []
    for i in range(len(genres)):
        books = search_books(genres[i],numOfBooks)
        bookCollection = bookCollection + books
    return bookCollection
#example usage!!
if __name__ == "__main__":
    # listGot = search_books('Science', 2)
    genres = [
        "Adventure",
        "Science Fiction",
        "History",
        "Thriller",
        "Crime",
        "Biography",
        "Poetry",
        "Dystopia",
        "Mystery",
        "Science",
        "Dystopia",
        "Science Fiction",
        "Thriller",
        "Drama",
        "Satire"]
    for genre in genres:
        try:
            search_books(genre,5)
        except:
            print(genre + " not valid")
    # allbooks = getAllBooks(genres,4)
    # print(json.dumps(allbooks,indent=1))
    # print(len(allbooks))
