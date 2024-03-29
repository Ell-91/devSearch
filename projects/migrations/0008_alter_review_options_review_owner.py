# Generated by Django 4.2.3 on 2023-09-30 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
        ("projects", "0007_alter_project_featured_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ["created"]},
        ),
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
