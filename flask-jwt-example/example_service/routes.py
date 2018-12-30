from . import bp
from .views import protected, partially_protected, critical


bp.url_prefix = '/example'

bp.add_url_rule('/protected', view_func=protected, methods=['GET'])
bp.add_url_rule('/partially-protected', view_func=partially_protected,
                methods=['GET'])
bp.add_url_rule('/critical', view_func=critical, methods=['GET'])
