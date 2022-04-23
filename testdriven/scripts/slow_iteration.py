from celery.utils.log import get_task_logger
from django.db.models import F, Q
from testdriven.tasks.sleep_tasks import create_task
from testdriven.models import DailyPerformance

logger = get_task_logger(__name__)


def run():
    queryset = DailyPerformance.objects.filter(Q(revenue__gte=F('cost') * 2) | Q(revenue__gte='1000')).exclude(
        cost__in='0')[:50]
    for _ in queryset:
        task = create_task.delay(60)
        print(task)
