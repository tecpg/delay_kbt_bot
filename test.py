# Define the main string
import kbt_funtions


# main_string = "This is a sample string to search."

# # Define the string to search for
# search_string = "ri"

# # Check if the search string is present in the main string
# if search_string in main_string:
#     print(f"The search string '{search_string}' was found.")
# else:
#     print(f"The search string '{search_string}' was not found.")


    

res = kbt_funtions.get_result('1X', '0:3')
print(res)
res = kbt_funtions.get_result_by_score('1.5', '0:3')
print(res)