from django.db import models

from django.core.validators import FileExtensionValidator

class CsvFiles(models.Model):
    nome = models.CharField(max_length=50, default='testeParsing')
    csv = models.FileField(upload_to='FileReceiver/', validators = [ FileExtensionValidator( ['csv'] ) ])

    def __str__(self):
            return f'CsvFiles {self.pk} |  {self.csv}' #{self.nome}

