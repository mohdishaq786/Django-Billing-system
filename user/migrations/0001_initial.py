# Generated by Django 2.2.7 on 2019-12-30 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(default='', max_length=100)),
                ('Enrollmentno', models.CharField(default='0', max_length=100)),
                ('billno', models.CharField(default='', max_length=100)),
                ('cousre', models.CharField(default='', max_length=100)),
                ('branch', models.CharField(default='', max_length=100)),
                ('phoneno', models.CharField(default='', max_length=10)),
                ('feestatus', models.CharField(default='', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
