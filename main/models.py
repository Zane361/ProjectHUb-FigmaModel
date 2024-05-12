from django.db import models
from random import sample
import string


class CodeGenerate(models.Model):
    code = models.CharField(max_length=255, blank=True,unique=True)
    
    @staticmethod
    def generate_code():
        return ''.join(sample(string.ascii_letters + string.digits, 15)) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                code = self.generate_code()
                if not self.__class__.objects.filter(code=code).count():
                    self.code = code
                    break
        super(CodeGenerate,self).save(*args, **kwargs)


    class Meta:
        abstract = True


class Home(CodeGenerate):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='home/')

    def __str__(self):
        return self.title
    

class Portfolio(CodeGenerate):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    url = models.URLField()

    def __str__(self):
        return self.title


class TeamMember(CodeGenerate):
    job = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='member/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Message(CodeGenerate):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    body = models.TextField()


class Vacancy(CodeGenerate):
    work_days = models.IntegerField()
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    least_salary = models.IntegerField()
    most_salary = models.IntegerField()
    requirements = models.TextField()
    tasks = models.TextField()
    technology = models.TextField()


class Resume(CodeGenerate):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resume/')