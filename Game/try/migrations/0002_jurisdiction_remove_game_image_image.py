# Generated by Django 5.0.6 on 2024-06-20 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jurisdiction', models.CharField(choices=[('MO', 'MACAU'), ('PH', 'PH-PAGCOR'), ('SE-ASIA', 'SE-asia'), ('US CA-TRIBAL', 'US CA-Tribal'), ('US FL-PARI', 'US FL-Pari'), ('US FL-SEMINOLE', 'US FL-Seminole'), ('US OKLA', 'US OKLA'), ('US OKLA-CHICKSAW', 'US OKLA-Chicksaw'), ('US MISSISSPPI', 'US Mississppi'), ('US MS CHOCTAW', 'US MS Choctaw'), ('PUERTO RICO', 'Puerto Rico'), ('US NORTH-DAKOTA', 'US North-Dakota'), ('US NEBRASKA', 'US Nebraska')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='game_images/')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='try.game')),
            ],
        ),
    ]