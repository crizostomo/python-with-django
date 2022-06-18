from django.db import models

class Base(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Appraisal(Base):
    course = models.ForeignKey(Course, related_name='appraisals', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    appraisal = models.DecimalField(max_digits=2, decimal_places=1) #4.8, 10.0

    class Meta:
        verbose_name = 'Appraisal'
        verbose_name_plural = 'Appraisals'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} appraised the course {self.course} with grade {self.appraisal}'


