from datetime import datetime, timedelta
def date_difference():
    from_date = input("Enter the from date (yy-mm-dd): ")
    to_date = input("Enter the to date (yy-mm-dd): ")
    difference = int(input("Enter the difference in days: "))
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')
    date_diff = (to_date - from_date).days
    if date_diff < difference:
        return True
    else:
        return False
result = date_difference()
print(result)
