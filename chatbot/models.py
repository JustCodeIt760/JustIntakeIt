from django.db import models
from project_initiation.models import Project

class ChatSession(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='chat_sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    context = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Chat Session for Project {self.project.id} at {self.created_at}"