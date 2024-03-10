import requests
from cmath import cos
import requests
import consts.global_consts as gc

#posting into wp
def featured_match_wp_post(**post_dict):
   
    tip_category = post_dict["tips_category"]
    tip_note = post_dict["category_note"]
    telegram_content = post_dict["telegram_content"]
    content = post_dict["post_content"]
    post_title = post_dict["post_title"]
    

    post = {
    'title'    : f'{post_title}',
    'status'   : 'publish', 
    'content'  : f'{content}'
                                        f'{tip_note}'
                                        f'{telegram_content}'
                                        f'{gc.WP_COMMENT_NOTE}',
                                     'date'   : f'{gc.WP_POST_DATE}',
                                    'categories' : ['4', '185', f'{tip_category}'],
                                    'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
    }

    r = requests.post(gc.WP_LIVE_URL, headers=gc.WP_HEADER, json=post)
    print(r)