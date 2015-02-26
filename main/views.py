from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

from main.models import Link
from main.models import Tag
# Create your views here.

def index(request):
    context = RequestContext(request)

    links = Link.objects.all()
    return render_to_response('main/tags.html', {'links':links}, context)

def tags(request):
    context = RequestContext(request)
    tags = Tag.objects.all()
    # tags = Tag.objects.values_list('name').distinct()
    return render_to_response('main/tags.html', {'tags': tags}, context)

def tag(request, tag_name):
    context = RequestContext(request)
    the_tag = Tag.objects.get(name=tag_name)
    links = the_tag.link_set.all()
    return render_to_response('main/index.html', {'links': links, 'tag_name': '#' + tag_name}, context)

def add_link(request):
    import pdb; pdb.set_trace()
    context = RequestContext(request)
    if request.method == 'POST':
        url = request.POST.get("url", "")
        tags = request.POST.get("tags", "")
        title = request.POST.get("title", "")

        # create the link object
        link = Link.objects.create(title=title, url=url)
        link.save()

        # add tags
        tags = tags.split()
        # remove duplicates
        tags = list(set(tags))
        for tag in tags:
            new_tag = Tag(name=tag)
            new_tag.save()
            link.tags.add(new_tag)
    return redirect(index)