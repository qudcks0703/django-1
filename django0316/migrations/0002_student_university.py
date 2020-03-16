# Generated by Django 3.0.4 on 2020-03-16 04:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django0316', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_birth', models.DateField()),
                ('residencce', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('intro', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django0316.University')),
            ],
        ),
    ]
