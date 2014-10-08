from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/blog/')
def blog():
    return render_template(
        'blog_index.html',
        title= 'Blog',
        )

@app.route('/blog/hello_world')
def contact():
    return render_template(
        'blog/hello_world.html',
        title='Hello, World!',
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/career')
def career():
    return render_template(
        'career_index.html',
        title = 'Index',
        )

@app.route('/career/overview')
def overview():
    return render_template(
        'career/overview.html',
        title = 'Overview'
        )


@app.route('/career/professional_skills/')
def professional_skills():
    return render_template(
        'career/professional_skills.html',
        title = 'Professional Skills',
        )

@app.route('/career/other_experience')
def other_experience():
    return render_template(
        'career/other_experience.html',
        title = 'Other Skills'
        )

@app.route('/career/formal_education')
def formal_education():
    return render_template(
        'career/formal_education.html',
        title = 'Formal Education',
        )

@app.route('/career/BenjaminMarkZichCV.pdf')
def BenjaminMarkZichCV():
    return render_template(
        'career/BenjaminMarkZichCV.html',
        title = 'Carriculum Vitae',
        )

@app.route('/code/')
def code():
    return render_template(
        'code_index.html',
        title = 'Index',
        )

@app.route('/code/personal_page/')
def personal_page():
    return render_template(
        'code/personal_page.html',
        title = 'Personal Webpage',
        )

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(410)
def page_gone(e):
    return render_template('errors/410.html'), 410

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500