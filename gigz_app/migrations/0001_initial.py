# Generated by Django 3.0.4 on 2020-03-12 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('website_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Audition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('roles', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.TextField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditions', to='gigz_app.Venue')),
            ],
        ),
    ]
