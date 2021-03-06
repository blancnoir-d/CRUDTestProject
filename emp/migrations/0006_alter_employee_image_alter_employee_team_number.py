# Generated by Django 4.0.1 on 2022-01-23 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrd', '0001_initial'),
        ('emp', '0005_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='emp/images/0db7c63c-5547-4796-833a-9df2f7eba99f/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrd.team'),
        ),
    ]
