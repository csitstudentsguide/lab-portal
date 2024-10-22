from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

import magic

ext_validator = FileExtensionValidator(['pdf', 'doc', 'docx'])

def validate_file_mimetype(file):
    accept = ['application/pdf']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    print(file_mime_type)
    if file_mime_type not in accept:
        raise ValidationError('Unsupported file type')

YEAR = [('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')]

SEM = [('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII')]

PROGRAMME = [('BTECH', 'BTech'), ('MBATECH', 'MBATech')]

SUBJECTS = [
    ('PPS', 'Programming for Problem Solving'), ('PP', 'Python Programming'),
    ('ECS', 'Essentials of Computer Science'), ('PEM', 'Principles of Economics and Management'),
    ('DCCA', 'Digital Circuits and Computer Architecture'), ('CN', 'Computer Networks'),
    ('DEP', 'Data Extraction and Processing'), ('DSA', 'Data Structures and Algorithms'),
    ('SE', 'Software Engineering'), ('CD', 'Compiler Design'),
    ('IVP', 'Image and Video Processing'), ('OS', 'Operating Systems'),
    ('ADBMS', 'Advanced Database Management Systems'), ('3DP', '3D Printing'),
    ('DT', 'Drone Technology'), ('EA', 'Elements of Automation'),
    ('GD', 'Game Design'), ('ML', 'Machine Learning'),
    ('CNS', 'Cryptography and Network Security'),
    ('BT', 'Blockchain Technology'), ('NLP', 'Natural Language Processing'),
    ('BDA', 'Big Data Analytics'), ('PS', 'Probability and Statistics'),
    ('DLS', 'Digital Logic Design'), ('AI', 'Artificial Intelligence'),
    ('MAD', 'Mobile Application Development'), ('OR', 'Operation Research'),
    ('CC', 'Cloud Computing'), ('DL', 'Deep Learning'), ('IOTA', 'IoT and Applications'),
    ('AWP', 'Advanced Web Programming'),
]

EXP_NO = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')]

AY = [('2024-25', '2024-25'), ('2025-26', '2025-26'), ('2026-27', '2026-27')]

TERM = [('ODD', 'Odd'), ('EVEN', 'Even')]

# Create your models here.
class ExpLists(models.Model):
    programme = models.CharField(max_length=10, choices=PROGRAMME)
    year = models.CharField(max_length=10, choices=YEAR)
    sem = models.CharField(max_length=5, choices=SEM)    
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    exp_no = models.CharField(max_length=50, choices=EXP_NO)
    ay = models.CharField(max_length=50, choices=AY)
    term = models.CharField(max_length=50, choices=TERM)
    exp_file = models.FileField(upload_to='exp_lists/%Y/%m', validators=[ext_validator], blank=False)

    #class Meta:
    #    unique_together = ['subject', 'exp_no']
       
    
    def __str__(self):
        return self.subject
    
