# Generated by Django 4.2.4 on 2023-08-16 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundingdetail',
            old_name='funding_header_id',
            new_name='funding_header',
        ),
        migrations.RenameField(
            model_name='fundingheader',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='fundinginquiry',
            old_name='funding_header_id',
            new_name='funding_header',
        ),
        migrations.RenameField(
            model_name='fundinginquiry',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='fundinginquiryanswer',
            old_name='funding_inquiry_id',
            new_name='funding_inquiry',
        ),
        migrations.RenameField(
            model_name='fundinginquiryanswer',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='fundingreply',
            old_name='funding_header_id',
            new_name='funding_header',
        ),
        migrations.RenameField(
            model_name='fundingreply',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='fundingsponsor',
            old_name='funding_header_id',
            new_name='funding_header',
        ),
        migrations.RenameField(
            model_name='fundingsponsor',
            old_name='member_id',
            new_name='member',
        ),
    ]
