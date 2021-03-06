# Generated by Django 3.0.6 on 2020-08-14 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('tracker', '0002_auto_20200809_0111'),
	]

	operations = [
		migrations.AddField(
			model_name='jobapp',
			name='active',
			field=models.BooleanField(default=True),
		),
		migrations.AlterField(
			model_name='jobappstep',
			name='date',
			field=models.DateField(default=datetime.date(2020, 8, 14)),
		),
		migrations.AlterField(
			model_name='jobappstep',
			name='step',
			field=models.CharField(choices=[('talk', 'talked at event'), ('resm', 'gave resume'), ('covr', 'gave cover letter'), ('appl', 'applied via job posting'), ('flup', 'follow-up'), ('chln', 'coding challenge/test'), ('intv', 'interview')], default='resm', max_length=50),
		),
	]
