# Generated by Django 4.1 on 2022-10-03 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_rename_descriptoin_skill_description"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="skills",),
        migrations.AddField(
            model_name="skill",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
