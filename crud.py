from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from model import db, User, Items


crud_blueprint = Blueprint('items', __name__, url_prefix='/items')
@crud_blueprint.route('/', methods=['GET'])
@login_required
def list_items():
    items = Items.query.all()
    return render_template('items.html', items=items)


@crud_blueprint.route('/create', methods=['POST'])
@login_required
def create_item():
    name = request.form('name')
    description = request.form('descripton')
    new_item = Items (name = name, description = description)
    db.session.add(new_item)
    db.session.commit()
    flash('u dey whine?' , 'error')
    return redirect(url_for(Items.list_items))


@crud_blueprint.route("/update/<int:item_id>" , methods=['POST'])
@login_required
def update (item_id):
    item = Items.query.get_or_404(item_id)
    if request.methods =='post':
        item.name = request.form ["name"]
        item.desc = request.form ["description"]
        db.session.commit()
        flash("item updated" , "success")
        return redirect(url_for(item.list_items))
    return render_template ("edit'html" , "items = item")


@crud_blueprint.route('/update/<int:item_id>' , methods=['POST'])
@login_required
def delete (item_id):
    item = Items.query.get_or_404(item_id)
    if request.methods =='post':
        db.session.delete(item)
        db.session.commit()
        flash ("item updated" , "success")
        return redirect(url_for(Items.list_items))
    return render_template ("edit'html" , "items = item")