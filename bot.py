from settings import TOKEN
import requests
from time import sleep
from pprint import pprint
import sends


def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result']
    else:
        return False


def get_last_update(updates: list[dict]) -> dict:
    return updates[-1]

# pprint(get_updates())

last_update_id = -1
while True:
    updates = get_updates()
    # print(updates)
    last_update = get_last_update(updates)
    if last_update['update_id'] != last_update_id:
            user = last_update['message']['from']
            if "photo" in last_update['message'].keys():
                photo=last_update['message']["photo"][0]["file_id"]

                sends.send_photo(user["id"], photo)
            
            elif "text" in last_update['message'].keys():

                text = last_update['message']['text']
                sends.send_message(user["id"], text)

            elif "contact" in last_update['message'].keys():
                 chat_id=user["id"]
                 number=last_update['message']["contact"]["phone_number"]
                 first_name=last_update['message']["contact"]["first_name"]
                 if "last_name" in last_update["message"]['contact'].keys():
                    last_name=last_update['message']["contact"]["last_name"]
                    sends.send_contact(chat_id, number, first_name, last_name)
                 else:
                     sends.send_contact(chat_id, number, first_name)
                

            elif "location" in last_update["message"].keys():

                latitude=last_update["message"]["location"]["latitude"]                
                longitude=last_update["message"]["location"]["longitude"]   
                sends.send_location(user["id"], latitude, longitude)   

            elif "video" in last_update["message"].keys():

                video=last_update["message"]["video"]["file_id"]

                sends.send_video(user["id"], video)
            elif "document" in last_update["message"].keys():

                document=last_update["message"]["document"]["file_id"]

                sends.send_video(user["id"], document)

            elif "voice" in last_update["message"].keys():

                voice=last_update["message"]["voice"]["file_id"]

                sends.send_video(user["id"], voice)
            
            elif "audio" in last_update["message"].keys():

                audio=last_update["message"]["audio"]["file_id"]

                sends.send_video(user["id"], audio)

            elif "video_note" in last_update["message"].keys():

                video_note=last_update["message"]["video_note"]["file_id"]

                sends.send_video_note(user["id"], video_note)

            elif "emoji" in last_update["message"].keys():

                emoji=last_update["message"]["dice"]["emoji"]

                sends.send_video_note(user["id"], emoji)

            last_update_id = last_update['update_id']
    sleep(0.5)




    