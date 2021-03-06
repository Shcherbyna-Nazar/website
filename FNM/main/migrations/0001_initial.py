# Generated by Django 4.0.2 on 2022-02-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=201)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product_photo', models.ImageField(default='/images/kohala-full-size-steel-string-acoustic-guitar.jpg', null=True, upload_to='images/')),
            ],
        ),
    ]
