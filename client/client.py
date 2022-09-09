import sys
import requests

# get url of remote-server
url = input('Enter remote-server url address -->').strip()

# get password of remove-server
password = input('Enter remote-server password -->')

while True:
    # get command
    command = input('Enter your command -->')
    if command == 'exit':
        sys.exit(0)
    try:
        # send command and get result from server
        result = requests.get(f'{url}/{password}/{command}')
        print(result.text)
    except:
        print('Invalid command or password')