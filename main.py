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

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
_RUNTIME = 5           # seconds between tasks
_START_DELAY_HOURS = 2 # initial delay in hours


def countdown(hours: int):
    """Countdown with minutes only, logging once per minute."""
    total_minutes = hours * 60
    logging.info(f"⏳ Delaying start for {total_minutes} minutes")
    while total_minutes > 0:
        hrs = total_minutes // 60
        mins = total_minutes % 60
        message = f"⏳ Starting in {hrs}h {mins}m"
        logging.info(message)
        print(message)
        time.sleep(60)
        total_minutes -= 1
    print()

import time
import logging

# def countdown_min(minutes: int):
#     """Countdown using minutes only, logging once per minute."""
#     logging.info(f"⏳ Delaying start for {minutes} minute(s)")
#     print(f"⏳ Delaying start for {minutes} minute(s)")

#     while minutes > 0:
#         message = f"⏳ Starting in {minutes} minute(s)"
#         logging.info(message)
#         print(message)

#         time.sleep(60)
#         minutes -= 1

#     logging.info("🚀 Delay complete. Starting tasks...")
#     print("🚀 Delay complete. Starting tasks...")


def run_task(task, index, total, monitor_duration=True):
    """Run a single task with logging, print, error handling, and optional duration monitoring."""
    message = f"▶ Running {task.__name__} ({index}/{total})..."
    logging.info(message)
    print(message)

    start_time = time.time()
    try:
        task.run()
    except Exception as e:
        error_message = f"❌ Error in {task.__name__}: {e}"
        logging.error(error_message)
        print(error_message)
    end_time = time.time()

    if monitor_duration:
        duration = end_time - start_time
        duration_msg = f"⏱ {task.__name__} completed in {duration:.2f} seconds."
        logging.info(duration_msg)
        print(duration_msg)

    time.sleep(_RUNTIME)


def run_daily_tasks():
    # Delay before starting tasks
    logging.info(f"⏳ Waiting for {_START_DELAY_HOURS} hours before starting tasks...")
    print(f"⏳ Waiting for {_START_DELAY_HOURS} hours before starting tasks...")
    countdown(_START_DELAY_HOURS)
    #countdown(1)

    # List of tasks
    tasks = [
        vip_ticket_tips,
        safebet_over_goals,
        safebet_dc,
        tipsbet_big_odds_spider,
        venasbet_spider,
        safe_bet,
        fetch_tejtips,
        oddslot_spider,
        safebet_btts,
        venasbet_overgoals_spider,
        venasbet_o25goals_spider,
        kbtxtips,
        kbt_telegram_bot,
        venabet_handicap,
        venasbet_btts,
        venasbet_dnb,
        venasbet_over_35goals,
        venasbet_wah,
        bet99,
        bet99_betday,
        bet99_draws,
        bet99_overgoals,
        venasbet_u35goals_spider,
    ]

    total_tasks = len(tasks)
    start_msg = f"📅 Starting daily scraping and automation tasks ({total_tasks} tasks)..."
    logging.info(start_msg)
    print(start_msg)

    for idx, task in enumerate(tasks, start=1):
        run_task(task, idx, total_tasks)

    success_msg = "✅ All daily tasks completed successfully."
    logging.info(success_msg)
    print(success_msg)


if __name__ == "__main__":
    run_daily_tasks()
