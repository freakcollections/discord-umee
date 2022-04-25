import requests
import json
import time
from datetime import datetime
from colorama import Fore


def sendMessage(token, channel_id, message):
    data = {"content": message}
    header = {"authorization": token}
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    response = requests.post(url, data=data, headers=header)
    current_time = datetime.now().time()
    if response.status_code == 200:
        print(f'{Fore.RESET}{current_time} | {Fore.GREEN}SUCCESS\n{Fore.RESET}{message}token: {token}\n')
        status = 1
    else:
        print(f'{Fore.RESET}{current_time} | {Fore.RED}ERROR\n{Fore.RESET}{message}token: {token}\n')
        status = 0
    return status


if __name__ == '__main__':
    print(f'{Fore.BLUE}Made by @freakcollections\n')
    time.sleep(3)
    channel_id = 959524634963869746
    all_statuses = 0
    
    with open('tokens.txt', 'r') as read_file:
        tokens = read_file.readlines()
        tokens = [line.rstrip('\n') for line in tokens]
    
    with open('messages.json', 'r') as json_file:
        wallets = json.load(json_file)

    for token in tokens:
        message = ''
        for network in wallets[token]['wallets']:
            message += f'!request {list(network.values())[0]}\n'
        cur_status = sendMessage(token, channel_id, message)
        all_statuses += cur_status
    
    print(f'{Fore.GREEN}SUCCESS: {all_statuses}{Fore.RESET} | {Fore.RED}ERROR: {len(tokens) - all_statuses}')