from django.db import models

class task(models.Model):
    activate_data = models.DateTimeField()
    task_name = models.CharField(max_length=200)

    def __str__(self):
        return self.task_name
    
