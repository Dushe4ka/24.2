# Generated by Django 5.0.7 on 2024-07-14 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="course_or_lesson",
        ),
        migrations.AddField(
            model_name="payment",
            name="paid_course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="paid_course",
                to="materials.course",
                verbose_name="Оплаченный курс",
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="paid_lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="paid_lesson",
                to="materials.lesson",
                verbose_name="Оплаченный урок",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "наличные"), ("card", "банковский перевод")],
                default="card",
                max_length=35,
                verbose_name="Способ оплаты",
            ),
        ),
    ]