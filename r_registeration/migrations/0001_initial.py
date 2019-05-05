# Generated by Django 2.1.8 on 2019-05-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.IntegerField(choices=[(0, '종로구'), (1, '용산구'), (2, '동대문구')], null=True)),
                ('address2', models.IntegerField()),
                ('address3', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField(verbose_name='date published')),
                ('bill', models.IntegerField()),
                ('pet', models.BooleanField()),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]