from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("requests", "0001_initial")]
    operations = [
        migrations.AddField(model_name="giftrequest", name="published_at", field=models.DateTimeField(blank=True, null=True)),
        migrations.AddField(model_name="giftrequest", name="rejection_reason", field=models.TextField(blank=True)),
        migrations.AlterField(model_name="giftrequest", name="status", field=models.CharField(choices=[("draft", "Draft"), ("pending_review", "Pending review"), ("published", "Published"), ("claimed", "Claimed"), ("completed", "Completed"), ("cancelled", "Cancelled"), ("rejected", "Rejected")], default="draft", max_length=32)),
    ]
