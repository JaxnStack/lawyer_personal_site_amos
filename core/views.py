from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Basic Pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def practice(request):
    return render(request, 'practice.html')

def blog(request):
    return render(request, 'blog.html')

# Contact Page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Send email notification
            send_mail(
                subject=f"New Contact Form Submission from {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Show message and redirect
            messages.success(request, "Thank you for your message. We’ll be in touch shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})

# Optional: Success page (if needed separately)
def success_view(request):
    return render(request, 'success.html')
