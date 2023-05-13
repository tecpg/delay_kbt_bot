import csv
import numpy as np
import tweepy
import configparser
from PIL import Image, ImageFont, ImageDraw
import kdb_config

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = kdb_config.api_key
api_key_secret = kdb_config.api_key_secret

access_token = kdb_config.access_token
access_token_secret = kdb_config.access_token_secret

webUrl = 'https://kingsbettingtips.com'

# print(api_key)

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


nigeria_woeid = "1398823"
kenya_woied = "1528335"
trend_results_nigeria = api.get_place_trends(nigeria_woeid)
trend_results_kenya = api.get_place_trends(kenya_woied)

kenya_trends = []
nigeria_trends = []

lost_post = False

# _________________________________________________________
                # Fetching tips from csv
def get_tweet_contents():
    csv_f = "oddslot_data.csv"
    tips = []


    with open(csv_f, "r") as f:    
            csv_data = csv.reader(f)
            rows = list(csv_data)
            reversed_rows = reversed(rows)  # Reverse the list of rows

            for row in reversed_rows:
                tips.append(row)


    predictions =tips[:6] #get from 0 - 6 rows 
    contents = []
  

    all_tips =  [x[:10] for x in predictions]
    indices = [0, 1, 2, 5, 8] #index to be selected
    selected_elements = []

    for sublist in all_tips:
      selected_elements.append([sublist[i] for i in indices])


    print(f"Selected  {selected_elements}")

   
    post_tips = ''
    lost_count = 0
    global lost_post

    

    for x in selected_elements:
        
        if x[4] == 'Lost':
             lost_count += 1

        if lost_count > 1:
             lost_post = True
        else:
             lost_post = False
        
        if x[4] not in ['Won', 'Lost']: 
             
             continue
   
        x[0] = f"{x[0]}\n"
        x[1] = f"{x[1]} =>"
        x[2] = f"{x[2]}"
        x[3] = f"({x[3]})"
        x[4] = f"==>{x[4]}\n\n"
        post_tips += ' '.join(x)

    print(post_tips)
    contents = post_tips
   
    return contents


     

def twiiter_bot(tips_content):
        
        #  #######################################################
                        # Create image
        ##########################################################


        thumbnail = Image.open("bg_img_results.png")
        t_font = ImageFont.truetype('b.ttf', 18)
        t_text = get_tweet_contents()
        image_editable = ImageDraw.Draw(thumbnail)
        image_editable.text((20,400), t_text,(00, 00, 00), t_font)
        thumbnail.save("thumbnail.jpg")



        # _________________________________________________________
    # try:
    ######################################################################
                    # Kenya Trends
    ######################################################################

        for trend in trend_results_kenya[0]["trends"][:50]:
            name = trend["name"]
            volume = trend["tweet_volume"]
            promoted = trend["promoted_content"]

            k_trends = [name, volume, promoted]
            if k_trends[1] is not None:
                kenya_trends.append(tuple(k_trends))
        # print(kbt_trends)

        kenya_trends.sort(key=lambda a: a[1], reverse = True)

    # # # ######################################################################
    # # #                 # Nigeria Trends
    # # # ######################################################################

        for trend in trend_results_nigeria[0]["trends"][:50]:
            name = trend["name"]
            volume = trend["tweet_volume"]
            promoted = trend["promoted_content"]

            n_trends = [name, volume, promoted]
            if n_trends[1] is not None:
                nigeria_trends.append(tuple(n_trends))
            # print(kbt_trends)

            nigeria_trends.sort(key=lambda a: a[1], reverse = True)
            # print(kbt_trends)

    # # #     # 👇️ using nested for loop

    # # # ######################################################################
    # # #                 # END
    # # # ######################################################################


        k_items = [item[0] for item in kenya_trends[:5]]
        n_items = [item[0] for item in nigeria_trends[:10]]
        n_items + k_items
        items = np.unique(n_items+k_items) # keeps only non dublicates
        post_trends = ' '.join(items)
        print(post_trends)

        tweet = f"Today Tips! \n {tips_content} \n - {webUrl} \n \n{post_trends}" 
        print(len(tweet))
        print(tweet)

        api.update_status_with_media(f"Results from our previous prediction tips \n for more tip visit ---{webUrl}\n\n{post_trends}","thumbnail.jpg")


      
    # except:
    #     print("something went wrong")





def run():
    if lost_post == False:
        twiiter_bot(get_tweet_contents)
        print(lost_post)
    else:
        pass
 

if __name__ == "__main__":
    run()
