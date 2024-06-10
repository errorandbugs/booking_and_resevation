from flask import Blueprint, render_template, request

feedback_blueprint = Blueprint('feedback', __name__, url_prefix='/feedback')

@feedback_blueprint.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        # Process the feedback here (store, send email, etc.)
        return render_template('feedback_sent.html')  # Replace with your template name
    return render_template('feedback.html')  # Replace with your template name
