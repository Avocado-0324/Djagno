# Generated by Django 5.0.6 on 2024-07-10 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtodos', to='Todolist.todo')),
            ],
        ),
    ]
