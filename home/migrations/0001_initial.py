# Generated by Django 3.0.4 on 2020-03-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('reg', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
