# Generated by Django 3.2.8 on 2021-10-29 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodis_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='meta_descriiption',
            new_name='meta_description',
        ),
    ]