from django.db import models
from patient.models import Patient
from account.models import User


class BarthelIndex(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    total = models.IntegerField()

    FOOD_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'Hilfe bei der Vorbereitung notwendig'),
        (10, 'komplett selbstständig')
    ]
    barthel_food = models.IntegerField(choices=FOOD_CHOICES)

    WASH_CHOICES = [
        (0, 'keine Selbstständigkeit gegeben'),
        (5, 'komplett selbstständig')
    ]
    barthel_wash = models.IntegerField(choices=WASH_CHOICES)

    SHOWER_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'Hilfe bei der Vorbereitung notwendig')
    ]
    barthel_shower = models.IntegerField(choices=SHOWER_CHOICES)

    DRESS_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'selbständig bei Oberkörper/ nutzt Utensilien'),
        (10, 'komplett selbstständig')
    ]
    barthel_dress = models.IntegerField(choices=DRESS_CHOICES)

    STOOL_CHOICES = [
        (0, 'kontinent oder komplett selbstständige Versorgung'),
        (5, 'überwiegend selbständige Versorgung'),
        (10, 'kontinent oder komplett selbstständige Versorgung')
    ]
    barthel_stool = models.IntegerField(choices=STOOL_CHOICES)

    URINE_CHOICES = [
        (0, 'kontinent oder komplett selbstständige Versorgung'),
        (5, 'überwiegend selbständige Versorgung'),
        (10, 'kontinent oder komplett selbstständige Versorgung')
    ]
    barthel_urin = models.IntegerField(choices=URINE_CHOICES)

    WC_USE_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'Hilfe bei der Vorbereitung notwendig'),
        (10, 'komplett selbstständig')
    ]
    barthel_wc = models.IntegerField(choices=WC_USE_CHOICES)

    TRANSFERS_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'erhebliche Hilfe oder Aufsicht nötig'),
        (10, 'geringe Hilfe oder Aufsicht nötig'),
        (15, 'komplett selbstständig')
    ]
    barthel_transf = models.IntegerField(choices=TRANSFERS_CHOICES)

    WALK_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'mit Laienhilfe/ Gehwagen oder bei Rollstuhlnutzung'),
        (10, 'mit Gehwagen möglich'),
        (15, 'Aufstehen + 50m ohne Hilfe')
    ]
    barthel_walk = models.IntegerField(choices=WALK_CHOICES)

    STAIRS_CHOICES = [
        (0, 'ohne Hilfe nicht durchführbar'),
        (5, 'Hilfe bei einem Stockwerk notwendig'),
        (10, 'komplett selbstständig 1 Stockwerk auf und ab')
    ]
    barthel_staris = models.IntegerField(choices=STAIRS_CHOICES)
