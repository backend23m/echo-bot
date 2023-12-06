from settings import URL
import requests
from time import sleep
import sends


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint # https://api.telegram.org/bot{TOKEN}/getUpdates

    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']
        if len(result) == 0:
            return 404
        last_update = result[-1]
        return last_update

    return response.status_code


def main(url: str):
    last_update_id = -1

    while True:
        current_update = get_last_update(url)
        if current_update['update_id'] != last_update_id:
            user = current_update['message']['from']
            text = current_update['message'].get('text')
            voice = current_update['message'].get('voice')
            location = current_update['message'].get('location')

            if text is not None:
                sends.send_message(user['id'], text)

            elif voice is not None:
                sends.send_voice(user['id'], voice['file_id'])

            elif location is not None:
                print(location)
                sends.send_location(user['id'], location['latitude'], location['longitude'])

            else:
                sends.send_message(user['id'], 'coming soon ...')

            last_update_id = current_update['update_id']

        sleep(0.5)

main(URL)
