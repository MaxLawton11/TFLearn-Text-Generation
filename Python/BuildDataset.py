import requests

print('--------- Building Dataset ---------')

url = 'https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt'
response = requests.get(url)

sets_path = 'DataSets'
output_file_name = 'shakespeare_input.txt'

print(f'# Creating file: {output_file_name}')

with open(f'{sets_path}/{output_file_name}', 'w') as file:
    file.write(response.text)

print('--------- Success ---------')