import oddslot_spider
import tipsbet_big_odds_spider

import venasbet_o25goals_spider
import venasbet_overgoals_spider
import venasbet_spider
import venasbet_u35goals_spider
import safe_bet
import featured_match_app
import kbtxtips
import vip_ticket_tips

import venabet_handicap
import venasbet_btts
import venasbet_dnb
import venasbet_wah
import bet99
import bet99_betday
import bet99_draws
import bet99_overgoals
import safebet_btts
import safebet_dc
import safebet_over_goals
# import betnum
import venasbet_over_35goals

# import twitter_api
# import twitter_results_api
import jackpot_spider
import kbt_telegram_bot
import time as _time


_runtime = 5

day_runtime = 86500

def _kbt():
        
        print('started for today ')
        _time.sleep(_runtime)
        jackpot_spider.run()
        _time.sleep(_runtime)
        vip_ticket_tips.run()
       
        oddslot_spider.run()
        _time.sleep(_runtime)
        safe_bet.run()
        _time.sleep(_runtime)
        featured_match_app.run()
        venasbet_spider.run()
        _time.sleep(_runtime)
        tipsbet_big_odds_spider.run()
        _time.sleep(_runtime)
        venasbet_overgoals_spider.run()
        _time.sleep(_runtime)
        venasbet_o25goals_spider.run()
        _time.sleep(_runtime)
        venasbet_u35goals_spider.run()
        _time.sleep(_runtime)
        kbtxtips.run()
        _time.sleep(_runtime)
        kbt_telegram_bot.run()

        _time.sleep(_runtime)
        venabet_handicap.run()
        _time.sleep(_runtime)
        venasbet_btts.run()
        _time.sleep(_runtime)
        venasbet_dnb.run()
        _time.sleep(_runtime)
        venasbet_over_35goals.run()
        _time.sleep(_runtime)
        venasbet_wah.run()
        _time.sleep(_runtime)
        bet99.run()
        bet99_betday.run()
        _time.sleep(_runtime)
        bet99_draws.run()
        _time.sleep(_runtime)
        bet99_overgoals.run()
       
        _time.sleep(_runtime)
        safebet_btts.run()
        _time.sleep(_runtime)
        safebet_over_goals.run()
        safebet_dc.run()
        
        print('ended for today ')
        _time.sleep(day_runtime)
        print('done')
  
 
def run():
    while True:
        _kbt()
        
        
if __name__ == "__main__":
    run()
