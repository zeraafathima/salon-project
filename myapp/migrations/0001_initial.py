# Generated by Django 5.1.3 on 2024-11-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('service_type', models.CharField(choices=[('consultation', 'Consultation'), ('follow_up', 'Follow-Up Appointment'), ('therapy', 'Therapy Session'), ('other', 'Other')], max_length=50)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.CharField(choices=[('09:00', '9:00 AM'), ('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '1:00 PM'), ('14:00', '2:00 PM'), ('15:00', '3:00 PM'), ('16:00', '4:00 PM')], max_length=5)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_designers', models.ImageField(upload_to='designers')),
                ('d_name', models.CharField(max_length=100)),
                ('d_spec', models.TextField()),
                ('d_desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='stylists/')),
            ],
        ),
    ]
