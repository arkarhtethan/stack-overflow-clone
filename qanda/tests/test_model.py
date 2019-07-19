from django.test import TestCase
from qanda.models import Answer, Question
from model_mommy import mommy
from django.urls import reverse


class TestQuestionModel(TestCase):

    def setUp(self):

        self.model = mommy.make("Question")

    def test_instance(self):

        self.assertTrue(isinstance(self.model, Question))

    def test_detail_url(self):

        detail_url = reverse('qanda:question-detail', kwargs={
            "pk": self.model.pk
        })

        self.assertEqual(self.model.get_absolute_url(), detail_url)

    def test_can_accept_answer(self):

        user = mommy.make("User")

        self.assertFalse(self.model.can_accept_answer(user))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.title)

class TestAnswerModel(TestCase):
    
    def setUp(self):

        self.model = mommy.make("Answer")

    def test_instance(self):

        self.assertTrue(isinstance(self.model, Answer))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.answer)
