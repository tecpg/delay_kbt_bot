import csv
import requests
import configparser
from PIL import Image, ImageFont, ImageDraw
from consts import global_consts as gc


def post():
    tips = []

    with open(gc.TELEGRAM_BOT_CSV, "r") as f:    
            csv_data = csv.reader(f)
            for row in csv_data:
                tips.append(row[:8])
    predictions =tips[:6]
    contents = []
    print(f"Predictions:   {predictions}")

    tips_date = [x[3] for x in predictions][0]
    all_tips = tips_date = [x[:3] for x in predictions]
    post_tips = ''
    for x in all_tips:
        x[0] = f"{x[0]}\n"
        x[1] = f"{x[1]} =>"
        x[2] = f"{x[2]}\n\n"
        post_tips += ' '.join(x)

    print(post_tips)


    thumbnail = Image.open("assets/images/bg_img.png")
    t_font = ImageFont.truetype('assets/fonts/b.ttf', 20)
    t_text = post_tips
    image_editable = ImageDraw.Draw(thumbnail)
    image_editable.text((50,400), t_text,(00, 00, 00), t_font)
    thumbnail.save("thumbnail.jpg")


    # Text and link you want to post
    message_text = "Winning KBT free telegram tips for today! Do not miss the cash!"
    link_url = "https://kingsbettingtips.com \n\n"
    link_url2 = " SUBSCRIBE NOW FOR PREMIUM TIPS --->>> https://kingsbettingtips.com/vip-subscriptions/"

    # Path to the photo file on your local filesystem
    photo_path = 'assets/images/thumbnail.jpg'

    # Construct the payload
    payload = {
        "chat_id": gc.CHANNEL_CHAT_ID,
        "text": f"{message_text} {link_url}"
    }
    # Send the POST request with the photo file
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(gc.TELEGRAM_BASE_URL + 'sendPhoto', data=payload, files=files)


    # Check the response status
    if response.status_code == 200:
        print("Message posted successfully!")
    else:
        print("Failed to post message:", response.text)



    # Construct the payload for sending the message
    payload = {
        "chat_id": gc.CHANNEL_CHAT_ID,
        "text": f"{message_text} {link_url} {link_url2}"
    }

    # Send the POST request for sending the message
    message_response = requests.post(gc.TELEGRAM_BASE_URL + 'sendMessage', data=payload)

    # Check the response status for sending the message
    if message_response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", message_response.text)


def run():
    post()

if __name__ == "__main__":
    run()



