# Generated by Django 4.2.3 on 2023-08-26 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0002_remove_patient_chronic_conditions_and_more'),
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
