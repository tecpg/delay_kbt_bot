import kbt_load_env
from datetime import datetime
from datetime import timedelta
from datetime import date
import base64
# all kbt CONSTANT variables indicated with capital snake case

#Wordpress constants
WP_LOCAL_URL = 'http://localhost:8080/wordpress/wp-json/wp/v2/posts/?post_type=predictions'
WP_LIVE_URL = 'https://kingsbettingtips.com/wp-json/wp/v2/posts'
WP_POST_TIME = datetime.now() + timedelta(minutes=5)
WP_POST_DATE = WP_POST_TIME.strftime("%Y-%m-%dT%H:%M:%S")
WP_LOCAL_USER = 'root'
WP_LIVE_USER = 'adminKBT'
WP_LOCAL_PASSWORD = kbt_load_env.local_pwd
WP_LIVE_PASSWORD = kbt_load_env.live_pwd
WP_CREDITIALS = WP_LIVE_USER + ':' + WP_LIVE_PASSWORD
WP_TOKEN = base64.b64encode(WP_CREDITIALS.encode())
WP_HEADER = {'Authorization': 'Basic ' + WP_TOKEN.decode('utf-8')}


WP_WELCOME_NOTE = """ Hello Kings!

We have just released a new set of football prediction tips for the upcoming matches. Our team of experts have analyzed the data and have come up with some highly accurate predictions.

Whether you are a casual fan or a serious bettor, these tips will help you make informed decisions about your bets. Be sure to check them out and let us know what you think.
<blockquote>
<small>As always, it is important to remember that these tips are not guaranteed and that there is always a risk of losing money when betting.</small> <strong>Please gamble responsibly.</strong></blockquote>

Thank you for your support and happy betting!<br> """

WP_JOIN_TELEGRAM_NOTE = """ We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
See you in the group!<br> 
<div class="media single-contact-info">
<a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
        </div>  
"""

WP_COMMENT_NOTE = """ <p>
We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
Your feedback is always valuable to us. Thank you!</p> """




#Time constants
MYSQL_DATE = date.today().strftime('%Y-%m-%d')

PRESENT_DAY_DATE = date.today()
YESTERDAY_DATE = PRESENT_DAY_DATE - timedelta(days = 1)
YESTERDAY_DMY = YESTERDAY_DATE.strftime('%d-%m-%Y')
PRESENT_DAY_DMY = date.today().strftime('%d-%m-%Y')
PRESENT_DAY_YMD = date.today().strftime('%Y-%m-%d')



#header constants
MY_HEARDER = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}




#cvs file names
JACKPOT_CSV = 'csv_files/jackpot_data.csv'
TELEGRAM_BOT_CSV = "csv_files/1x2bet-code.csv"
BLOG_POST_TIPS_CSV= "csv_files/1x2bet-code.csv"
ODDSLOT_CSV = "csv_files/oddslot_data.csv"
PROTIPS_CSV = "csv_files_protips.csv"
TIPSBET_CSV = "csv_files/tipsbet_data.csv"
VENASBET_2_5_CSV = "csv_files/venasbet_o_2_5_data.csv"
VENASBET_1_5_CSV = "csv_files/venasbet_over_1_5data.csv"
VENASBET_ACCA_CSV = "csv_files/venasbet_acca_data.csv"
VENASBET_3_5_CSV = "csv_files/venasbet_u_3_5_data.csv"
VIP_CSV = "csv_files/vip_tips_data.csv"





#telegram const
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6151016586:AAHnkIqKqBO01v1fQfd8noSOCzKLHjrWyGw'

# Replace 'CHANNEL_CHAT_ID' with the actual chat ID of your channel
CHANNEL_CHAT_ID = '-1001701327610'

# URL for the Telegram Bot API
# BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# URL for the Telegram Bot API
# URL for the Telegram Bot API
TELEGRAM_BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"