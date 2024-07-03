from django.db import models
from django.db import models  # Импорт модуля models из библиотеки Django для работы с базой данных.
from django.contrib.auth.models import User  # Импорт модели пользователя Django для аутентификации.
from books.models import artic  # Импорт модели игры из приложения b4cklog.
from PIL import Image  # Импорт модуля Image из библиотеки Pillow для работы с изображениями.


# Модель профиля пользователя.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь "один к одному" с моделью User.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # Изображение профиля пользователя.
    # книги, которые пользователь хочет прочитать.
    want_to_read = models.ManyToManyField(artic, related_name='want_to_read', blank=True)
    # книги, которые пользователь в настоящее время читает.
    reading = models.ManyToManyField(artic, related_name='reading', blank=True)
    # книги, которые пользователь читал, но бросил.
    reaed = models.ManyToManyField(artic, related_name='reaed', blank=True)
    # книги, которые пользователь завершил.
    completed = models.ManyToManyField(artic, related_name='completed', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'  # Возвращает строковое представление объекта - профиль пользователя.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Сохранение профиля пользователя.

        img = Image.open(self.image.path)  # Открытие изображения профиля.

        if img.height > 300 or img.width > 300:  # Если размер изображения больше 300x300.
            output_size = (300, 300)
            img.thumbnail(output_size)  # Создание превью изображения.
            img.save(self.image.path)  # Сохранение изменений.

    def get_category(self, category):
        if category == 'want_to_read':
            return self.want_to_read.all()  # Получение списка игр, которые пользователь хочет поиграть.
        elif category == 'reading':
            return self.reading.all()  # Получение списка игр, которые пользователь в настоящее время играет.
        elif category == 'reaed':
            return self.reaed.all()  # Получение списка игр, которые пользователь уже играл.
        elif category == 'completed':
            return self.completed.all()  # Получение списка игр, которые пользователь завершил.
        else:
            return None  # Если указана некорректная категория, возвращается None.