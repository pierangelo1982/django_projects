from django.db import models
from django.utils.safestring import mark_safe

class Post(models.Model):
    titolo = models.CharField('Titolo', max_length=250, null=False, blank=True)
    descrizione = models.TextField('Descrizione', null=True, blank=True)
    image = models.ImageField('Immagine', null=True, blank=True, upload_to='post_image')
    tag =  models.CharField('Parole Chiave', max_length=250, null=True, blank=True)
    active = models.BooleanField('Pubblicato', null=False, default=False)
    pub_date = models.DateTimeField('date published')

    def image_img(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px"/>' % self.image.url)
        else:
            return '(Nessuna Immagine)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __str__(self):
       return self.titolo

    class Meta:
        verbose_name_plural = "Post"
        ordering = ['-pub_date']