# Generated by Django 4.2 on 2023-04-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(db_column='message', max_length=5000),
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='mensagem',
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(db_column='name', max_length=65),
        ),
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='nome',
        ),
    ]
