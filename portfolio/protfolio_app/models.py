from django.db import models


# class Project(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     short_description = models.CharField(max_length=200, null=True)
#     description = models.TextField(null=True)
#     # pub_date = models.TimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class ProjectImage(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
#     image = models.ImageField

#     def __str__(self):
#         return self.project
