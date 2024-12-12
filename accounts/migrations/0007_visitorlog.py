# Generated by Django 5.1.2 on 2024-12-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_gender_alter_profile_middle_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('HR', 'HR'), ('IT', 'IT'), ('Admin', 'Admin'), ('Finance', 'Finance')], max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('to_whom', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]