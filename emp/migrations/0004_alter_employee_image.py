# Generated by Django 4.0.1 on 2022-01-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_employee_empp_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='emp/images/0804477b-6678-491a-ad12-e41a968b4cbe/'),
        ),
    ]