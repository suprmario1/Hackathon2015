from django.contrib import admin

# Register your models here.
from blog.models import Post

admin.site.register(Post)
admin.site.register(Address)
admin.site.register(DIYUser)
admin.site.register(ItemService)
admin.site.register(Offer)
