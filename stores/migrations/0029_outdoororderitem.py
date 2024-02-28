# Generated by Django 4.2.2 on 2024-02-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0028_outdoororder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutdoorOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(editable=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outdoor_order_items', to='stores.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.outdoororder')),
            ],
        ),
    ]
