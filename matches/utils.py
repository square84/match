from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db.models import Q
from questions.models import UserAnswer, Question


# User = get_user_model()
#
# user = User.objects.all()
# all_user_answer = UserAnswer.objects.all().order_by("user__id")

def get_points2(user_a, user_b):
    q1 = Q(useranswer__user=user_a)
    q2 = Q(useranswer__user=user_b)
    question_set = Question.objects.filter(q1 | q2).distinct()
    for question in question_set:
        try:
            a_answer = UserAnswer.objects.get(user=user_a, question=question)
        except:
            a_answer = None
        try:
            b_answer = UserAnswer.objects.get(user=user_b, question=question)
        except:
            b_answer = None

        if a_answer and b_answer:
            print("Something")


def get_points(user_a, user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)
    b_answers = UserAnswer.objects.filter(user=user_b)
    a_total_awarded = 0
    a_points_possible = 0
    num_question = 0
    for a in a_answers:
        for b in b_answers:
            if a.question.id == b.question.id:
                num_question += 1
                a_pref = a.their_answer
                b_answer = b.my_answer
                if a_pref == b_answer:
                    '''
                    awards points for correct answer
                    '''
                    a_total_awarded += a_answers.their_points
                '''
                assiging total points
                '''
                a_points_possible += a.their_points
            print "%s has awarded %s points of %s to %s" % (user_a, a_total_awarded, a_points_possible, user_b)
    percent = a_total_awarded / Decimal(a_points_possible)
    print percent
    if percent == 0:
        percent = 0.00001
    return percent, num_question


# get_points(jmitchel3,khalessi)
# a = get_points(khalessi,jmitchel3)
# b = get_points(jmitchel3,khalessi)
#
# match_percentage = "%.2f" %((Decimal(a[0])*Decimal(b[0])) ** (1/Decimal(b[1])))


def get_match(user_a, user_b):
    a = get_points(user_a, user_b)
    b = get_points(user_b, user_a)
    # a[0] = decimal match value
    # b[1] = number of question answered
    number_of_questions = b[1]
    match_decimal = (Decimal(a[0]) * Decimal(b[0])) ** (1 / Decimal(number_of_questions))
    return match_decimal, number_of_questions
