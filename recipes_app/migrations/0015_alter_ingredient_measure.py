# Generated by Django 5.0.6 on 2024-07-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0014_alter_ingredient_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measure',
            field=models.CharField(choices=[('шт.', 'шт.'), ('гр.', 'гр.'), ('ст.л.', 'ст.л.'), ('чай.л.', 'чай.л.'), ('мл.', 'мл.')], default='гр.', max_length=6),
        ),
    ]
