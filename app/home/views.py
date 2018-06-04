# app/home/views.py

from flask import render_template, abort
from flask_login import login_required, current_user

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage templates on the / route
    """
    return render_template('home.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard templates on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('admin_dashboard.html', title="Dashboard")