# Generated by Django 2.2.12 on 2020-04-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('result', models.TextField(blank=True, verbose_name='Результат проверки погоды')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created'],
            },
        ),
    ]
