# Generated by Django 5.0.7 on 2024-07-19 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menan', '0002_abt_presonal_our_goal_our_mission_what_we_do'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('author', models.CharField(default='Admin', max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comments_count', models.IntegerField(default=0)),
            ],
        ),
    ]
