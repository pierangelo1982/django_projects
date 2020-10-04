# coding=utf-8
__author__ = 'pierangelo'

import os
import re
import time
from os import path
import pykml
from pykml import parser
import lxml
from fastkml import kml


from django.conf import settings


def elabora(mypath, mymarker, mycolor, myfilename):
	## importo il KML originale
	percorso = path.join(mypath)
	imp = file(percorso).read()
	## creo un kml con modifiche
	out = open("out.kml", 'w')  # out file

	# ## creo l'array con i colori presenti nel KML
	tag_colore = re.findall(r"(?<=<color>)(.*?)(?=</color>)", imp)

	## lista dei colori ottenuti, rimpiazzo il colore e scrivo dentro imp,
	## imp, ovvero stringa del KML originale che poi salvo nel nuovo kml.
	for x in tag_colore:
		editdoc = imp.replace(x, mycolor)

	# write fuori dal loop perchè altrimenti salvava tutto kml per numero dei loop
	out.write(editdoc)
	out.close()

	# apro kml appena generato
	path_out = path.join("out.kml")
	imp = file(path_out).read()

	## nuovo file kml
	#kml_name = str(time.time()) + ".xml"
	outmarker = open(settings.MEDIA_ROOT + "uploads/kml/" + myfilename, 'w')  # out file

	tag_marker = re.findall(r"(?<=<href>)(.*?)(?=</href>)", imp)

	for t in tag_marker:
		editmarker = imp.replace(t, mymarker)

	#write fuori dal loop perchè altrimenti salvava tutto kml per numero dei loop
	outmarker.write(editmarker)
	outmarker.close()
	return path.join(myfilename)