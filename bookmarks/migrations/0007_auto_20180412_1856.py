# Generated by Django 2.0.4 on 2018-04-12 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0006_auto_20180412_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='category',
            field=models.CharField(choices=[('FI', 'Film'), ('GA', 'Gaming'), ('MU', 'Music'), ('TE', 'Tech')], max_length=50, null=True, verbose_name='Category'),
        ),
    ]
