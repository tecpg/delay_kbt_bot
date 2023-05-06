import oddslot_spider
import tipsbet_big_odds_spider
import venasbet_o25goals_spider
import venasbet_overgoals_spider
import venasbet_spider
import venasbet_u35goals_spider
import previous_1x2tips
import kbtxtips
import twitter_api
import protips
import time as _time

_runtime = 10
day_runtime = 86500

def _kbt():
 
        print('started for today ')
        oddslot_spider.run()
        _time.sleep(_runtime)
        tipsbet_big_odds_spider.run()
        _time.sleep(_runtime)
        protips.run()
        _time.sleep(_runtime)
        twitter_api.run()
        _time.sleep(_runtime)
        venasbet_spider.run()
        _time.sleep(_runtime)
        venasbet_overgoals_spider.run()
        _time.sleep(_runtime)
        venasbet_u35goals_spider.run()
        _time.sleep(_runtime)
        venasbet_o25goals_spider.run()
        _time.sleep(_runtime)
        previous_1x2tips.run()
        _time.sleep(_runtime)
        kbtxtips.run()
       

        print('ended for today ')
        _time.sleep(day_runtime)
        print('done')
  
 

def run():
    while True:
        _kbt()

        
if __name__ == "__main__":
    run()
