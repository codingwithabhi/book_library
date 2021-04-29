# Generated by Django 3.2 on 2021-04-29 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_collection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', unique=True),
        ),
    ]
