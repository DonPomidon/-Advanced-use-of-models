from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name


class Teacher(Person):
    subject = models.CharField(max_length=100)


class ClassDetails(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(Person):
    class_details = models.ForeignKey(ClassDetails, on_delete=models.CASCADE)
    age = models.IntegerField()
    attendance = models.IntegerField()


class AdultStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)


class AdultStudent(Student):
    object = AdultStudentManager()

    class Meta:
        proxy = True


class YoungStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__lt=18)


class YoungStudent(Student):
    object = YoungStudentManager()

    class Meta:
        proxy = True
