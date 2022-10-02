from math import atan2
from ossaudiodev import AFMT_S16_BE
import requests
import random

def AttractionData(city):
    city=city.split(",")[0]

    ### API for City Code ############################################################
    url = "https://travel-advisor.p.rapidapi.com/locations/search"
    querystring = {"query":city,"limit":"30","offset":"0","units":"mi","location_id":"1","currency":"USD","sort":"relevance","lang":"en_US"}

    headers = {
        "X-RapidAPI-Key": "92b828dae2msh32f6193103ed4c6p1dcf00jsn0db7f7d743b4",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }
    codeResponse = requests.request("GET", url, headers=headers, params=querystring)
    code = codeResponse.json()
    cityCode = (code['data'][0]['result_object']['location_id'])

    ### API for Attraction Data #######################################################
    url = "https://travel-advisor.p.rapidapi.com/attractions/list"

    querystring = {"location_id":str(cityCode),"currency":"USD","lang":"en_US","lunit":"km","sort":"recommended"}

    headers = {
        "X-RapidAPI-Key": "92b828dae2msh32f6193103ed4c6p1dcf00jsn0db7f7d743b4",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    attractResponse = requests.request("GET", url, headers=headers, params=querystring)
    attract = attractResponse.json()
    #########################################################################

    attractList, ratingList, thingsRankList, descriptList, webList = [],[],[],[],[]

    #add attractions to attractions list
    for i in range(len(attract['data'])):
        if 'name' in attract['data'][i] and 'rating' in attract['data'][i] and 'ranking_subcategory' in attract['data'][i] and 'description' in attract['data'][i] and 'web_url' in attract['data'][i]:
            attraction = (attract['data'][i]['name'])
            rating = (attract['data'][i]['rating'])
            rank = (attract['data'][i]['ranking_subcategory'])
            descript = (attract['data'][i]['description'])
            web = (attract['data'][i]['web_url'])

            attractList.append(attraction)
            ratingList.append(rating)
            thingsRankList.append(rank)
            descriptList.append(descript)
            webList.append(web)
        if len(attractList) == 10:
            break

    at0 = attractList[0] + ". "+"("+thingsRankList[0]+") " + "\nWebsite: " + webList[0]  
    at1 = attractList[1] + ". "+"("+thingsRankList[1]+") " + "\nWebsite: " + webList[1]  
    at2 = attractList[2] + ". "+"("+thingsRankList[2]+") " + "\nWebsite: " + webList[2]  
    at3 = attractList[3] + ". "+"("+thingsRankList[3]+") " + "\nWebsite: " + webList[3]  
    at4 = attractList[4] + ". "+"("+thingsRankList[4]+") " + "\nWebsite: " + webList[4] 

    
    return (at0, at1, at2)
