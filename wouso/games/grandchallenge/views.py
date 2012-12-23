from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import  GrandChallengeGame, GrandChallengeUser, GrandChallenge
from wouso.interface import render_string

@login_required
def index(request):
    """ Shows all rounds played by the current user """
    profile = request.user.get_profile()
    gc_user = profile.get_extension(GrandChallengeUser)

    gchalls = sorted(GrandChallenge.get_challenges(), key=lambda gc:gc.branch)
    #played = GrandChallengeGame.get_played(gc_user)
    users = sorted(GrandChallengeGame.allUsers, key=lambda u: u.user)
    over = 0
    done = GrandChallenge.all_done()
    #if not gc_user in GrandChallengeGame.ALL:
    #    return do_result(request, error='Ne pare rau, nu participi in turneu ')

    return render_to_response('grandchallenge/index.html',
            {'gchalls': gchalls,
             'nr': GrandChallengeGame.round_number - 1,
             'done': done,
             'users': users,
             'over': over,
             'gcuser': gc_user},
            context_instance=RequestContext(request))

@login_required
def do_result(request, error='', message=''):
    return render_to_response('grandchallenge/message.html',
        {'error': error, 'message': message},
        context_instance=RequestContext(request))

def sidebar_widget(request):
    gc = GrandChallengeGame
    active = GrandChallengeGame.get_active()
    gc_user = request.user.get_profile().get_extension(GrandChallengeUser)
    return render_string('grandchallenge/sidebar.html', {'gchall': gc, 'active': active, 'gcuser': gc_user})
