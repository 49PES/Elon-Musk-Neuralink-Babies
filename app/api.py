import requests

def get_key():
    with open('./keys/key_nutrition.txt', 'r') as file:
        key = file.read()
        return key

def get_nutrition(query):
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': get_key()})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

# get_nutrition("cheerios")

def get_reccomendations(age, gender, pregnant, sex, tobacco):
    url = "https://health.gov/myhealthfinder/api/v3/myhealthfinder.json?" + f"age={age}&sex={gender}&pregnant={pregnant}&sexuallyActive={sex}&tobaccoUse={tobacco}"
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        x = response.json()
        description = x["Result"]['AboutTheseResults']
        advice = x["Result"]["Resources"]["all"]["Resource"][0]["Title"]
        advice_url = x["Result"]["Resources"]["all"]["Resource"][0]["AccessibleVersion"]
        related_arr = x["Result"]["Resources"]["all"]["Resource"][0]["RelatedItems"]["RelatedItem"]
        temp_titles = []
        x_1 = (advice, advice_url)
        temp_titles.append(x_1)
        for i in related_arr:
            y = (i['Title'],i["Url"])
            temp_titles.append(y)
        return description, temp_titles
    else:
        print("Error:", response.status_code, response.text)

#print(get_reccomendations(50,"female","no","no","no"))