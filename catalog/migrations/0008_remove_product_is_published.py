# Generated by Django 4.2.2 on 2024-06-20 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_product_creator_product_is_published"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="is_published",
        ),
    ]
