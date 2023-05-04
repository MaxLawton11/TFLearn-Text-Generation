import requests

url = "https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt"
response = requests.get(url)

sets_path = "DataSets"

with open(f"{sets_path}/shakespeare_input.txt", "w") as file:
    file.write(response.text)
