# Generated by Django 4.1.6 on 2023-02-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERNAME', models.CharField(blank=True, max_length=50, null=True)),
                ('EMAIL', models.CharField(blank=True, max_length=50, null=True)),
                ('PASSWORD', models.CharField(blank=True, max_length=50, null=True)),
                ('IMAGE', models.ImageField(upload_to='profile')),
                ('MOBILE', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
