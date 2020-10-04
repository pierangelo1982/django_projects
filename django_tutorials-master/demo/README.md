docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=passworddb -d mysql

docker run --name django-phpmyadmin -d --link django-mysql:db -p 8081:80 phpmyadmin/phpmyadmin



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django.test',
        'USER': 'root',
        'PASSWORD': 'passworddb',
        'HOST': '0.0.0.0',
        'PORT': '3306',
    }
}


    def __str__(self):
       return self.titolo

    def __unicode__(self):
       return self.denominazione

    class Meta:
        verbose_name_plural = "Anagrafica Aziende"
        ordering = ['denominazione']



