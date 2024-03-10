# Define the main string
from kbt_funtions import get_result_by_score


main_string = "This is a sample string to search."

# Define the string to search for
search_string = "ri"

# Check if the search string is present in the main string
if search_string in main_string:
    print(f"The search string '{search_string}' was found.")
else:
    print(f"The search string '{search_string}' was not found.")


    

res = get_result_by_score('0bv,...', '0o/o--=jjkk7')
print(res)