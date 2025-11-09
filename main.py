import time
import logging

import oddslot_spider
import tipsbet_big_odds_spider
import venasbet_o25goals_spider
import venasbet_overgoals_spider
import venasbet_spider
import venasbet_u35goals_spider
import safe_bet
import fetch_tejtips
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
import venasbet_over_35goals
import kbt_telegram_bot

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

_RUNTIME = 5  # seconds between each run


def run_daily_tasks():
    logging.info("📅 Starting daily scraping and automation tasks...")

    try:
        time.sleep(_Runtime)
        vip_ticket_tips.run()
        time.sleep(_Runtime)

        safebet_over_goals.run()
        safebet_dc.run()
        time.sleep(_Runtime)

        tipsbet_big_odds_spider.run()
        time.sleep(_Runtime)

        venasbet_spider.run()
        time.sleep(_Runtime)

        safe_bet.run()
        fetch_tejtips.run()
        oddslot_spider.run()
        time.sleep(_Runtime)

        safebet_btts.run()
        venasbet_overgoals_spider.run()
        venasbet_o25goals_spider.run()
        time.sleep(_Runtime)

        kbtxtips.run()
        kbt_telegram_bot.run()
        time.sleep(_Runtime)

        venabet_handicap.run()
        venasbet_btts.run()
        venasbet_dnb.run()
        venasbet_over_35goals.run()
        venasbet_wah.run()
        time.sleep(_Runtime)

        bet99.run()
        bet99_betday.run()
        bet99_draws.run()
        bet99_overgoals.run()
        venasbet_u35goals_spider.run()

        logging.info("✅ All daily tasks completed successfully.")

    except Exception as e:
        logging.error(f"❌ Error during task execution: {e}")


if __name__ == "__main__":
    run_daily_tasks()
