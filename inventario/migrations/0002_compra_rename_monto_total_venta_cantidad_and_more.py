# Generated by Django 4.2 on 2024-09-25 22:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(default=datetime.date.today)),
                ('cantidad', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'compra_elementos',
            },
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='monto_total',
            new_name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='elementos',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='fecha',
        ),
        migrations.AddField(
            model_name='element',
            name='comprador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='venta',
            name='elemento',
            field=models.ManyToManyField(to='inventario.element'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterModelTable(
            name='venta',
            table='venta_elementos',
        ),
        migrations.DeleteModel(
            name='Compra_elemento',
        ),
        migrations.AddField(
            model_name='compra',
            name='elemento',
            field=models.ManyToManyField(to='inventario.element'),
        ),
    ]
