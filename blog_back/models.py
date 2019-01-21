from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    userkname = models.CharField(max_length=10, null=False)
    s_gender = models.BooleanField(default=1)
    userage = models.IntegerField(max_length=3)
    password = models.CharField(max_length=150, null=False)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class Category(models.Model):
    c_name = models.CharField(max_length=10, null=False, unique=True)
    b_name = models.CharField(max_length=10)
    f_id = models.ForeignKey('self', related_name='father', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'category'


class CategoryInfo(models.Model):
    key_words = models.CharField(max_length=20, null=True)
    catinfo = models.CharField(max_length=255, null=True)

    cat = models.OneToOneField(Category, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'catinfo'


class Article(models.Model):
    title = models.CharField(max_length=20, null=False)
    text = models.CharField(max_length=5000, null=False)
    key_words = models.CharField(max_length=30, null=True)
    discribe = models.CharField(max_length=30, null=True)
    c = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name='category')
    tage = models.CharField(max_length=30, null=True)
    icon = models.ImageField(upload_to='uplod', null=True, verbose_name="文章图片")
    add_time = models.DateField(auto_now_add=True, null=True)
    update_time = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'article'
