from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import QuizForm
import json

def quiz_view(request, question_index=0):
    # Carregar as perguntas do arquivo JSON
    with open('questions.json', 'r') as file:
        data = json.load(file)

    # Pegar as questões
    concepts = data[0]['concepts']

    # Garantir que o índice da pergunta não excede o número de questões
    if question_index >= len(concepts):
        return redirect('quiz_results')

    question = concepts[question_index]
    form = QuizForm([question], request.POST or None)

    # Variáveis para feedback sobre a resposta
    is_answered = False
    correct = False
    user_answer = None

    if request.method == 'POST':
        if form.is_valid():
            user_answer = form.cleaned_data['question_0']
            is_answered = True
            correct = user_answer == question['correct_text']

            # Salvar a resposta na sessão
            request.session.setdefault('answers', []).append({
                'question': question['question'],
                'user_answer': user_answer,
                'correct_answer': question['correct_text'],
                'correct': correct,
            })

            # Gravar a posição onde o usuário parou
            request.session['current_question_index'] = question_index + 1

            # Não redirecionar imediatamente, apenas renderizar a mesma página para mostrar o feedback
            context = {
                'form': form,
                'question_index': question_index + 1,
                'total': len(concepts),
                'current_question': question,  # Passar a pergunta atual
                'is_answered': is_answered,
                'correct': correct,
                'user_answer': user_answer,
            }
            return render(request, 'quiz/quiz.html', context)

    # Passar o índice incrementado para o template
    context = {
        'form': form,
        'question_index': question_index,
        'total': len(concepts),
        'current_question': question,  # Passar a pergunta atual
        'is_answered': is_answered,
        'correct': correct,
        'user_answer': user_answer,
    }

    return render(request, 'quiz/quiz.html', context)

def quiz_results_view(request):
    # Recuperar as respostas da sessão
    answers = request.session.get('answers', [])
    score = sum(1 for ans in answers if ans['correct'])

    # Renderizar os resultados
    return render(request, 'quiz/results.html', {
        'score': score,
        'total': len(answers),
        'results': answers,
    })

def reset_quiz(request):
    # Limpar as respostas e o índice da pergunta atual
    request.session['answers'] = []
    request.session['current_question_index'] = 0
    return redirect('quiz')  # Redireciona para a primeira pergunta