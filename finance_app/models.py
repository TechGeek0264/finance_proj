from django.db import models

# finance_app/models.py


class FinanceRate(models.Model):
    AGE_CHOICES = (
        (62, '62'),
        (63, '63'),
        (62, '62'),
        (63, '63'),
        (64, '64'),
        (65, '65'),
        (66, '66'),
        (67, '67'),
        (68, '68'),
        (69, '69'),
        (70, '70'),
        (71, '71'),
        (72, '72'),
        (73, '73'),
        (74, '74'),
        (75, '75'),
        (76, '76'),
        (77, '77'),
        (78, '78'),
        (79, '79'),
        (80, '80'),
        (81, '81'),
        (82, '82'),
        (83, '83'),
        (84, '84'),
        (85, '85'),
        (86, '86'),
        (87, '87'),
        (88, '88'),
        (89, '89'),
        (90, '90'),
        (91, '91'),
        (92, '92'),
        (93, '93'),
        (94, '94'),
        (95, '95'),
        (96, '96'),
        (97, '97'),
        (98, '98'),
        (99, '99'),
        # Add more age choices as needed
    )

    RATE_CHOICES = (
        ('3.0', '3.0%'),
        ('3.125', '3.125%'),
        ('3.25', '3.25%'),
        ('3.375', '3.375%'),
        ('3.5', '3.5%'),
        ('3.625', '3.625%'),
        ('3.75', '3.75%'),
        ('3.875', '3.875%'),
        ('4.0', '4.0%'),
        # Add more rate choices as needed
    )

    age = models.IntegerField(choices=AGE_CHOICES)
    rate_3_0 = models.FloatField()
    rate_3_125 = models.FloatField()
    rate_3_25 = models.FloatField()
    rate_3_375 = models.FloatField()
    rate_3_5 = models.FloatField()
    rate_3_625 = models.FloatField()
    rate_3_75 = models.FloatField()
    rate_3_875 = models.FloatField()
    rate_4_0 = models.FloatField()

    # Add other fields as needed

    def __str__(self):
        return f"FinanceRate {self.id} - Age: {self.age}"


class FinanceCalculation(models.Model):
    margin = models.FloatField()
    home_value = models.FloatField()
    age = models.IntegerField()
    initial_rate = models.FloatField()
    expected_rate = models.FloatField()
    cap_on_interest_rate = models.FloatField()
    initial_loc_growth = models.FloatField()
    principal_limit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calculation {self.id} at {self.created_at}"
