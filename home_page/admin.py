from django.contrib import admin

from .models import Customize_home_page,Customize_home_page_gallery_courses,Message_From_Alumni

from .models import Customize_study_with_section, myCarousel, Message_From_Principle

from .models import About_ETC

admin.site.register(Customize_home_page)
admin.site.register(Customize_home_page_gallery_courses)
admin.site.register(Customize_study_with_section)
admin.site.register(myCarousel)
admin.site.register(Message_From_Alumni)
admin.site.register(Message_From_Principle)
admin.site.register(About_ETC)


