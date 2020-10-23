# Generated by Django 3.1.2 on 2020-10-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('friends', models.ManyToManyField(null=True, related_name='_person_friends_+', to='users.Person')),
            ],
        ),
    ]
