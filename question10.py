from datetime import datetime, timedelta
def find_previous_date():
    date = input("Enter a date (yy-mm-dd): ")
    n = int(input("Enter the number of days: "))
    date = datetime.strptime(date, '%y-%m-%d')
    previous_date = date - timedelta(days=n)
    previous_date_str = previous_date.strftime('%y-%m-%d')
    return previous_date_str
result = find_previous_date()
print(result)
