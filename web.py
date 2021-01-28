import pigwig
from pigwig import Response

def root(request):
    return Response('hello, world!')

routes = [
    ('GET', '/', root),
]

app = pigwig.PigWig(routes)
