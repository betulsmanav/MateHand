from rest_framework.pagination import PageNumberPagination
class Pagination(PageNumberPagination):
    page_size=20
    # page_query_param = 'page' # queryserch  kismini degistirebilirisn. default=page
