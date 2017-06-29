from django.shortcuts import render
from mywebsite.models import Introductions


def index(request):
    """
    Introductions.objects.first().first -> Gives me objects attribute "first" value
    Introductions.objects.all() -> The best solution, it gives me back queryset, which I can iterate through in template
        For example:
            queryset.0.first -> getting the text of first queryset's first entry
        OR if there are many querysets and there is a need to iterate through all of them:
            {% for entry in queryset %}
                <tr class="{% cycle 'row1' 'row2' %}">
                    <p>{{ entry.first }}</p>
                    <p>{{ entry.second }}</p>
                    <p>{{ entry.third }}</p>
                </tr>
            {% endfor %}
    
    :param request: 
    :return: 
    """

    context = {}
    first_field = Introductions.objects.first().first
    all_entries = Introductions.objects.all()
    introduction_queryset = Introductions.objects.all()  # The best solution
    introductions_list = []

    for entry in all_entries:
        first_intro = entry.first
        second_intro = entry.second
        third_intro = entry.third
        introductions_list.extend([first_intro, second_intro, third_intro])

    context.update({'first_introduction': first_field, 'introductions_list': introductions_list, 'queryset': introduction_queryset})

    return render(request, 'mywebsite/index.html', context)


def about(request):
    return render(request, 'mywebsite/about.html')


def services(request):
    return render(request, 'mywebsite/services.html')


def contact(request):
    return render(request, 'mywebsite/contact.html')


def portfolio_first(request):
    return render(request, 'mywebsite/portfolio-1-col.html')


def portfolio_second(request):
    return render(request, 'mywebsite/portfolio-2-col.html')


def portfolio_third(request):
    return render(request, 'mywebsite/portfolio-3-col.html')


def portfolio_fourth(request):
    return render(request, 'mywebsite/portfolio-4-col.html')


def faq(request):
    return render(request, 'mywebsite/faq.html')


def pricing(request):
    return render(request, 'mywebsite/pricing.html')

