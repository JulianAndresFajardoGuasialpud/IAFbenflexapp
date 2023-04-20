from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('IAFBenflex', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['username', 'id']},
            options={'ordering': ['id', 'username']},
        ),
    ]
