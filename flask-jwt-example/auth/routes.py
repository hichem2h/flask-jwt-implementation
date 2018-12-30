from . import bp
from .views import LoginView, FreshLoginView, RefreshView


bp.url_prefix = '/auth'

bp.add_url_rule('/login', view_func=LoginView.as_view('login'))
bp.add_url_rule('/fresh-login', view_func=FreshLoginView.as_view('fresh_login'))
bp.add_url_rule('/refresh', view_func=RefreshView.as_view('fresh_view'))
