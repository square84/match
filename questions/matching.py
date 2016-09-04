from django.contrib.auth import get_user_model

from .models import UserAnswer

User = get_user_model()

user = User.objects.all()
all_user_answer = UserAnswer.objects.all().order_by("user__id")


def get_match(usera, userb):
    user_a_answers = UserAnswer.objects.filter(user=usera)[0]
    user_b_answers = UserAnswer.objects.filter(user=userb)[0]

    if user_a_answers.question.id == user_b_answers.question.id:
        user_a_answer = user_a_answers.my_answer
        user_a_pref = user_a_answers.their_answer
        user_b_answer = user_b_answers.my_answer
        user_b_pref = user_b_answers.their_answer

        if user_a_answer == user_b_pref:
            print "%s fits with %s's preference" % (user_a_answers.user.username, user_b_answers.user.username)

        if user_a_pref == user_b_answer:
            print " %s fits with %s's preference" % (user_a_answers.user.username, user_b_answers.user.username)

        if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
            print "this is an ideal answer for both"
