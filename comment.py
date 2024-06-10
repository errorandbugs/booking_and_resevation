from flask import Blueprint, render_template, request
from model import db ,Items,User


'''@comments_blueprint.route('/')
def index():
  # Get all comments from the database
  comments = db.session.query(Comment).filter_by(Item_id=item_id).all()
  return render_template('comments/index.html', comments=comments)

@comments_blueprint.route('/add_comment', methods=['POST'])
def add_comment():
  # ... (similar logic to process and add comment)
  return 'Comment added successfully!'

@app.route('/feedback')
  def show_feedback_form():
       return render_template('feedback_form.html')
   @app.route('/submit_feedback', methods=['POST'])
   def submit_feedback():
       name = request.form['name']
       email = request.form['email']
       feedback = request.form['feedback']
       # Save the feedback to a database or file
       # You can also send the feedback via email or store it in a data structure
       return "Thank you for your feedback, {}!".format(name)'''