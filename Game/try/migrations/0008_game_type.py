# Generated by Django 5.0.6 on 2024-06-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0007_alter_jurisdiction_jurisdiction'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='type',
            field=models.CharField(choices=[('ETG', 'ETG'), ('SLOT', 'Slot')], default='SLOT', max_length=100),
        ),
    ]
