# Generated by Django 3.2.3 on 2021-05-21 03:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('max_no_of_applications', models.IntegerField()),
                ('max_no_of_positions', models.IntegerField()),
                ('date_of_posting', models.DateTimeField(default=datetime.datetime(2021, 5, 21, 3, 29, 8, 526638, tzinfo=utc))),
                ('deadline', models.DateTimeField()),
                ('type', models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-TIme'), ('WH', 'Work from Home')], default='FT', max_length=2)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('salary', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('bio', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Required',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.job')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.language')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.recruiter'),
        ),
        migrations.CreateModel(
            name='Has_skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.applicant')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.language')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=100)),
                ('start_year', models.PositiveSmallIntegerField()),
                ('end_year', models.PositiveSmallIntegerField(null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sop', models.CharField(max_length=1500)),
                ('status', models.CharField(choices=[('AP', 'Applied'), ('SH', 'Shortlisted'), ('AC', 'Accepted'), ('RE', 'Rejected')], default='AP', max_length=2)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='total.job')),
            ],
        ),
    ]