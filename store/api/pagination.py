from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class Pagination(PageNumberPagination):
    page_size=20
    page_size_query_param='page'
    # page_query_param = 'page' # queryserch  kismini degistirebilirisn. default=page
class LimitPagi(LimitOffsetPagination):
    default_limit=20
