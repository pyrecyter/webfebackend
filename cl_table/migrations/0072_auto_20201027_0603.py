# Generated by Django 3.0.7 on 2020-10-27 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0008_auto_20201013_0749'),
        ('cl_table', '0071_auto_20201026_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositaccount',
            name='Cust_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer'),
        ),
        migrations.AddField(
            model_name='depositaccount',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
        migrations.AddField(
            model_name='depositaccount',
            name='site_code',
            field=models.CharField(db_column='Site_Code', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prepaidaccount',
            name='Cust_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer'),
        ),
        migrations.AddField(
            model_name='prepaidaccount',
            name='Site_Codeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist'),
        ),
    ]
