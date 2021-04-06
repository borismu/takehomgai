# Generated by Django 3.1.7 on 2021-04-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('STARTING', 'STARTING'), ('STARTED', 'STARTED'), ('WAITING', 'WAITING'), ('EXECUTING', 'EXECUTING'), ('STOPPING', 'STOPPING'), ('STOPPED', 'STOPPED')], default='STARTING', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]