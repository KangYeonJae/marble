from django.db import models

# Create your models here.
class Blog(models.Model):
    Gu = (
    (0, '강남구'),
    (1, '강동구'),
    (2, '강북구'),
    (3, '강서구'),
    (4, '관악구'),
    (5, '광진구'),
    (6, '구로구'),
    (7, '금천구'),
    (8, '노원구'),
    (9, '도봉구'),
    (10, '동대문구'),
    (11, '동작구'),
    (12, '마포구'),
    (13, '서대문구'),
    (14, '서초구'),
    (15, '성동구'),
    (16, '성북구'),
    (17, '송파구'),
    (18, '양천구'),
    (19, '영등포구'),
    (20, '용산구'),
    (21, '은평구'),
    (22, '종로구'),
    (23, '중구'),
    (24, '중랑구'),
    )
    address1 = models.IntegerField(null=True, choices=Gu)
    address2 = models.CharField(max_length=50)
    address3 = models.CharField(max_length=100)
    deadline = models.DateTimeField('data published')
    bill = models.IntegerField()
    pet = models.BooleanField()
    title = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.title


