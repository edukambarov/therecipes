# Generated by Django 5.0.6 on 2024-07-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0012_alter_recipe_categories_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='measure',
            field=models.CharField(choices=[('U', 'шт.'), ('G', 'гр.'), ('B', 'ст.л.'), ('S', 'чай.л.'), ('M', 'мл.')], default='G', max_length=1),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
