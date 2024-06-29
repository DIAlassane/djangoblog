from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Document
import openai
import os

# Chargement de la clé API OpenAI depuis les variables d'environnement
openai.api_key = os.getenv('AI_KEY')

def switch_to_french(request):
    activate('fr')
    return redirect('/')

def switch_to_english(request):
    activate('en')
    return redirect('/')

@csrf_exempt
def ExtendedFront(request):
    posts = Post.objects.all()
    response_text = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # modèle d'IA openAI
            messages=[
                {"role": "system", "content": "You are a master poet. Craft beautiful, emotive, and lyrical poems on any topic."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.5
        )

        response_text = (response.choices[0].message.content)

    return render(request, 'main/ExtendedFront.html', {'posts': posts, 'response': response_text})

def search_documents(query):
    documents = Document.objects.all()
    results = []
    for doc in documents:
        if query.lower() in doc.content.lower():
            results.append(doc)
    return results
