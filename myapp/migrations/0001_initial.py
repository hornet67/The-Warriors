# Generated by Django 5.1 on 2024-09-20 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('AlbionUsername', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=150, unique=True)),
                ('Total_fame', models.CharField(max_length=50)),
                ('Kill_fame', models.CharField(max_length=50)),
                ('Playerkill', models.IntegerField(default=0)),
                ('Server', models.CharField(choices=[('Asia', 'Asia'), ('Europe', 'Europe'), ('N.America', 'N.America')], default='Asia', max_length=12)),
                ('GuildMember', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=5)),
                ('Guildmemebertype', models.CharField(choices=[('Founder', 'Founder'), ('CoCaptain', 'CoCaptain'), ('Member', 'Member'), ('Recuit', 'Recuit')], default='Recuit', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Profile/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_member', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
