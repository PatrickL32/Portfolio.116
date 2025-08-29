from django.shortcuts import render
from  .import models
from. forms import ContactForm
from django.core.mail import send_mail as send_email

# Create your views here.
def about_view(request):
    return render(request, 'your_app/about_me.html')

def about_me(request):
    return render(request, 'pages/about_me.html')

def experience(request):
    return render(request, 'pages/experience.html')

def projects_list(request):
    projects_list = models.Project.objects.all()
    context = {
        'projects_list': projects_list
    }
    return render(request, 'pages/projects_list.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the form data
            message_body = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}"
            )

            try:
                send_email(
                    "Email from PortFolio Website", #subject
                    message_body, # messag body the user typed
                    email, # from email: The user's Email
                    ['Jedi.92.lewis@gmail.com']
                )
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'pages/contact.html', {'form': form})
        else:
            print("Invalid Data")
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})