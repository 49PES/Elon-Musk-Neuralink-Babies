import requests

def get_key():
    with open('./keys/key_nutrition.txt', 'r') as file:
        key = file.read()
        return key

def get_nutrition(query):
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': get_key()})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

