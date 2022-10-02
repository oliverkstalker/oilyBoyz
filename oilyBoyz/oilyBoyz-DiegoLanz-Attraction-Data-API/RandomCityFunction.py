import requests
import random

def RandomCity():
    cityCode = random.randint(10000,999999) 
    while (True):
        url = "https://travel-advisor.p.rapidapi.com/attractions/list"

        querystring = {"location_id":str(cityCode),"currency":"USD","lang":"en_US","lunit":"km","sort":"recommended"}

        headers = {
            "X-RapidAPI-Key": "92b828dae2msh32f6193103ed4c6p1dcf00jsn0db7f7d743b4",
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
        }

        attractResponse = requests.request("GET", url, headers=headers, params=querystring)
        attract = attractResponse.json()
        if ('errors' in attract) or (attract['paging']['results'] == "0"):
                cityCode=random.randint(10000,999999)
        else:
            break
    ######################################################################################################

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
    
    return (attractList, ratingList, thingsRankList)

    


