# Generated by Django 4.1.13 on 2024-05-03 09:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_rename_product_images_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="Descriptions",
        ),
        migrations.RemoveField(
            model_name="product",
            name="Product_Information",
        ),
        migrations.AddField(
            model_name="product",
            name="Description",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="Product_information",
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]