# Generated by Django 4.2.3 on 2023-07-30 11:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_created_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contents',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Contenido del post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=110, verbose_name='Descripción'),
        ),
    ]