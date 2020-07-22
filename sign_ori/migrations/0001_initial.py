# Generated by Django 3.0.3 on 2020-07-21 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False, verbose_name='account_id')),
                ('user_id', models.CharField(max_length=20)),
                ('user_pw', models.CharField(max_length=16)),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('user_type', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='t_list',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False, verbose_name='table_id')),
                ('field_main', models.CharField(max_length=20)),
                ('field_sub', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.Accounts')),
            ],
            options={
                'db_table': 't_list',
            },
        ),
    ]