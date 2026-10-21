from .models import Visitor


class VisitorMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.path.startswith('/admin/'):

            ip = request.META.get('REMOTE_ADDR')

            if ip:
                visitor, created = Visitor.objects.get_or_create(
                    ip_address=ip
                )

                if not created:
                    visitor.visits += 1
                    visitor.save(
                        update_fields=['visits', 'last_seen']
                    )

        response = self.get_response(request)

        return response