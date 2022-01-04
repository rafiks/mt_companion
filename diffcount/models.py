from django.db import models

# Differential count
# This app will be a differential counter for hematalogy
#
# idea:
# multiple webforms for each parameter
# show also teh absolute count base off of the WBC count


class Diffct(models.Model):
    wbc = models.PositiveIntegerField()
    neut = models.PositiveIntegerField()
    lymp = models.PositiveIntegerField()
    mono = models.PositiveIntegerField()
    baso = models.PositiveIntegerField()
    eos = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    neut_a = models.PositiveIntegerField()
    lymp_a = models.PositiveIntegerField()
    mono_a = models.PositiveIntegerField()
    baso_a = models.PositiveIntegerField()
    eos_a = models.PositiveIntegerField()
