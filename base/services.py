from jobhandler.models import JobCategory

def get_categories(n=8):
    cats = list(JobCategory.objects.all())
    cats.reverse()
    cats = cats[0:n]
    return cats