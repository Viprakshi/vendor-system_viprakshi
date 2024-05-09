# Generated by Django 4.2.6 on 2024-05-09 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Vendor Name')),
                ('contact_details', models.TextField(verbose_name='Contact Details')),
                ('address', models.TextField(verbose_name='Address')),
                ('vendor_code', models.CharField(max_length=50, unique=True, verbose_name='Vendor Code')),
                ('on_time_delivery_rate', models.FloatField(default=0, verbose_name='On-Time Delivery Rate')),
                ('quality_rating_avg', models.FloatField(default=0, verbose_name='Quality Rating Average')),
                ('average_response_time', models.FloatField(default=0, verbose_name='Average Response Time')),
                ('fulfillment_rate', models.FloatField(default=0, verbose_name='Fulfillment Rate')),
            ],
            options={
                'db_table': 'vendor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50, unique=True, verbose_name='PO Number')),
                ('order_date', models.DateTimeField(verbose_name='Order Date')),
                ('delivery_date', models.DateTimeField(verbose_name='Delivery Date')),
                ('items', models.JSONField(verbose_name='Items')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('quality_rating', models.FloatField(blank=True, default=0, verbose_name='Quality Rating')),
                ('issue_date', models.DateTimeField(verbose_name='Issue Date')),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True, verbose_name='Acknowledgment Date')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor', verbose_name='Vendor')),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('on_time_delivery_rate', models.FloatField(default=0, verbose_name='On-Time Delivery Rate')),
                ('quality_rating_avg', models.FloatField(default=0, verbose_name='Quality Rating Average')),
                ('average_response_time', models.FloatField(default=0, verbose_name='Average Response Time')),
                ('fulfillment_rate', models.FloatField(default=0, verbose_name='Fulfillment Rate')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor', verbose_name='Vendor')),
            ],
            options={
                'db_table': 'performance',
                'managed': True,
            },
        ),
    ]
