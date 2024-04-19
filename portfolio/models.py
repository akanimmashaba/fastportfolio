from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    self_image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    email = models.EmailField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Project/', null=True, blank=True)
    description = models.TextField()
    github_link = models.URLField()
    demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title