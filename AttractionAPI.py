import requests
import random

def AttractionData(city):
    randYN = input("Random city? (y/n): ")

    if randYN == 'n':
        url = "https://travel-advisor.p.rapidapi.com/locations/search"
        city = input("Enter desired city: ")
        print("Loading...")

        querystring = {"query":city,"limit":"30","offset":"0","units":"mi","location_id":"1","currency":"USD","sort":"relevance","lang":"en_US"}

        headers = {
            "X-RapidAPI-Key": "92b828dae2msh32f6193103ed4c6p1dcf00jsn0db7f7d743b4",
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
        }
        codeResponse = requests.request("GET", url, headers=headers, params=querystring)
        code = codeResponse.json()
        #print (codeResponse.text)
        cityCode = (code['data'][0]['result_object']['location_id'])

    elif randYN == 'y':
        cityCode = random.randint(10000,999999) 
        print("Loading...")

    while (True):
        url = "https://travel-advisor.p.rapidapi.com/attractions/list"

        querystring = {"location_id":str(cityCode),"currency":"USD","lang":"en_US","lunit":"km","sort":"recommended"}

        headers = {
            "X-RapidAPI-Key": "92b828dae2msh32f6193103ed4c6p1dcf00jsn0db7f7d743b4",
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
        }

        attractResponse = requests.request("GET", url, headers=headers, params=querystring)
        attract = attractResponse.json()
        print (cityCode)
        if ('errors'in attract) or (attract['paging']['results'] == "0"):
                cityCode=random.randint(10000,999999)
        else:
            break
    #########################################################################

    attractList, ratingList, thingsRankList, descriptList = [],[],[],[]

    #add attractions to attractions list
    for i in range(len(attract['data'])):
        if 'name' in attract['data'][i] and 'rating' in attract['data'][i] and 'ranking_subcategory' in attract['data'][i] and 'description' in attract['data'][i]:
            attraction = (attract['data'][i]['name'])
            rating = (attract['data'][i]['rating'])
            rank = (attract['data'][i]['ranking_subcategory'])
            descript = (attract['data'][i]['description'])

            attractList.append(attraction)
            ratingList.append(rating)
            thingsRankList.append(rank)
            descriptList.append(descript)
        if len(attractList) == 10:
            break

    #city = attract['data'][0]['ranking_geo']
    #print ("City: " + city + "\n")
    #for i in range(len(attractList)):
     #   print ("- "+attractList[i] + ". Rating: "+ratingList[i] + " (" +thingsRankList[i]+")\n")
    
    return (attractList, ratingList, thingsRankList)












