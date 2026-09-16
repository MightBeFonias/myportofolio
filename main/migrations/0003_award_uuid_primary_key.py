import uuid

from django.db import migrations, models


def populate_uuid_ids(apps, schema_editor):
    Award = apps.get_model("main", "Award")
    for award in Award.objects.all().iterator():
        award.new_id = uuid.uuid4()
        award.save(update_fields=["new_id"])


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_award"),
    ]

    operations = [
        migrations.AddField(
            model_name="award",
            name="new_id",
            field=models.UUIDField(null=True, editable=False),
        ),
        migrations.RunPython(populate_uuid_ids, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="award",
            name="id",
        ),
        migrations.RenameField(
            model_name="award",
            old_name="new_id",
            new_name="id",
        ),
        migrations.AlterField(
            model_name="award",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
