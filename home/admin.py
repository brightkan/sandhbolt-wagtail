from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from home.models import Slider


class SliderAdmin(ModelAdmin):
    model = Slider
    menu_label = "Sliders"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("sub_title", "title", "image")
    search_fields = "__all__"


modeladmin_register(SliderAdmin)
