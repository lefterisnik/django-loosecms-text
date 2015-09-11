# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text=b'Give some title.', max_length=200, verbose_name='title')),
                ('body', loosecms.fields.LoosecmsRichTextField(verbose_name='body')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            bases=('loosecms.plugin',),
        ),
    ]
