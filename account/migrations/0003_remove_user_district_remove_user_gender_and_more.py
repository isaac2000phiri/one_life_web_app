# Generated by Django 4.2.6 on 2024-01-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_cover_plan_user_gender_user_phone_home_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='district',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='idNo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_back',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_front',
        ),
        migrations.RemoveField(
            model_name='user',
            name='idtype',
        ),
        migrations.RemoveField(
            model_name='user',
            name='province',
        ),
        migrations.AddField(
            model_name='user',
            name='access_code',
            field=models.UUIDField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='user',
            name='creation_ip_address',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='deletion_ip_address',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='email confirmed'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_id',
            field=models.CharField(blank=True, max_length=900),
        ),
        migrations.AddField(
            model_name='user',
            name='nrc',
            field=models.CharField(blank=True, max_length=300, verbose_name='national registration number'),
        ),
    ]
