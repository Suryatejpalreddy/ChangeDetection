# Generated by Django 4.2.15 on 2024-08-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='images',
            name='path1',
            field=models.ImageField(upload_to='webapp/static/image1'),
        ),
        migrations.AlterField(
            model_name='images',
            name='path2',
            field=models.ImageField(upload_to='webapp/static/image2'),
        ),
    ]