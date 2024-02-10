# Generated by Django 5.0.1 on 2024-02-10 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_course_date_created_course_date_modified_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('start_date_and_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date_and_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('organizer', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='users.cohort')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_attendee', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_author', to='users.imuser')),
                ('class_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_schedule', to='main.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('resolution_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN PROGRESS'), ('DECLINED', 'DECLINED'), ('RESOLVED', 'RESOLVED')], default='PENDING', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_author', to='users.imuser')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_by', to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='QueryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='users.imuser')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_comment', to='main.query')),
            ],
        ),
    ]
