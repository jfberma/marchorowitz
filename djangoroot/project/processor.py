from project.models import PieceCategory


def view_id(request):
    path = request.path.replace('/', ' ').strip()
    path = path or 'index'
    return {'view_id': '-'.join(path.split())}


def categories(request):
    categories_list = PieceCategory.objects.all()
    return {'categories': categories_list}