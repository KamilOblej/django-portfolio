from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = ' About me'
        verbose_name_plural = 'About me'

    def __str__(self):
        return (self.name)


class Skill(models.Model):
    # pass
    name = models.TextField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Project(models.Model):
    pass
    # name = models.CharField(max_length=100)
    # short_description = models.CharField(max_length=200)
    # description = models.TextField(null=False)
    # thumbnail_image = models.ImageField()

    # def __str__(self):
    #     return self.name


class ProjectImage(models.Model):
    pass
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100, null=False)
    # pub_date = models.DateField()
    # image = models.FileField()
