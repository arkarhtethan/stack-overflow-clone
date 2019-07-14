from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    TemplateView,
    FormView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from .models import (
    Answer,
    Question
)
from .forms import (
    AnswerForm,
    AskQuestionForm,
    AnswerAcceptanceForm,
    ContactForm,
)


class QuestionListView(ListView):

    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):

    form_class = AskQuestionForm

    template_name = "qanda/ask.html"

    def get_initial(self):

        return {
            "user": self.request.user.id
        }


class QuestionDetailView(DetailView):

    model = Question

    ACCEPT_FORM = AnswerAcceptanceForm(initial={"accepted": True})

    REJECT_FORM = AnswerAcceptanceForm(initial={"accepted": False})

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)

        ctx['solved'] = self.object.answer_set.filter(accepted=True).exists()

        ctx.update({
            'answer_form': AnswerForm(
                initial={
                    'user': self.request.user.pk,
                    'question': self.object.pk,
                }
            )
        })

        if self.object.can_accept_answer(self.request.user):

            ctx.update({
                'accept_form': self.ACCEPT_FORM,
                'reject_form': self.REJECT_FORM,
            })

        return ctx


class AnswerCreateView(LoginRequiredMixin, CreateView):

    form_class = AnswerForm

    def get_initial(self):

        return {
            "user": self.request.user.pk,
            "question": self.kwargs['pk'],
        }

    def get_success_url(self):

        pk = self.kwargs['pk']

        return self.get_question(pk).get_absolute_url()

    def get_question(self, pk):

        return Question.objects.get(pk=pk)


class AnswerUpdateView(UpdateView):

    form_class = AnswerForm

    queryset = Answer.objects.all()

    template_name = "qanda/answer_form.html"

    def get_success_url(self):
    
        return self.object.question.get_absolute_url()

class AnswerAcceptanceUpdate(LoginRequiredMixin, UpdateView):

    form_class = AnswerAcceptanceForm

    queryset = Answer.objects.all()

    def get_success_url(self):

        return self.object.question.get_absolute_url()

class AboutView(TemplateView):

    template_name = "qanda/about.html"

class ContactView(FormView):

    form_class = ContactForm

    template_name = "qanda/contact.html"

    def form_valid(self, form):

        self.send_email()

        return super().form_valid(form)

    def send_email(self):

        pass