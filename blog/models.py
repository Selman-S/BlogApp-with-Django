from django.db import models

# Create your models here.

class Blog(models.Model):
  title = models.CharField('Başlık',max_length=100)
  content = models.TextField('Açıklama',max_length=350)
  avatar = models.ImageField('Resim', blank=True, null=True, upload_to='media/')
  comment_count = models.IntegerField('Yorum sayısı')
  view_count = models.IntegerField('Görüntülenme')
  like_count = models.IntegerField('Beğeni sayısı')
  publish_date = models.DateField('Yayınlanma tarihi',auto_now_add=True)

  def __str__(self):
    return f'{self.title}'

  class Meta:
    ordering = ['publish_date']