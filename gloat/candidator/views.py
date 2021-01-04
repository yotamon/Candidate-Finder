from django.shortcuts import render

from .models import Skill, Job, Candidate
from operator import itemgetter
from itertools import chain

# Views #
# Home Page View
def index(request):
    candidates_list = Candidate.objects.all()
    jobs_list = Job.objects.all()
    context = {'candidates_list': candidates_list, 'jobs_list': jobs_list}
    return render(request, 'candidator/index.html', context)

# Results Page View
def results(request):
    try:
        candidates = getMatchedCandidates(request.POST['job'])
    except Candidate.DoesNotExist:
        raise Http404("Candidate does not exist")
    return render(request, 'candidator/results.html', { 'candidates': candidates })


# Functions #
# Get Matched Candidates for a specific job
def getMatchedCandidates(job_id):
    # Set a list of matches queries
    match_sets = []

    # Set a match counting array
    matchesArray = list(Candidate.objects.values('id'))
    for field in matchesArray:
        field['match_points'] = 0;

    # Match by skill query
    selected_job = Job.objects.get(pk=job_id)
    # Add match-query of skill matches to match_sets query list
    match_sets.append(Candidate.objects.filter(skills__id=selected_job.skill.id))

    # Match by title words (make query for every word in title)
    job_title_words = selected_job.title.split()
    for word in job_title_words:
        # Add match-query of current word matches to match_sets query list
        match_sets.append(Candidate.objects.filter(title__icontains=word))

    # Count all matches
    for match_set in match_sets:
        for match in match_set:
            matchesArray[match.id - 1]['match_points'] += 1
    
    # Sort array by match match_points
    matchesArray = sorted(matchesArray, key=itemgetter('match_points'), reverse=True)

    # Create a new sorted candidates query
    allCan = Candidate.objects.all()
    result = Candidate.objects.none()
    i = 0
    while matchesArray[i]['match_points'] > 0:
        result = list(chain(result, allCan.filter(pk=matchesArray[i]['id'])))
        i += 1 

    return result