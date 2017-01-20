from django.db import models


class Job(models.Model):
    # TYPES = (
    #     ('fibonacci', 'fibonacci'),
    #     ('power', 'power'),
    #     ('github','github')
    # )

    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    # type = models.CharField(choices=TYPES, max_length=20)
    type = 'github'                 #creating a choices tuple can enable to add more functions
    status = models.CharField(choices=STATUSES, max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # argument = models.PositiveIntegerField()
    argument = models.CharField(max_length=100,help_text="Enter the github profile name")
    # result = models.CharField(null=True, max_length=1000)
    result = models.TextField(default="None")

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.type]
            task.delay(job_id=self.id, str=self.argument)