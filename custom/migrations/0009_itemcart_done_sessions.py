# Generated by Django 3.0.7 on 2020-10-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0008_remove_itemcart_workcommpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcart',
            name='done_sessions',
            field=models.CharField(blank=True, db_column='Done_Sessions', max_length=700, null=True),
        ),
    ]
