# Generated by Django 4.0.6 on 2022-07-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasklist_detail_alter_tasklist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='detail',
            field=models.TextField(max_length=100),
        ),
    ]
