from decimal import Decimal
from django.contrib.auth import get_user_model

from .models import UserAnswer

User = get_user_model()

user = User.objects.all()
all_user_answer = UserAnswer.objects.all().order_by("user__id")


def get_points(user_a,user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)[0]
    b_answers = UserAnswer.objects.filter(user=user_b)[0]
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
            print "%s has awarded %s points of %s to %s" % (user_a,a_total_awarded,a_points_possible,user_b)
    percent = a_total_awarded / Decimal(a_points_possible)
    print percent
    if percent == 0:
        percent = 0.00001
    return percent,num_question


get_points(jmitchel3,khalessi)
a = get_points(khalessi,jmitchel3)
b = get_points(jmitchel3,khalessi)

match_percentage = "%.2f" %((Decimal(a[0])*Decimal(b[0])) ** (1/Decimal(b[1])))