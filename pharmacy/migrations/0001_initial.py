# Generated by Django 4.1.9 on 2023-07-06 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('purchased', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_id', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('featured_image', models.ImageField(blank=True, default='medicines/default.png', null=True, upload_to='medicines/')),
                ('description', models.TextField(blank=True, null=True)),
                ('medicine_type', models.CharField(blank=True, choices=[('tablets', 'tablets'), ('syrup', 'syrup'), ('capsule', 'capsule'), ('general', 'general')], max_length=200, null=True)),
                ('medicine_category', models.CharField(blank=True, choices=[('fever', 'fever'), ('pain', 'pain'), ('cough', 'cough'), ('cold', 'cold'), ('flu', 'flu'), ('diabetes', 'diabetes'), ('eye', 'eye'), ('ear', 'ear'), ('allergy', 'allergy'), ('asthma', 'asthma'), ('bloodpressure', 'bloodpressure'), ('heartdisease', 'heartdisease'), ('vitamins', 'vitamins'), ('digestivehealth', 'digestivehealth'), ('skin', 'skin'), ('infection', 'infection'), ('nurological', 'nurological')], max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('stock_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Prescription_reqiuired', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('pharmacist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, default='pharmacist/user-default.png', null=True, upload_to='doctors/')),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(blank=True, max_length=200, null=True)),
                ('trans_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('orderitems', models.ManyToManyField(to='pharmacy.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicine'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
