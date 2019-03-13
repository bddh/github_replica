def make_replica(strategy, backend, user, response, *args, **kwargs):
    strategy.request.session['access_token'] = response['access_token']
