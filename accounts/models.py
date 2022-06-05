from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

from datetime import date
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    NATIONALITY = (
        ("Afghanistan", 'Afganistan'),
        ("Albania", 'Albania'),
        ("Algeria", 'Algeria'),
        ("America", 'Ameryka'),
        ("Andorra", 'Andora'),
        ("Angola", 'Angola'),
        ("Anguilla", 'Anguilla'),
        ("Argentina", 'Argentyna'),
        ("Armenia", 'Armenia'),
        ("Australia", 'Australia'),
        ("Austria", 'Austria'),
        ("Azerbaijan", 'Azerbaijani'),
        ("the Bahamas", 'Bahamy'),
        ("Bahrain", 'Bahrain'),
        ("Bangladesh", 'Bangladesz'),
        ("Barbados", 'Barbados'),
        ("Barbudans", 'Barbudany'),
        ("Botswana", 'Botswana'),
        ("Belarus", 'Białoruś'),
        ("Belgium", 'Belgia'),
        ("Belize", 'Belize'),
        ("Benin", 'Benin'),
        ("Bhutan", 'Bhutan'),
        ("Bolivia", 'Boliwia'),
        ("Bosnia", 'Bośnia'),
        ("Brazylia", 'Brazylia'),
        ("Britain", 'Wielka Brytania'),
        ("Bruneia", 'Bruneia'),
        ("Bulgaria", 'Bułgaria'),
        ("Burkina Faso", 'Burkina Faso'),
        ("Burma", 'Birma'),
        ("Burgundia", 'Burgundia'),
        ("Cambodia", 'Kambodża'),
        ("Cameroon", 'Kamerun'),
        ("Canada", 'Kanada'),
        ("Cape Verde", 'Republika Zielonego Przylądka'),
        ("Central Africa", 'Centralna Afryka'),
        ("Chad", 'Czad'),
        ("Chile", 'Chile'),
        ("China", 'Chiny'),
        ("Colombia", 'Kolumbia'),
        ("Camorra", 'Camorra'),
        ("Democratic Republic of the Congo", 'Demokratyczna Republika Konga'),
        ("Costa Rica", 'Kostaryka'),
        ("Croatia", 'Chorwacja'),
        ("Cuba", 'Kuba'),
        ("Cyprus", 'Cypr'),
        ("Czechia", 'Czechy'),
        ("Denmark", 'Dania'),
        ("Djibouti", 'Dżibuti'),
        ("Dominica", 'Dominika'),
        ("Holland", 'Holandia'),
        ("East Timor", 'Wschodni Timor'),
        ("Ecuador", 'Ekwador'),
        ("Egypt", 'Egipt'),
        ("United Arab Emirates", 'Zjednoczone Emiraty Arabskie'),
        ("Equatorial Guinea", 'Ginea Równikowa'),
        ("Eritrea", 'Erytrea'),
        ("Estonia", 'Estonia'),
        ("Ethiopia", 'Etiopia'),
        ("Fiji", 'Fidżi'),
        ("Philippines", 'Filipiny'),
        ("Finn", 'Finy'),
        ("France", 'Francja'),
        ("Gabon", 'Gabon'),
        ("Gambia", 'Gambia'),
        ("Georgia", 'Gruzja'),
        ("Germany", 'Niemcy'),
        ("Ghana", 'Ghana'),
        ("Greece", 'Grecja'),
        ("Grenada", 'Grenada'),
        ("Guatemala", 'Guatemala'),
        ("Guinea-Bissau", 'Gwinea Bissau'),
        ("Guinea", 'Gwinea'),
        ("Guyana", 'Gujana'),
        ("Haiti", 'Haiti'),
        ("Herzegovina", 'Hercegowina'),
        ("Honduras", 'Honduras'),
        ("Hungary", 'Węgry'),
        ("Iceland", 'Islandia'),
        ("India", 'Indie'),
        ("Indonesia", 'Indonezja'),
        ("Iran", 'Iran'),
        ("Iraq", 'Irak'),
        ("Ireland", 'Irlandia'),
        ("Israel", 'Izrael'),
        ("Italy", 'Włochy'),
        ("Ivory Coast", 'Wybrzeże Kości Słoniowej'),
        ("Jamaica", 'Jamajka'),
        ("Japan", 'Japonia'),
        ("Jordan", 'Jordania'),
        ("Kazakhstan", 'Kazakhstan'),
        ("Kenya", 'Kenia'),
        ("Kittian and Nevisian", 'Kittan and Nevisian'),
        ("Kuwait", 'Kuwejt'),
        ("Kyrgyzstan", 'Kirgistan'),
        ("Lao", 'Laos'),
        ("Latvia", 'Łotwa'),
        ("Lebanon", 'Liban'),
        ("Liberia", 'Liberia'),
        ("Libya", 'Libia'),
        ("Liechtenstein", 'Liechtenstein'),
        ("Lithuania", 'Litwa'),
        ("Luxembourg", 'Luksemburg'),
        ("Macedonia", 'Macedonia'),
        ("Madagascar", 'Madagaskar'),
        ("Malawi", 'Malawi'),
        ("Malaysia", 'Malezja'),
        ("Maldives", 'Malediwy'),
        ("Malia", 'Malia'),
        ("Malaysia", 'Malezja'),
        ("the Marshall Islands", 'Wyspy Marshalla'),
        ("Mauritania", 'Mauretania'),
        ("Mexic", 'Meksyk'),
        ("Micronesia", 'Mikronezja'),
        ("Moldova", 'Mołdawia'),
        ("Monaco", 'Monako'),
        ("Mongolia", 'Mongolia'),
        ("Morocco", 'Maroko'),
        ("Lesotho", 'Lesotho'),
        ("Mozambique", 'Mozambik'),
        ("Namibia", 'Namibia'),
        ("Nauruan", 'Republika Nauru'),
        ("Nepal", 'Nepal'),
        ("New Zealand", 'Nowa Zelandia'),
        ("Nicaragua", 'Nikaragua'),
        ("Nigeria", 'Nigeria'),
        ("North Korea", 'Korea Północna'),
        ("Norway", 'Norwegia'),
        ("Oman", 'Oman'),
        ("Pakistan", 'Pakistan'),
        ("Palau", 'Palau'),
        ("Panama", 'Panama'),
        ("Papua New Guinea", 'Papua Nowa Gwinea'),
        ("Paraguay", 'Paragwaj'),
        ("Peru", 'Peru'),
        ("Poland", 'Polska'),
        ("Portugal", 'Portugalia'),
        ("Qatar", 'Katar'),
        ("Romania", 'Rumunia'),
        ("Russia", 'Rosja'),
        ("Rwanda", 'Rwanda'),
        ("Saint Lucia", 'Saint Lucia'),
        ("Salvador", 'Salwador'),
        ("Samoa", 'Samoa'),
        ("San Marino", 'San Marino'),
        ("Saudi Arabia", 'Arabia Saudyjska'),
        ("Scotland", 'Szkocja'),
        ("Senegal", 'Senegal'),
        ("Serbia", 'Serbia'),
        ("Seychelles", 'Seszele'),
        ("Sierra Leone", 'Sierra Leone'),
        ("Singapore", 'Singapur'),
        ("Slovakia", 'Słowacja'),
        ("Slovenia", 'Słowenia'),
        ("Solomon Island", 'Wyspa Salomona'),
        ("Somalia", 'Somalia'),
        ("South Africa", 'Połódniowa Afryka'),
        ("South Korea", 'Połódniowa Korea'),
        ("Spain", 'Hiszpania'),
        ("Sri Lanka", 'Sri Lanka'),
        ("Sudan", 'Sudan'),
        ("Surinam", 'Surinam'),
        ("Swaziland", 'Suazi'),
        ("Sweden", 'Szwecja'),
        ("Switzerland", 'Szwajcaria'),
        ("Syria", 'Syria'),
        ("Taiwan", 'Tajwan'),
        ("Tajikistan", 'Tadżykistan'),
        ("Tanzania", 'Tanzania'),
        ("Thailand", 'Tajlandia'),
        ("Togo", 'Togo'),
        ("Tonga", 'Tongo'),
        ("Tobago", 'Tobago'),
        ('Trinidad', 'Trynidad'),
        ("Tunisia", 'Tunezja'),
        ("Turkey", 'Turcja'),
        ("Tuvalu", 'Tuvalu'),
        ("Uganda", 'Uganda'),
        ("Ukraina", 'Ukraine'),
        ("Uruguay", 'Urugwaj'),
        ("Uzbekistan", 'Uzbekistan'),
        ("Venezuela", 'Wenezuela'),
        ("Vietnam", 'Wietnam'),
        ("Wales", 'Walia'),
        ("Yemen", 'Jemen'),
        ("Zambia", 'Zambia'),
        ("Zimbabwe", 'Zimbabwe')
    )
    user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE)
    birthday = models.DateField(default = date.today)
    place_of_birth = models.CharField(
        _('Place Of Birth'), default='Kalisz', max_length=32, blank=False)
    phone_number = PhoneNumberField()
    cellphone_number = PhoneNumberField(null=True)
    nationality = models.CharField(max_length=32, choices=NATIONALITY)
    biography = models.TextField(null=True)
    country = models.CharField(max_length=32, choices=NATIONALITY)
    city = models.CharField(_('City'), max_length=100)
    street_line = models.CharField(_('Address'), max_length=100)
    site = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(_('ZIP code'), max_length=5)
    avatar = models.ImageField(default='user-profile.jpg')

    def __str__(self):
        return self.user.email

    @receiver(post_save, sender=CustomUser) #add this
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=CustomUser) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()