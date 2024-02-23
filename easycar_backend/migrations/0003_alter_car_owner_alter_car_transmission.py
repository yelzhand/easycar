# Generated by Django 4.2.7 on 2024-02-15 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easycar_backend', '0002_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(default='12', on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='automatic', max_length=10),
        ),
    ]
