from django.db import models
from taggit.managers import TaggableManager
from image_cropping import ImageRatioField, ImageCropField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from ckeditor.fields import RichTextField



# Create your models here.

#class Imageprova(models.Model):
 #   image_field = models.ImageField(upload_to='uploaded_multiimages')

class Image(models.Model):
    image_field = models.ImageField(upload_to='uploaded_images')

#model insert file
class Allegato(models.Model):
        allegato = models.FileField(upload_to="uploaded_allegati")

        class Meta:
                verbose_name_plural = "Allegati"

CATEGORIA_CHOICES = (
    ('televisione', 'Televisione'),
    ('viaggi', 'Viaggi'),
    ('vita', 'Vita'),
    ('sociale', 'Sociale'),
    ('storie', 'Storie'),
)

# MODEL POST
class Post(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=200, null=True, blank=True)
    image = models.ForeignKey(Image)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '250x250')
    croppinghome = ImageRatioField('image__image_field', '100x100')
    #body = models.TextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    tags = TaggableManager()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo


#MODEL Televisione
class Televisione(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=200, null=True, blank=True)
    image = models.ForeignKey(Image)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '350x213')
    youtube = models.CharField(max_length=300, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    galleria_folder = FilerFolderField(null=True, blank=True)
    inizio_programma = models.DateTimeField('Inizio')
    fine_programma = models.DateTimeField('Fine')
    sfondo = models.ImageField(upload_to='uploaded_sfondi', null=True, blank=True)

    class Meta:
                verbose_name_plural = "Televisione"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo

YEAR_CHOICES = (
	('1995', '1995'),
	('1996', '1996'),
	('1997', '1997'),
	('1998', '1998'),
	('1999', '1999'),
	('2000', '2000'),
	('2001', '2001'),
	('2002', '2002'),
	('2003', '2003'),
	('2004', '2004'),
	('2005', '2005'),
	('2006', '2006'),
	('2007', '2007'),
	('2008', '2008'),
	('2009', '2009'),
	('2010', '2010'),
	('2011', '2011'),
	('2012', '2012'),
	('2013', '2013'),
	('2014', '2014'),
	('2015', '2015'),
	('2016', '2016'),
	('2017', '2017'),
	('2018', '2018'),
	('2019', '2019'),
	('2020', '2020'),
	)

#MODEL CURRICULUM
class Curriculum(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    anno = models.CharField(choices=YEAR_CHOICES, max_length=200, null=True, blank=True)
    inizio_programma = models.DateTimeField('Inizio')
    fine_programma = models.DateTimeField('Fine')

    class Meta:
                verbose_name_plural = "Curriculum"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo


#GALLERY CON FILER
class Gallery(models.Model):
    #titolo = models.CharField(max_length=200,  null=True, blank=True)
    #post = models.ForeignKey(Post)
    #didascalia = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='uploaded_galleria')
    image_field = FilerImageField(related_name="book_covers")

    class Meta:
                verbose_name_plural = "Gallery"

#GALLERIA IMMAGINI COLLEGATA A FILER
class Galleria(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    post = models.ForeignKey(Post)
    didascalia = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='uploaded_galleria')
    #image = FilerImageField(related_name="book_covers")
    image = models.ForeignKey(Gallery)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '250x250')
    croppingminiatura = ImageRatioField('image', '350x213')

    class Meta:
                verbose_name_plural = "Galleria Per Post in Blog"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo

#Video Gallery YouTube
class Video(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    programma = models.ForeignKey(Televisione)
    didascalia = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200,  null=True, blank=True)
    embedded = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    class Meta:
                verbose_name_plural = "Video per Televisione"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo

#Episodi
class Episodio(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    programma = models.ForeignKey(Televisione)
    data_onda = models.DateTimeField('Data in Messa in Onda')
    canale = models.CharField(max_length=200,  null=True, blank=True)
    descrizione = RichTextField(null=True, blank=True)
    url = models.CharField(max_length=200,  null=True, blank=True)
    embedded = models.TextField(null=True, blank=True)
    image = models.ForeignKey(Image)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '100x100')
    pub_date = models.DateTimeField('date published')

    class Meta:
                verbose_name_plural = "Episodi"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo



#FOLDER FILER PROVA

class Folder(models.Model):
    #titolo = models.CharField(max_length=200,  null=True, blank=True)
    #post = models.ForeignKey(Post)
    #didascalia = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='uploaded_galleria')
    images_folder = FilerFolderField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.images_folder

PAGINA_CHOICES = (
    ('biografia', 'Biografia'),
    ('un po di me', 'un po di Me'),
    ('contatti', 'Contatti'),
    ('curriculum', 'Curriculum'),
    ('libri', 'Libri'),
)

#GALLERIA IMMAGINI COLLEGATA A FILER PER PAGINE STATICHE
class Galleriapagina(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    pagina = models.CharField(choices=PAGINA_CHOICES, max_length=200, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploaded_galleria')
    image = FilerImageField(related_name="book_covers")
    image = models.ForeignKey(Gallery)
    cropping = ImageRatioField('image__image_field', '800x600')
    croppingthumb = ImageRatioField('image__image_field', '250x250')
    croppingminiatura = ImageRatioField('image', '350x213')

    class Meta:
                verbose_name_plural = "Galleria Pagine Statiche"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo

class Galleriatelevisione(models.Model):
    titolo = models.CharField(max_length=200,  null=True, blank=True)
    programma = models.ForeignKey(Televisione)
    didascalia = models.TextField(null=True, blank=True)
    #image = models.ImageField(upload_to='uploaded_galleria')
    #image = FilerImageField(related_name="book_covers")
    image = models.ForeignKey(Gallery)
    cropping = ImageRatioField('image__image_field', '800x600')
    croppingthumb = ImageRatioField('image__image_field', '250x250')
    croppingminiatura = ImageRatioField('image', '350x213')

    class Meta:
                verbose_name_plural = "Galleria Televisione"

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titolo


