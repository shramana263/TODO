# Generated by Django 5.0.3 on 2024-03-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='status',
            field=models.CharField(default='Incomplete', max_length=10),
        ),
    ]
