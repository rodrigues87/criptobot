from django.apps import AppConfig




class HistoricoConfig(AppConfig):
    name = 'historico'

    def ready(self):
        from historico import updater
        updater.start()
