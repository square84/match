from django.contrib.auth import get_user_model

from .models import UserAnswer

User = get_user_model()

user = User.objects.all()
all_user_answer = UserAnswer.objects.all().order_by("user__id")


def get_match(user_a, user_b):
    user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
    user_b_answers = UserAnswer.objects.filter(user=user_b)[0]

    if user_a_answers.question.id == user_b_answers.question.id:
        user_a_answer = user_a_answers.my_answer
        user_a_pref = user_a_answers.their_answer
        user_b_answer = user_b_answers.my_answer
        user_b_pref = user_b_answers.their_answer

        user_a_total_awared = 0
        user_b_total_awared = 0

        if user_a_answer == user_b_pref:
            user_b_total_awared += user_b_answers.their_points
            print "%s fits with %s's preference" % (user_a_answers.user.username, user_b_answers.user.username)

        if user_a_pref == user_b_answer:
            user_a_total_awared += user_a_answers.their_points
            print " %s fits with %s's preference" % (user_a_answers.user.username, user_b_answers.user.username)

        if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
            print "this is an ideal answer for both"


def get_points(user_a,user_b):
    a_answers = UserAnswer.objects.filter(user=user_a)[0]
    b_answers = UserAnswer.objects.filter(user=user_b)[0]
    a_total_awarded = 0
    a_points_possible = 0
    if a_answers.question.id == b_answers.question.id:
        a_pref = a_answers.their_answer
        b_answers = b_answers.my_answer
        if a_pref == b_answers:
            '''
            awards points for correct answer
            '''
            a_total_awarded += a_answers.their_points
        '''
        assiging total points
        '''
        a_points_possible += a_answers.their_points
    print "%s has awarded %s points of %s to %s" % (user_a,a_total_awarded,a_points_possible,user_b)