"""Flask public web catalogue for buyers.

Shows available listings, lets buyers search/filter, view a property's
detail page with its image and agent contact, and send an enquiry.
"""
import os

from flask import Flask, render_template, request, redirect, url_for, flash, send_file

import db

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'


@app.route('/')
def home():
    country = request.args.get('country', '').strip()
    state = request.args.get('state', '').strip()
    min_price = request.args.get('min_price', '').strip()
    max_price = request.args.get('max_price', '').strip()

    properties = db.search_properties(
        country=country or None,
        state=state or None,
        min_price=float(min_price) if min_price.replace('.', '', 1).isdigit() else None,
        max_price=float(max_price) if max_price.replace('.', '', 1).isdigit() else None,
    )

    return render_template('index.html', properties=properties, filters=request.args)


@app.route('/property/<property_id>')
def property_detail(property_id):
    property_ = db.get_property(property_id)
    if not property_:
        return "Property not found", 404
    image = db.get_image(property_id)
    agent = db.get_agent(property_.get('Agent_id'))
    return render_template('detail.html', property=property_, image=image, agent=agent)


@app.route('/property/<property_id>/image')
def property_image(property_id):
    image = db.get_image(property_id)
    if not image or not os.path.isfile(image['image_path']):
        return "Image not found", 404
    return send_file(image['image_path'])


@app.route('/property/<property_id>/enquire', methods=['POST'])
def submit_enquiry(property_id):
    property_ = db.get_property(property_id)
    if not property_:
        return "Property not found", 404

    buyer_name = request.form.get('buyer_name', '').strip()
    buyer_email = request.form.get('buyer_email', '').strip()
    message = request.form.get('message', '').strip()

    if not buyer_name or not buyer_email or '@' not in buyer_email:
        flash("Please provide a valid name and email address.")
        return redirect(url_for('property_detail', property_id=property_id))

    db.add_enquiry(property_id, buyer_name, buyer_email, message)
    flash("Your enquiry has been sent. The agent will contact you soon.")
    return redirect(url_for('property_detail', property_id=property_id))


if __name__ == '__main__':
    app.run(debug=True)
