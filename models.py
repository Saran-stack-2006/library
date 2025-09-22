from django.db import models

# Create your models here.



class AdminUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # We'll hash the password for security

    def __str__(self):
        return self.username

from django.db import models

class CollegeStudent(models.Model):   # ✅ Student table
    student_id = models.CharField(max_length=100, unique=True)  # Barcode ID
    student_name = models.CharField(max_length=200)             # Student name

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"


class Book(models.Model):   # ✅ Book table
    scanner = models.CharField(max_length=100, unique=True)  # Barcode/Book ID
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    abstract = models.TextField(null=True)
    available = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.title} ({self.scanner})"

    



from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True, null=False, blank=False)
    student_name = models.CharField(max_length=100, null=True, blank=True)  # optional name

    def __str__(self):
        return f"{self.student_name or 'Unknown'} ({self.student_id})"
from django.db import models

from django.db import models

class Borrow(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)   # ✅ when book is returned
    borrow_duration_days = models.IntegerField(null=True, blank=True)  # ✅ optional: store difference in days

    class Meta:
        db_table = "borrow_records"   # existing table name

    def _str_(self):
        return f"{self.student_name} - {self.book_name}"

