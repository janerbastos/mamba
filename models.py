# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.text import slugify

from databases.constants import CHOOSE_STATUS, CHOOSE_CATEGORIA, CHOOSE_TIPO_CONTENT


class Site(models.Model):
    url = models.SlugField(max_length=150, unique=True)
    titulo = models.CharField('Título', max_length=150)
    descricao = models.TextField('Breve descrição', default=None, null=True, blank=True)
    create_at = models.DateField('Data de criação', auto_now_add=True)
    update_at = models.DateField('Data de atualização', null=True, blank=True, default=None)
    status = models.BooleanField(default=False, choices=CHOOSE_STATUS)
    facebook_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    twitter_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    youtube_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    google_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    flicker_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    rss_link = models.URLField(max_length=255, null=True, blank=True, default=None)
    logo = models.ImageField('Logo do site', upload_to='imagens/site/', blank=True, null=True, default=None)
    banner_topo = models.ImageField('Banner de destaque', upload_to='imagens/site/', blank=True, null=True, default=None)
    favicon = models.ImageField('Favicon', upload_to='imagens/site/', blank=True, null=True, default=None)
    texto_rodape = models.TextField(default=None, blank=True, null=True)
    facebook_cod = models.TextField(null=True, blank=True, default=None)
    twitter_cod = models.TextField(null=True, blank=True, default=None)
    youtube_cod = models.TextField(null=True, blank=True, default=None)
    google_cod = models.TextField(null=True, blank=True, default=None)
    flicker_cod = models.TextField(null=True, blank=True, default=None)
    analytic_cod = models.TextField(null=True, blank=True, default=None)
    html_cod = models.TextField(null=True, blank=True, default=None)
    email = models.EmailField(max_length=255, null=True, blank=True, default=None)
    telefone = models.CharField(max_length=255, null=True, blank=True, default=None)
    workflow = models.CharField(max_length=20, default='privado', choices=CHOOSE_CATEGORIA)
    content_type_permissao = models.ManyToManyField('ContentType', related_name='list_permissao_tipo', )

    def __unicode__(self):
        return self.titulo

    @property
    def get_configure_url(self):
        return '/manage/sites/%s/' % self.url

    def get_absolute_url(self):
        return '/%s/' % self.url

    @property
    def get_map_site(self):
        return '/%s/@@map_site/' % self.url

    def save(self, **kwargs):
        if not self.url:
            self.url = slugify(self.titulo)
        if self.id:
            self.update_at = datetime.datetime.now()
        super(Site, self).save()


class ContentType(models.Model):
    tipo = models.CharField(max_length=20, choices=CHOOSE_TIPO_CONTENT, unique=True)
    descricao = models.CharField(max_length=20)

    def __unicode__(self):
        return self.descricao
