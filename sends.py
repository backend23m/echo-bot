from settings import TOKEN, URL
import requests


def send_message(chat_id: int, text, parse_mode=False):
    url = URL+'sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    if parse_mode:
        payload["parse_mode"] = "HTML"

    requests.get(url, params=payload)

def send_contact(chat_id, numer, fname, lname=None):
    url = URL+"sendContact"
    payload = {
        "chat_id": chat_id,
        "phone_number": numer,
        "first_name": fname,
    }
    if lname:
        payload['last_name'] = lname

    requests.post(url, params=payload)

def send_photo(chat_id, photo):
    url=URL+'sendPhoto'
    payload = {
        "chat_id": chat_id,
        "photo": photo,
    }
    requests.get(url, params=payload)

def send_location(chat_id: int, latitude, longitude):
    url=URL+"sendLocation"

    payload = {
        "chat_id" : chat_id,
        "latitude" : latitude,
        "longitude" : longitude
    }

    requests.get(url, params = payload)

def send_video(chat_id: str, video):
    url=URL+"sendVideo"

    payload = {
        "chat_id" : chat_id,
        "video" : video
    }

    requests.get(url, params=payload)

def send_document(chat_id: str, document ):
    url=URL+"sendDocument"

    payload = {
        "chat_id" : chat_id,
        "document" : document
    }

    requests.get(url, params=payload)

def send_voice(chat_id: int, voice):
    url=URL+"sendVoice"

    payload = {
        "chat_id" : chat_id,
        "voice" : voice
    }

    requests.get(url, params=payload)

def send_audio(chat_id: int, audio):
    url=URL+"sendAudio"

    payload = {
        "chat_id" : chat_id,
        "audio" : audio
    }

    requests.get(url, params=payload)

def send_video_note(chat_id: int, video_note):
    url=URL+"sendVideoNote"

    payload = {
        "chat_id" : chat_id,
        "video_note" : video_note
    }

    requests.get(url, params=payload)

def send_emoji(chat_id, emoji=None):
    url=URL+"sendDice"

    payload = {
        "chat_id" : chat_id,
        "emoji" : emoji
    }

    requests.get(url, params=payload)


