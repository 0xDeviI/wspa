import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
print(f'Response of "{url}" is:\n{response.text}')