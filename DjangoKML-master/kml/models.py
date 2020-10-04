from __future__ import unicode_literals

from django.db import models

from kml import KMLeditor
from KMLeditor import elabora

from django.conf import settings


class Path(models.Model):
    titolo = models.CharField(blank=True, null=True, max_length=255, verbose_name="Titolo Italiano")
    marker = models.ImageField(blank=True, null=True, upload_to='marker')
    colore = models.CharField(blank=True, null=True, max_length=255,
        verbose_name="Colore Riferimento Percorso", help_text="For more information about KML color: http://www.netdelight.be/kml/index.php")
    mappa = models.FileField(upload_to='uploads/kml/', blank=True, null=True)
    kml_ok = models.FileField(upload_to='uploads/kml/', editable=False, blank=True, null=True)

    def mykml(self, *args, **kwargs):
        source_kml = settings.MEDIA_ROOT + str(self.mappa)
        source_marker = settings.MEDIA_URL + str(self.marker)
        source_color = str(self.colore)
        source_filename = str(self.titolo.strip()) + ".kml"
        #elab = str(elabora(source_kml,  source_marker, source_color, source_filename))
        self.kml_ok = "uploads/kml/" + str(elabora(source_kml,  source_marker, source_color, source_filename))
        super(Path, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "KML"

    def __unicode__(self):
        return self.titolo
