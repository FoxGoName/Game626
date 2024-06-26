# Generated by Django 5.0.6 on 2024-06-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0005_alter_game_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='jurisdiction',
            field=models.CharField(choices=[('MO', 'MACAU'), ('PH', 'PH-PAGCOR'), ('SE-ASIA', 'SE-asia'), ('US CA-TRIBAL', 'US CA-Tribal'), ('US FL-PARI', 'US FL-Pari'), ('US FL-SEMINOLE', 'US FL-Seminole'), ('US OKLA', 'US OKLA'), ('US OKLA-CHICKSAW', 'US OKLA-Chicksaw'), ('US OKLA-CHOCTAW', 'US OKLA-Choctaw'), ('US MISSISSPPI', 'US Mississppi'), ('US MS CHOCTAW', 'US MS Choctaw'), ('PUERTO RICO', 'Puerto Rico'), ('US NORTH-DAKOTA', 'US North-Dakota'), ('US NEBRASKA', 'US Nebraska')], max_length=100),
        ),
    ]
