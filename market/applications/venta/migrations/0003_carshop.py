# Generated by Django 3.0.6 on 2020-05-15 00:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_product_num_sale'),
        ('venta', '0002_auto_20200514_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Venta')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_car', to='producto.Product', verbose_name='producto')),
            ],
            options={
                'verbose_name': 'Carrito de compras',
                'verbose_name_plural': 'Carrito de compras',
            },
        ),
    ]
