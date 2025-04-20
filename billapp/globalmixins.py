class ModelNameContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelname'] = self.model.__name__
        return context
