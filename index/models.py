from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date_of_burn = models.DateField()

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    phone = models.CharField(max_length=255)
    sell_by = models.DateField()
    year_of_issue = models.DateField()

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


from django.db import models


class MyPort(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='my_port', null=True, blank=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Списки портфолио'


from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def str(self):
        return self.mark

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'Список машин'


class Person(models.Model):
    name = models.CharField(max_length=100)
    sure_name = models.CharField(max_length=100)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images", null=True, blank=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Жаран'
        verbose_name_plural = 'Жарандар'

