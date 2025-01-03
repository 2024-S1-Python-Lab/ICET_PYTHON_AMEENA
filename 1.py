import datetime
current_yr=datetime.date.today().year
final_yr=int(input('Enter the final year:'))
if final_yr<current_yr:
    print('final year must be greater than or equal to current year')
else:
    print(f'Leap years from {current_yr} to {final_yr}')
    for year in range(current_yr,final_yr+1):
        if year%4==0 and (year%100!=0 or year%400==0):
           print(year)
