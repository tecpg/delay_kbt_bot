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
                if any(map(str.isdigit, score)):
                        s_list = list(score.split(":"))
                
                        if pick == "1X":
                                if s_list[0] > s_list[1] or s_list[0] == s_list[1] :
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif pick == "2X":
                                if s_list[0] < s_list[1] or s_list[0] == s_list[1] :
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif pick == "X2":
                                if s_list[0] < s_list[1] or s_list[0] == s_list[1] :
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif pick == "1":
                                if s_list[0] > s_list[1]:
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif pick == "2":
                                if s_list[0] < s_list[1]:
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif pick == "12":
                                if s_list[0] > s_list[1] or s_list[0] < s_list[1] :
                                        result = "Won"
                                else:
                                        result = "Lost"
                        elif score == ":":
                                result = "..."
                        else:
                                result = "..."

                                return result
                else:
                        result = "..."
                        return result
        except Exception as e:
               results = "..."
               return results



def get_result_by_score(pick, score):
    
        try:
      
                if any(map(str.isdigit, score)):
        
                        s_list = list(score.split(":"))
                        s_n = [eval(i)for i in s_list]

                        #calculate over 2.5 score
                        if '2.5' in pick:
                                if s_n > 2:
                                        results = "Won"
                                else:
                                        results = "Lost"
                                return results
                        
                        elif '1.5' in pick:
                                if s_n >= 2:
                                        results = "Won"
                                else:
                                        results = "Lost"
                                return results
                        
                        elif '3.5' in pick: 
                                if s_n <= 3:
                                        results = "Won"
                                else:
                                        results = "Lost"
                                return results
                        
                        elif "2DNB" in pick:
                        
                                if s_list[0] < s_list[1] or s_list[0] == s_list[1] :
                                        results = "Won"
                                else:
                                        results = "Lost"

                        elif "1DNB" in pick:
                                if s_list[0] > s_list[1] or s_list[0] == s_list[1] :
                                        results = "Won"
                                else:
                                        results = "Lost"

                        else:
                                results = "..."
                        
                        return results
                
                
                
                else:
                        results = "..."
                        return results
                
        except Exception as e:
               results = "..."
               return results


def check_odd_range(value):
    return 1.50 <= value <= 4.0

