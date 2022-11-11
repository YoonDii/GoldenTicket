

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationid', models.CharField(max_length=20)),
                ('locationname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('relateurl', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=20)),
                ('lgt', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playid', models.CharField(max_length=20)),
                ('playname', models.CharField(max_length=50)),
                ('genrename', models.CharField(max_length=20)),
                ('playstate', models.CharField(max_length=20)),
                ('playstdate', models.CharField(max_length=20)),
                ('playenddate', models.CharField(max_length=20)),
                ('poster', models.ImageField(blank=True, upload_to='images/')),
                ('locationname', models.CharField(max_length=30)),
                ('playcast', models.CharField(max_length=50)),
                ('runtime', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('locationid', models.CharField(max_length=20)),
                ('image1', models.ImageField(blank=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
