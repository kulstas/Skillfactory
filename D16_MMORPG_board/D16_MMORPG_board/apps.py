from django.apps import AppConfig


class D16_MMORPG_boardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "D16_MMORPG_board"

    def ready(self):
        from D16_MMORPG_board import signals