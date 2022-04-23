from django.db import models
from decimal import Decimal
from django.db.models import FloatField, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Cast


class Performance(models.Model):
    cost = models.DecimalField(max_digits=12, decimal_places=2, )
    revenue = models.DecimalField(max_digits=12, decimal_places=2, )
    profit = models.DecimalField(max_digits=12, decimal_places=2, default=None, blank=True)
    creation_date = models.DateField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.profit = Decimal(self.revenue) - Decimal(self.cost)
        super(Performance, self).save(*args, **kwargs)


class HourlyPerformance(Performance):
    datetime = models.DateTimeField()


class FilterManager(models.QuerySet):
    def filter_by_min_roi(self, min_roi=None):
        if min_roi is not None:
            return self.all().annotate(prod=ExpressionWrapper(F('profit') * Decimal('1.0') / F('cost') * 100,
                                              output_field=FloatField())).filter(prod=Decimal(min_roi) * 100)
        return self.all().annotate(prod=ExpressionWrapper(F('profit') * Decimal('1.0')/F('cost') * 100,
                                                            output_field=FloatField()))


class DailyPerformance(Performance):
    date = models.DateField()

    objects = FilterManager.as_manager()


