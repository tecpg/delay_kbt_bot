import csv
import numpy as np
import tweepy
import configparser

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

webUrl = 'https://kingsbettingtips.com/combo-betting-tips'

# print(api_key)

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# public_tweets = api.home_timeline()

# print(public_tweets[0].user.screen_name)


nigeria_woeid = "1398823"
kenya_woied = "1528335"
trend_results_nigeria = api.get_place_trends(nigeria_woeid)
trend_results_kenya = api.get_place_trends(kenya_woied)

kenya_trends = []
nigeria_trends = []

# _________________________________________________________
                # Fetching tips from csv
csv_f = "tipsbet_data.csv"
tips = []


with open(csv_f, "r") as f:    
        csv_data = csv.reader(f)
        for row in csv_data:
            tips.append(row[:8])


predictions =tips[:3]
contents = []
print(f"Predictions:   {predictions}")

tips_total_odd = [x[7] for x in predictions][0]
tips_date = [x[6] for x in predictions][0]
all_tips = tips_date = [x[:4] for x in predictions]
post_tips = ''
for x in all_tips:
    x[0] = f"({x[0]})"
    x[2] = f"({x[2]})"
    x[3] = f"({x[3]})-"
    post_tips += ' '.join(x)

print(post_tips)
contents = post_tips
# _________________________________________________________

def twiiter_bot(tips_content):
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

    ######################################################################
                    # Nigeria Trends
    ######################################################################

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

        # 👇️ using nested for loop

    ######################################################################
                    # END
    ######################################################################


        k_items = [item[0] for item in kenya_trends[:2]]
        n_items = [item[0] for item in nigeria_trends[:7]]
        n_items + k_items
        items = np.unique(n_items+k_items) # keeps only non dublicates
        post_trends = ' '.join(items)
        print(post_trends)

        tweet = f"Today Tips! \n {tips_content} \n - {webUrl} \n \n{post_trends}" 
        print(len(tweet))
        print(tweet)

        api.update_status(f"Betting Tips! \n {tips_content} \n visit-{webUrl}\n\n{post_trends}")


      
    # except:
    #     print("something went wrong")

   
twiiter_bot(contents)
