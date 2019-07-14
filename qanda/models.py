from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.urls import reverse

# Create your models here.


class Question(models.Model):

    title = models.CharField(max_length=120)

    question = models.TextField()

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-created_at',)

    def can_accept_answer(self, user):

        return self.user == user

    def get_absolute_url(self):

        return reverse('qanda:question-detail', kwargs={'pk': self.pk})

    def __str__(self):

        return self.title

class Answer(models.Model):

    answer = models.TextField()

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)

    question = models.ForeignKey(to="Question", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    accepted = models.BooleanField(default=False)

    class Meta:

        ordering = ('-created_at', )

    def can_edit(self, user):

        return self.user is user

    def __str__(self):

        return self.answer
