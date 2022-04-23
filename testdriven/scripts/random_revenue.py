import random

from testdriven.models import DailyPerformance


def run():
    queryset = DailyPerformance.objects.filter_by_min_roi()
    rev = []
    for roi in queryset:
        if roi.prod > float(50):
            rev.append(roi)
    print(len(queryset))
    print(len(rev)*2)

    for index in range(len(queryset)):
        print(index+1, '/', len(queryset))
        rand = random.uniform(0.5, 2)
        perform = DailyPerformance.objects.get(id=queryset[index].id)
        perform.revenue = rand
        perform.save()
