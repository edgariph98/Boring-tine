import requests
import json

class Bored(object):
    def __init__(self):
        pass
    
    def getBored(self, limit  = 5):
        activities = []
        suggested_activities =  {}
        for i in range(limit):
            x = requests.get("http://www.boredapi.com/api/activity?maxaccessibility=0.1&maxprice=0.09").content
            x = json.loads(x)
            output  = {}
            output['Activity'] = x['activity']
            output['Type'] = x['type']
            if(x["price"] == ""):
                output["Price"] = "0"
            else:
                output['Price'] = x['price']

            if(x["link"] == ""):
                output['Link'] = "None"
            else:
                output['link'] = x['link']
            activities.append(output)
		#suggested_activities = json.dumps(activities)
        suggested_activities = activities
        return suggested_activities

if __name__ == '__main__':
    b = Bored()
    print(json.dumps(b.getBored(2),indent=1))