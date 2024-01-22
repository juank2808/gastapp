from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        # Puedes agregar dependencias si es necesario
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True)),
                ('password', models.CharField(max_length=128)),
                ('date_birth', models.DateField()),
                ('last_login', models.DateTimeField(default=None, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
