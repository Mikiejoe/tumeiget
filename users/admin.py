from django.contrib import admin


from .models import FoundId,User,Searching

admin.site.site_title = '2MEIGET'
admin.site.site_header = '2MEIGET ADMINISTRATION'
admin.site.register(FoundId)
admin.site.register(User)
admin.site.register(Searching)
