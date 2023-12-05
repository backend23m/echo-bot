from settings import URL
import requests
from time import sleep

def echobot_update(url: str):
    endpoint = "/getUpdates"
    url += endpoint
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]
        else:
            return 404
    else:
        return response.status_code

def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    requests.get(url, params=payload)



def send_voice(url: str, chat_id: int, voice_file_id: str, duration: int):
    endpoint = '/sendVoice'
    url += endpoint

    params = {
        'chat_id': chat_id,
        'voice': voice_file_id,
    }
    requests.get(url, params=params)

def send_photo(url: str, chat_id: int, photo: str):
    endpoint = '/sendPhoto'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'photo': photo,
    }
    requests.get(url, params=payload)

def send_video(url: str, chat_id: int, video_file_id: str, duration: int):
    endpoint = '/sendVideo'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'video': video_file_id,
    }
    requests.get(url, params=payload)

def send_animation(url: str, chat_id: int, animation_file_id, duration: int):
    endpoint = '/sendAnimation'
    url+=endpoint

    payload = {
        'chat_id': chat_id,
        'animation': animation_file_id,
    }
    requests.get(url, params=payload)

def send_document(url: str, chat_id: int, file: str):
    endpoint = '/sendDocument'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'document': document,
    }
    requests.get(url, params=payload)

def send_contact(url: str, chat_id: int, phone_number: str, first_name: str): 
    endpoint = '/sendContact'
    payload = {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
    }
    requests.get(url, params=payload)

def send_location(url: str, chat_id: int, latitude: float, longitude: float):
    endpoint = '/sendLocation'
    payload = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
    }
    requests.get(url, params=payload)
    
    
def main(url: str):
    last_update_id = -1

    while True:
        update = echobot_update(url)

        if update['update_id'] != last_update_id:
            user = update['message']['from']
            text = update['message'].get("text")
            photo = update['message'].get("photo")
            voice = update['message'].get("voice")
            video = update['message'].get("video")
            animation=update['message'].get("animation")
            document=update['message'].get("document")
            contact=update['message'].get("contact")
            location=update['message'].get("location")

            if text:
                send_message(url, user['id'], text)
            elif photo:
                send_photo(url, user['id'], photo[-1]['file_id'])
            elif voice:
                send_voice(url, user['id'], voice['file_id'], voice['duration'])
            elif video:
                send_video(url, user['id'], video['file_id'], video['duration'])
            elif animation:
                send_animation(url, user['id'], animation['file_id'], animation['duration'])
            elif photo:
                send_document(url, user['id'], document[-1]['file_id'])
            elif contact:
                send_contact(url, user['id'],contact['phone_number'], contact['first_name'])
            elif location:
                send_location(url, user['id'], location['latitude'], location['longitude'])
                
            last_update_id = update['update_id']

        sleep(0.5)

if __name__ == "__main__":
    main(URL)
