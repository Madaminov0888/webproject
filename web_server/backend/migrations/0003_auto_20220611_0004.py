# Generated by Django 3.2.8 on 2022-06-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_url', models.URLField(default='https://kun.uz', null=True, unique=True)),
                ('news_name', models.CharField(default='News name', max_length=25, null=True)),
                ('news_count_views', models.IntegerField(default=1, null=True)),
                ('news_text', models.TextField(default='0', null=True)),
                ('news_date', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Popular News',
                'verbose_name_plural': 'Popular News',
            },
        ),
        migrations.RenameModel(
            old_name='news',
            new_name='last_news',
        ),
        migrations.AlterModelOptions(
            name='last_news',
            options={'verbose_name': 'Last News', 'verbose_name_plural': 'Last News'},
        ),
    ]
