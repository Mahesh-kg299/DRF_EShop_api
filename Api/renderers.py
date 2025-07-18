from rest_framework.renderers import JSONRenderer

class PrettyJSONRenderer(JSONRenderer):
    def get_indent(self, *args, **kwargs):
        return 4