# Generated by Django 2.1 on 2018-11-12 16:54

from django.db import migrations, models
import hello_django.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPrivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=hello_django.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(storage=hello_django.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]