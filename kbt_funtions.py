import random
import string
import kbt_load_env
import mysql.connector
from mysql.connector import errorcode

def db_connection():
     #open db connection
    return mysql.connector.connect(host=kbt_load_env.db_host,
                                        database=kbt_load_env.db_dbname,
                                        user=kbt_load_env.db_user,
                                        password=kbt_load_env.db_pwd)
#local mysql connection
        # connection = mysql.connector.connect(host='localhost',
        #                                  database='kingsbet_KBTdb',
        #                                  user='root',
        #                                  password='')
  

def get_code(length):
    letters = string.ascii_lowercase
    r_letters = ''.join(random.choice(letters) for i in range(length))
    numbers =   str(random.randint(2220,333000333))
    code = r_letters+numbers
    return code

# Python code to remove whitespace
def remove(string):
    return string.replace("\n", "")

def get_result(pick, score):
    try:
        if ':' in score:
            # Score contains ':', indicating it's in the format 'score1:score2'
            s_list = list(map(int, score.split(":")))  # Convert scores to integers for comparison
            if pick == "1X":
                result = "Won" if s_list[0] >= s_list[1] else "Lost"
            elif pick == "2X":
                result = "Won" if s_list[0] <= s_list[1] else "Lost"
            elif pick == "X2":
                result = "Won" if s_list[0] <= s_list[1] else "Lost"
            elif pick == "1":
                result = "Won" if s_list[0] > s_list[1] else "Lost"
            elif pick == "2":
                result = "Won" if s_list[0] < s_list[1] else "Lost"
            elif pick == "12":
                result = "Won" if s_list[0] != s_list[1] else "Lost"
            else:
                result = "..."
        else:
            # Score doesn't contain ':', indicating it's not in the expected format
            result = "..."
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        result = "..."  # Default result if an exception occurs

    return result



def get_result_by_score(pick, score):
     
     try:
        if any(map(str.isdigit, score)):
            s_list = list(map(int, score.split(":")))
            s_n = sum(s_list)  # Sum of scores

            if '2.5' in pick:
                return "Won" if s_n > 2 else "Lost"
            elif '1.5' in pick:
                return "Won" if s_n >= 2 else "Lost"
            elif '3.5' in pick:
                return "Won" if s_n <= 3 else "Lost"
            elif "2DNB" in pick:
                return "Won" if s_list[0] < s_list[1] or s_list[0] == s_list[1] else "Lost"
            elif "1DNB" in pick:
                return "Won" if s_list[0] > s_list[1] or s_list[0] == s_list[1] else "Lost"
            else:
                return "..1."
        else:
            return ".2.."
     except Exception as e:
        print(e)
        return "..3."


def check_odd_range(value):
    return 1.50 <= value <= 4.0

