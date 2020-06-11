from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment
from django.views.generic import ListView, TemplateView
from taggit.models import Tag
from django.views.generic.edit import CreateView
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import get_template
from . forms import ContactForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method =='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request, 'detail.html', {'post':post, 'comments':comments, 'comment_form':comment_form})



def tag_detail(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request,'category.html', {'posts':posts, 'tag':tag})


class AboutView(TemplateView):
    template_name = "about.html"


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            user_email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            
            template = get_template('contact.txt') 
            context = {
				'name': name,
				'email': user_email,
				'message': message,
			}
            content = template.render(context)
            email = EmailMessage(
				"New contact form submission (DjanGrow)",
				content,
				user_email,
				[EMAIL_HOST_USER],
				headers = {'Reply-To': user_email},
				)
            email.send()
            request.session['mail_sent'] = True
            return redirect ('success')
    else:
        form = ContactForm()	
    return render(request, 'contact.html', {'form':form})


def success(request):
	if not request.session.pop('mail_sent', False):
		return redirect('home')
	else:
		return render(request, 'success.html')