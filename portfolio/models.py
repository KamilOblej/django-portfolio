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
    name = models.CharField(max_length=100, default='null')
    short_description = models.CharField(max_length=200, default='null')
    description = models.TextField(default='null')
    thumbnail_image = models.ImageField(null=False)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    # pass
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Icon(models.Model):
    name = models.CharField(max_length=50, null=False)
    font_avesome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class SocialIcon(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    link = models.TextField()

    def __str__(self):
        return self.icon.name
