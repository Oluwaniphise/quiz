from django.shortcuts import render, redirect
from .models import Question, Choice, Score
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


# def home(request):
#     questions = Question.objects.all().order_by('id')
#     paginator = Paginator(questions, 1)
#     page_num = request.GET.get('page', 1)
#     try:
#         page_obj = paginator.page(page_num)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.page_num)

#     page_obj = paginator.page(page_num)
#         #find a way to get the question from the page_obj

#     score=0
#     users_choices = []
#     try:
#         question = page_obj.object_list.get()
#         user_choice = question.choice_set.get(pk=request.POST['choice'])
#         # save_user_choice = Choice(question=question, choice_text=user_choice)
#         #find a way to store the user's choices and then mark
#         for question in questions:
#             if user_choice.answer == True:
#                 print("Very good")
#                 score += 1
#             else:
#                 print("uh uh")
#                 score += 0
#             # print(score)
#             # print([question_array])
        
#         users_choices.append(user_choice)
#         print(users_choices)
       

#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'index.html', {
            
#             'questions':page_obj, 'paginator':paginator,
#             'error_message': "Try selecting an option", 'page_num':int(page_num)
#         })
    


        


    # context = {
    #     'questions':questions,
    #     # 'page_num':page_num,
    #     # 'paginator':paginator
   
    # }
    # return render(request, 'index.html', context)



def home(request):
    questions = Question.objects.all().order_by('id')
    paginator = Paginator(questions, 1)
    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.page_num)

    page_obj = paginator.page(page_num)
        #find a way to get the question from the page_obj

   
    try:
        question = page_obj.object_list.get()
        user_choice = question.choice_set.get(pk=request.POST['choice'])
        # save_user_choice = Choice(question=question, choice_text=user_choice)
        #find a way to store the user's choices and then mark
        # for question in questions:
        if user_choice.answer == True:
            print("Very good")
                # score += 1
        else:
            print("uh uh")
                # score += 0
            # print(score)
          
       

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'index.html', {
            
            'questions':page_obj, 'paginator':paginator,
            'error_message': "Try selecting an option", 'page_num':int(page_num)
        })
    


        


    context = {
        'questions':questions,
        'page_num':page_num,
        'paginator':paginator           
   
    }
    return render(request, 'index.html', context)

    





