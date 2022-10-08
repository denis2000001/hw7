from django.db import models
# Create your models here.

POST_TYPE_CHOICES = (
    (1, 'Animals'),
    (2, 'Cars'),
    (3, 'Recipes'),
    (4, 'Nature'),
    (5, 'Other')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    stars = models.IntegerField(null=True)
    type = models.IntegerField(choices=POST_TYPE_CHOICES, null=True)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.author