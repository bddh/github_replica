import requests
import json
from django.shortcuts import render

from core.settings import GITHUB_REPOS_API_URL, APP_OWNER, APP_REPO


def index(request):
    return render(request, 'app/index.html')


def complete(request):
    complete = False
    url = None
    headers = {'Authorization': 'token {0}'.format(
        request.session['access_token'])}
    result = requests.post(
        '{0}/{1}/{2}/forks'.format(
            GITHUB_REPOS_API_URL, APP_OWNER, APP_REPO), headers=headers)
    if result.ok:
        complete = True
        deserialized = json.loads(result.content.decode())
        url = deserialized['html_url']

    return render(
        request, 'app/index.html', {'complete': complete, 'url': url})
