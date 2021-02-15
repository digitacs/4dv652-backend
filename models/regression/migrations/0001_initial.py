# Generated by Django 3.1.6 on 2021-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LRRequest',
            fields=[
                ('Id', models.UUIDField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('aimoscore', models.DecimalField(blank=True, decimal_places=24, max_digits=25, null=True)),
                ('No_1_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_2_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_3_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_4_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_5_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_6_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_7_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_8_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_9_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_10_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_11_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_12_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_13_Angle_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_1_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_2_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_3_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_4_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_5_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_6_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_7_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_8_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_9_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_10_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_11_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_12_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_13_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_14_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_15_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_16_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_17_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_18_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_19_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_20_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_21_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_22_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_23_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_24_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_25_NASM_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_1_Time_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('No_2_Time_Deviation', models.DecimalField(decimal_places=24, max_digits=25)),
                ('estimatedscore', models.DecimalField(blank=True, decimal_places=24, max_digits=25, null=True)),
                ('score', models.DecimalField(decimal_places=24, max_digits=25)),
            ],
        ),
    ]
