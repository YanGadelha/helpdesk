# Generated by Django 4.2.16 on 2024-11-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
