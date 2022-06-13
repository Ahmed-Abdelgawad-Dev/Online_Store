# Generated by Django 4.0.4 on 2022-06-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='No name', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='No name', max_length=150),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='No name', max_length=150),
        ),
    ]