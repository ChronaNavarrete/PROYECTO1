from django.db import models
from django.contrib.auth.models import AbstractUser , User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify
# Create your models here.

class User(AbstractUser):
    pass
    #name = models.CharField(max_length=200)
    #email = models.EmailField()
    #password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,unique=True)
    #title = models.CharField(max_length=100)
    #content = models.TextField()  # importar el otro field
    #imagen = models.URLField()
    #publish_date = models.DateTimeField(auto_now_add=True)
    #last_update = models.DateTimeField(auto_now = True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField()
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    def get_like_url(self):
        return reverse("like", kwargs={
            'slug': self.slug
        })

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_dislike_count(self):
        return self.dislike_set.all().count()

    
#funcion creacion automatica posts de cabildos

def CreacionAutomaticaCabildo():
    pass


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
