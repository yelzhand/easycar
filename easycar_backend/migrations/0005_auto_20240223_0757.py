# Generated by Django 3.2.23 on 2024-02-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easycar_backend', '0004_alter_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('gray', 'Gray'), ('silver', 'Silver'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple')], default='blue', max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='location',
            field=models.CharField(choices=[('Astana, Kazakhstan', 'Astana, Kazakhstan'), ('Almaty, Kazakhstan', 'Almaty, Kazakhstan'), ('Shymkent, Kazakhstan', 'Shymkent, Kazakhstan'), ('Karaganda, Kazakhstan', 'Karaganda, Kazakhstan'), ('Aktobe, Kazakhstan', 'Aktobe, Kazakhstan'), ('Taraz, Kazakhstan', 'Taraz, Kazakhstan'), ('Pavlodar, Kazakhstan', 'Pavlodar, Kazakhstan'), ('Ust-Kamenogorsk, Kazakhstan', 'Ust-Kamenogorsk, Kazakhstan'), ('Semey, Kazakhstan', 'Semey, Kazakhstan'), ('Atyrau, Kazakhstan', 'Atyrau, Kazakhstan'), ('Kostanay, Kazakhstan', 'Kostanay, Kazakhstan'), ('Kyzylorda, Kazakhstan', 'Kyzylorda, Kazakhstan'), ('Aktau, Kazakhstan', 'Aktau, Kazakhstan'), ('Kokshetau, Kazakhstan', 'Kokshetau, Kazakhstan'), ('Taldykorgan, Kazakhstan', 'Taldykorgan, Kazakhstan'), ('Ekibastuz, Kazakhstan', 'Ekibastuz, Kazakhstan'), ('Petropavl, Kazakhstan', 'Petropavl, Kazakhstan'), ('Oral, Kazakhstan', 'Oral, Kazakhstan'), ('Temirtau, Kazakhstan', 'Temirtau, Kazakhstan'), ('Turkestan, Kazakhstan', 'Turkestan, Kazakhstan')], default='Astana,Kazakhstan', max_length=100),
        ),
    ]
