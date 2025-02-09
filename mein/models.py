<<<<<<< HEAD
from django.db import models     # type: ignore
=======
from django.db import models
>>>>>>> 0984425 (1-commit)




<<<<<<< HEAD
class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=30, verbose_name='Famila')
    yosh = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.first_name
    

class Davomat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='davomat')
    sana = models.DateField()

    def __str__(self) -> str:
        return f"{str(self.group.name)} jamoasining {str(self.sana)} sanadagi davomadi."
    


class Belgi(models.Model):
    davomat = models.ForeignKey(Davomat, on_delete=models.CASCADE, related_name='davomat_belgi')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_belgi')
    is_attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['davomat', 'student']
=======
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


>>>>>>> 0984425 (1-commit)

