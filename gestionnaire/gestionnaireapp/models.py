from django.db import models

# Create your models here.

class Niveaux(models.Model):
    name = models.CharField(max_length=200)
    codeniveau = models.CharField(max_length=100)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveaux'

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=200)
    niveau = models.ForeignKey(Niveaux, on_delete= models.CASCADE, related_name='niveauclas')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name


class Matieres(models.Model):
    name = models.CharField(max_length=200)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'

    def __str__(self):
        return self.name

class Professeurs(models.Model):
    name = models.CharField(max_length=200)
    datenaiss = models.DateTimeField()
    telephone = models.CharField(max_length=10)

    password = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matieres, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to ='profiles/')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Professeur'
        verbose_name_plural = 'Professeurs'

    def __str__(self):
        return self.name

class Eleves(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    datenaiss = models.DateTimeField()

    matricule = models.CharField(max_length=10)
    classe = models.ForeignKey(Classes, on_delete = models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Eleve'
        verbose_name_plural = 'Eleves'

    def __str__(self):
        return str(self.name)

class Notes(models.Model):
    note = models.IntegerField(default=0)
    matiere = models.ForeignKey(matiere, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleves, on_delete = models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return str(self.note)
