# Generated by Django 4.2.2 on 2024-02-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0031_outdoorcart_anonymous_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous_user_id', models.CharField(blank=True, max_length=80, null=True, unique=True)),
            ],
            options={
                'db_table': 'temp_users',
            },
        ),
    ]
