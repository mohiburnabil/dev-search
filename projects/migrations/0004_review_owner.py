# Generated by Django 4.1 on 2022-10-25 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_profile_skills_skill_owner"),
        ("projects", "0003_project_developer"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
