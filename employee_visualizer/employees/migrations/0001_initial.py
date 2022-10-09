# Generated by Django 4.1.2 on 2022-10-09 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('passport', models.TextField()),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('gender', models.TextField(choices=[('0', 'Male'), ('1', 'Female')])),
                ('birthday', models.DateField()),
                ('natinality', models.TextField()),
                ('hired', models.DateField()),
                ('dept', models.TextField()),
                ('position', models.TextField()),
                ('status', models.TextField(choices=[('1', 'Active'), ('2', 'Resigned'), ('3', 'Retired')])),
                ('region', models.TextField()),
            ],
        ),
    ]