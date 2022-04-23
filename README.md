############ test-driven-oriented exercise ############

 write a model called Performance which has cost, revenue and creation date.
 add a new field for profit, which is the spread between revenue and costs
 extend this class with two other classes HourlyPerformance, DailyPerformance.
 HourlyPerformance has to have a datetime field called datetime
 DailyPerformance has to have a date field called date
 Please note, any migration hasn't been performed yet and the model Performance doesn't need to be in the db
 create a method called filter_by_min_roi(min_roi: float) so you can do DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
-- ROI in economics is return on investment and it's the result from the profit/costs, usually expressed in % --
 create a script called random_revenue.py.
 in this script filter the queryset using filter_by_min_roi previously created and save in a variable all the daily performance where the roi > 50%
 print the length of the queryset
 print the length of the queryset multiplied by 2

expected query set length ~= 50.000 records
 in a loop show the index of the loop out of the length of the queryset: 1/50000, 2/50000, 3/50000 and so on.
 in the same loop assign a new value to the revenue = revenue multiplied by a random factor which goes between 0.5 and 2 and save the daily_revenue with the new values

 create another script called slow_iteration.py
 in this script filter DailyPerformance where revenue > 2*cost or revenue > 1000, excluding records with cost=0 .
Limit the queryset to 50 records.
Iter over this queryset, and add a time.sleep(60) inside the loop. Implement this with celery task

How to run project
pip install -r requirements.txt
- ./manage.py makemigrations 
- ./manage.py migrate
- ./manage.py runscript random_revenue --dir-policy root
- ./manage.py runscript slow_iteration --dir-policy root