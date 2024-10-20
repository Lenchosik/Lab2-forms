from django import forms
class UserForm(forms.Form):
    name = forms.CharField(label= "Имя клиента", max_length=30, help_text="ФИО")
    age = forms.IntegerField(label= "Возраст клиента")
    adoyou = forms.NullBooleanField(label="Вы пользуетесь наземным транспортом?")
    bdoyou = forms.NullBooleanField(label="Вы довольны качеством наземного транспорта?")
    email = forms.EmailField(label="Ваш электронный адрес")
    сdoyou = forms.NullBooleanField(label="Пользуетесь ли вы сайтом по поиску билетов?")
    url_text = forms.URLField(label="Пожалуйста, введите ссылку на сайт")
    file = forms.FileField(label="Прикрепите ваше фото(3x4)", required=False)
    file_path = forms.FilePathField(label="Прикрепите ещё одно фото", path="D:\Pictures", required=False)
    regex = forms.RegexField(label="Введите ваш номер телефона", regex=r'^[0-9]*$', help_text="Только цифры (не используйте +7)", required=False)

    bus_choices = (
        ("1", "7"),
        ("1", "9"),
        ("1", "85"),
        ("1", "3"),
        ("1", "93"),
        ("1", "67"),
        ("1", "82"),
    )
    choice = forms.ChoiceField(choices=bus_choices, label="Каким из маршрутов чаще пользуетесь?")