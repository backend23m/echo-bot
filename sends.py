from settings import URL
import requests


def send_message(chat_id: int, text, parse_mode=False):
    url = URL + '/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    requests.get(url, params=payload)


def send_voice(chat_id: int, voice: str):
    url = URL + '/sendVoice'
    payload = {
        "chat_id": chat_id,
        "voice": voice
    }

    requests.get(url, params=payload)

def send_location(chat_id: int, latitude: float, longitude: float):
    url = URL + '/sendLocation'
    payload = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude	
    }

    requests.get(url, params=payload)

