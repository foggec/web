# Generated by Django 5.0.6 on 2024-07-01 14:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_alter_artic_pre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('completed', models.ManyToManyField(blank=True, related_name='completed', to='books.artic')),
                ('reading', models.ManyToManyField(blank=True, related_name='reading', to='books.artic')),
                ('reaed', models.ManyToManyField(blank=True, related_name='reaed', to='books.artic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('want_to_read', models.ManyToManyField(blank=True, related_name='want_to_read', to='books.artic')),
            ],
        ),
    ]
