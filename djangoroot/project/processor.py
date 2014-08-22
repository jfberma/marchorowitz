

def view_id(request):
    path = request.path.replace('/', ' ').strip()
    path = path or 'index'
    return {'view_id': '-'.join(path.split())}