# In the python console
import requests
import json
import os
import random
from pprint import pprint


def generatePageNum(visitedPages):
    pageNum = random.randint(1,35) 
    while pageNum in visitedPages:
        pageNum = random.randint(1,35)
    return pageNum

def getPage(pageNum):
    url = 'https://wger.de/api/v2/exercise/?page=' + str(pageNum)
    #print("Requesting new page" + str(pageNum))
    headers = {'Accept': 'application/json',
         'Authorization':'28aafca4b20580c072fe3c87722eca33e13138ac'}
    r = requests.get(url=url,headers=headers)
    results = json.loads(r.content)["results"]
    return results
    #pprint(results)
def cleanDescription(description):
    string = description[:len(description)-4]
    string = string[3:]
    return string

# def getExercises(category, n):

#     category = int(category)
#     exercises = []
#     pagesVisited = set()
#     while len(exercises)  < n:
#         #print("here")
#         pageNum = generatePageNum(pagesVisited)
#         pagesVisited.add(pageNum)
#         routines = getPage(pageNum)
#         for exercise in routines:
#             exerciseObject = {}
        
#             if len(exercise["equipment"]) == 0 and exercise["language"] == 2 and exercise["category"] == category:
#                 name  = exercise["name"]
#                 if name == "<p></p>":
#                     exerciseObject["name"] = "None"
#                 else:
#                     exerciseObject["name"] = exercise["name"]
#                 #description = cleanDescription(exercise["description"])
#                 description = exercise["description"]
#                 if description == "":
#                     exerciseObject["description"] = "None"
#                 else:
#                     exerciseObject["description"] = description
#                 if "with" not in exerciseObject["description"]:
#                     exercises.append(exerciseObject)

    # return exercises

def getExercises(category,n):
    TEST_FILENAME = os.path.join(os.path.dirname(__file__), 'Exercises.json')
    exercisesData = json.load(open(TEST_FILENAME))
    categoryExercises = exercisesData[category]
    exercisesIndexes = random.sample(range(len(categoryExercises)), n)
    resultExercises = []
    for i in exercisesIndexes:
        resultExercises.append(categoryExercises[i])
    
    #pprint(resultExercises)
    return resultExercises
def createExerciseObjects():
    exerciseData ={
        10:[],
        12:[],
        8:[],
        14:[],
        11:[],
        9:[],
        13:[]
    }
    for pageNum in range(1,35):
        page = getPage(pageNum)
        for exercise in page:
            category = exercise["category"]
            exerciseObject = {}
            if len(exercise["equipment"]) ==0 and exercise["language"] == 2:
                name  = exercise["name"]
                if name == "<p></p>":
                    exerciseObject["name"] = "None"
                else:
                    exerciseObject["name"] = exercise["name"]
                #description = cleanDescription(exercise["description"])
                description = exercise["description"]
                if description == "":
                    exerciseObject["description"] = "None"
                else:
                    exerciseObject["description"] = description
                if "with" not in exerciseObject["description"]:
                    exerciseData[category].append(exerciseObject)
    with open('Exercises.json', 'w') as fp:
        json.dump(exerciseData, fp)
if __name__ == "__main__":
    # getPage(1)
    #pprint(getExercises(9,3))
    #createExerciseObjects()
    getExercises("10",10)

