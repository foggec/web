from django.db import models

class artic(models.Model):
    book_id = models.IntegerField(unique=True)
    title = models.CharField('наименование произведения', max_length=50)
    avtor = models.CharField('автор произведения', max_length=80)
    pre = models.ImageField(default= 'main/img/sxz.png', upload_to='icons')
    idea = models.CharField('жанр.мысль', max_length=150)
    full_t = models.TextField('краткое содержание')
    data = models.DateField('дата публикации')

    def  __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Писание'
        verbose_name_plural = 'Писания'