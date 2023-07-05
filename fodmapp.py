import requests

def api_call():
    url = "https://api.example.com/data"
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    params = {"param1": "value1", "param2": "value2"}

    response = requests.get(url, headers=headers, params=params)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.json()  # Extract the JSON data from the response
        print(data)
    else:
        # Request failed
        print("Error:", response.status_code)

def user_input():
    list_of_ingredients = input().split(", ")
    print(list_of_ingredients)
    return list_of_ingredients

def lookup():
    for i in user_input.list_of_ingredients:
        #make API call
        print(i)

user_input()
lookup()