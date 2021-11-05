from django.db import models
from django.core.exceptions import ValidationError

def content_file_name(instance, filename):
   return "{folder}/{file}".format(folder=instance.last_name, file=filename)

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Error message')

# Create your models here.
class InternatDocuments(models.Model):

    CLASS_CHOICE = (('7', '7'),
                    ('8', '8'),
                    ('9', '9'))
    REGION_CHOICE = (('Нур-Султан','Нур-Султан'),
                     (' Алматы', ' Алматы'),
                     ('Шымкент', 'Шымкент'),
                     ('Алматинская область', 'Алматинская область'),
                     ('Акмолинская область', 'Акмолинская область'),
                     ('Атырауская область', 'Атырауская область'),
                     ('Актюбинская область', 'Актюбинская область'),
                     ('Восточно-Казахстанская область', 'Восточно-Казахстанская область'),
                     (' Жамбылская область', ' Жамбылская область'),
                     ('Западно-Казахстанская область', 'Западно-Казахстанская область'),
                     ('Карагандинская область', 'Карагандинская область'),
                     ('Костанайская область', 'Костанайская область'),
                     ('Кызылординская область', 'Кызылординская область'),
                     ('Мангистауская область', 'Мангистауская область'),
                     ('Павлодарская область', 'Павлодарская область'),
                     ('Северо-Казахстанская область', 'Северо-Казахстанская область'),
                     ('Туркестанская область', 'Туркестанская область'),
                     )
    GENDER_CHOICE = (
                    ('мужской', 'мужской'),
                    ('женский', 'женский'),)

    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    category = models.CharField(max_length=70, choices=CLASS_CHOICE, verbose_name='Выберите класс',default='7')
    oblast = models.CharField(max_length=100, choices=REGION_CHOICE, verbose_name='Область', default='Туркестанская область')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='мужской', verbose_name='Пол')
    zayavlenye = models.FileField(upload_to=content_file_name,validators=[validate_file_extension], help_text='Формат файла pdfs')
    copy_svid_rozh = models.FileField(upload_to=content_file_name, verbose_name='Копия свидетельства о рождении', validators=[validate_file_extension], help_text='Формат файла pdfs')
    copy_vkl_roj_IIN = models.FileField(upload_to=content_file_name, verbose_name='Копия вкладыша к свидетельству о рождении с указанием ИИН', validators=[validate_file_extension])
    copy_udos_lich = models.FileField(upload_to=content_file_name, verbose_name='Копия удостоверения личности', validators=[validate_file_extension])
    copy_udos_lich_rod = models.FileField(upload_to=content_file_name, verbose_name='копия удостоверения личности законных представителей учащегося', validators=[validate_file_extension])
    adress_reg_vseh = models.FileField(upload_to=content_file_name, verbose_name='Данные по адресу регистрации учащегося и его законных представителей с портала электронного правительства egov.kz', validators=[validate_file_extension])
    copy_prikaz_rab = models.FileField(upload_to=content_file_name, verbose_name='Копия приказа о принятии на работу, справка с места работы', validators=[validate_file_extension])
    sprv_akima_or_egov = models.FileField(upload_to=content_file_name, verbose_name='Данные с портала элек. прав. egov.kz или справка акима поселка ...', validators=[validate_file_extension])
    sprv_rab_zrpl_or_mest_ispol_org = models.FileField(upload_to=content_file_name, verbose_name='Справка с места работы зар. пл.', validators=[validate_file_extension])
    inform_gnpf = models.FileField(upload_to=content_file_name, verbose_name='Информация о поступлении и движении средств вкладчика единого накопительного пенсионного фонда', validators=[validate_file_extension])
    copy_svd_rozh_mnodet = models.FileField(upload_to=content_file_name, verbose_name='Справка от многодетных матерей', validators=[validate_file_extension])
    sprv_invd = models.FileField(upload_to=content_file_name, verbose_name='Справка о инвалидности', validators=[validate_file_extension])
    sprv_asp = models.FileField(upload_to=content_file_name, verbose_name='Справка о АСП')
    sprv_neblag_semya = models.FileField(upload_to=content_file_name, verbose_name='Справка подтверждающую постановку на учет заявителя и его семьи в качестве неблагополучной семьи', validators=[validate_file_extension])
    copy_doc_nepol_semya = models.FileField(upload_to=content_file_name, verbose_name='Копия документов подтверждающих отсуствие одного из родителей', validators=[validate_file_extension])

    def __str__(self):
        return  self.first_name + self.last_name