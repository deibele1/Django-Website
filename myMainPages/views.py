from django.views.generic import TemplateView

from .models import MainPage


class MainView(TemplateView):
    template_name = "mainPage.html"
    model = MainPage

    def get_context_data(self, **kwargs):
        page = self.model.objects.get(name__iexact=kwargs["url"]) if 'url' in kwargs else self.model.objects.get(name="index")
        pages = self.model.objects.all()
        return {
            "title": page.title,
            "content": page.content,
            "side_content": page.side_content,
            "pages": pages,
        }
