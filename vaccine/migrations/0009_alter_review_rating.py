# Generated by Django 5.0.6 on 2024-08-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0008_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=50),
        ),
    ]
