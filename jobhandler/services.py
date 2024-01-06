

def categories_count_update(Job , JobCategory):
    cats = JobCategory.objects.all()

    for cat in cats:
        cat.count = len(list(Job.objects.filter(category = cat)))
        cat.save()