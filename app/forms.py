from flask.ext.wtf import Form
from wtforms import (StringField, TextAreaField, BooleanField,
    SelectField, SubmitField)
from wtforms.validators import DataRequired


# TODO Make a list of cities and categories for each of the things.

categories = [('ameri', 'American'), ('arts', 'Arts & Entertainment'),
              ('asian', 'Asian Fusion'), ('bagel', 'Bagels'), ('baker', 'Bakeries'),
              ('barbe', 'Barbeque'), ('bars', 'Bars'), ('break', 'Breakfast & Brunch'),
              ('briti', 'British'), ('buffe', 'Buffets'), ('burge', 'Burgers'), ('cafes', 'Cafes'),
              ('canad', 'Canadian (New)'), ('cater', 'Caterers'), ('chick', 'Chicken Wings'),
              ('chine', 'Chinese'), ('coffe', 'Coffee & Tea'), ('delis', 'Delis'),
              ('desse', 'Desserts'), ('diner', 'Diners'), ('event', 'Event Planning & Services'),
              ('fast', 'Fast Food'), ('food', 'Food'), ('frenc', 'French'), ('gastr', 'Gastropubs'),
              ('germa', 'German'), ('glute', 'Gluten-Free'), ('greek', 'Greek'), ('groce', 'Grocery'),
              ('hawai', 'Hawaiian'), ('hot d', 'Hot Dogs'), ('ice c', 'Ice Cream & Frozen Yogurt'),
              ('india', 'Indian'), ('itali', 'Italian'), ('japan', 'Japanese'),
              ('juice', 'Juice Bars & Smoothies'), ('korea', 'Korean'),
              ('latin', 'Latin American'), ('loung', 'Lounges'), ('medit', 'Mediterranean'),
              ('mexic', 'Mexican'), ('middl', 'Middle Eastern'), ('night', 'Nightlife'),
              ('pizza', 'Pizza'), ('pubs', 'Pubs'), ('resta', 'Restaurants'), ('salad', 'Salad'),
              ('sandw', 'Sandwiches'), ('seafo', 'Seafood'), ('south', 'Southern'),
              ('speci', 'Specialty Food'), ('sport', 'Sports Bars'), ('steak', 'Steakhouses'),
              ('sushi', 'Sushi Bars'), ('tex-m', 'Tex-Mex'), ('thai', 'Thai'), ('vegan', 'Vegan'),
              ('veget', 'Vegetarian'), ('vietn', 'Vietnamese'), ('wine', 'Wine Bars')]

secondary_categories = [('na', 'Nothing')] + categories

cities = [([36.1662859, -115.149225], 'Las Vegas'), ([33.4467681, -112.0756724], 'Phoenix'), ([35.2270869, -80.8431268], 'Charlotte'),
           ([40.4416941, -79.9900861], 'Pittsburgh'), ([45.5115944, -73.6051013], 'Montréal'), ([33.5091215, -111.8992365], 'Scottsdale'),
           ([55.9483544, -3.1931187], 'Edinburgh'), ([33.436188, -111.586066076293], 'Mesa'), ([45.5115944, -73.6051013], 'Montreal'),
          ([33.4144139, -111.9094473], 'Tempe')]


class BusinessForm(Form):
    city = SelectField('What city would you like to start your business in?', validators=[DataRequired()],
                       choices=cities)
    business = SelectField("What Business would you like to start?", validators=[DataRequired()],
                           choices=categories)
    additional_category = SelectField("What else would you like your business to have?",
                                      choices=secondary_categories)
    more_details = SubmitField("Calculate")