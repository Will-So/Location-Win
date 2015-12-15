from flask.ext.wtf import Form
from wtforms import (StringField, TextAreaField, BooleanField,
    SelectField, SubmitField)
from wtforms.validators import DataRequired


# TODO Make a list of cities and categories for each of the things.

categories = [('American (New)', 'American'), ('American (Traditional)', 'American (American Traditional)'),
              ('Arts & Entertainment', 'Arts & Entertainment'),
               ('Asian Fusion', 'Asian Fusion'), ('Bagels', 'Bagels'),
               ('Bakeries', 'Bakeries'), ('Barbeque', 'Barbeque'),
               ('Bars', 'Bars'), ('Breakfast & Brunch', 'Breakfast & Brunch'),
               ('British', 'British'), ('Buffets', 'Buffets'), ('Burgers', 'Burgers'),
               ('Cafes', 'Cafes'), ('Canadian (New)', 'Canadian (New)'),
               ('Caterers', 'Caterers'), ('Chicken Wings', 'Chicken Wings'),
               ('Chinese', 'Chinese'), ('Coffee & Tea', 'Coffee & Tea'),
               ('Delis', 'Delis'), ('Desserts', 'Desserts'), ('Diners', 'Diners'),
               ('Event Planning & Services', 'Event Planning & Services'),
               ('Fast Food', 'Fast Food'), ('Food', 'Food'), ('French', 'French'),
               ('Gastropubs', 'Gastropubs'), ('German', 'German'),
               ('Gluten-Free', 'Gluten-Free'), ('Greek', 'Greek'),
               ('Grocery', 'Grocery'), ('Hawaiian', 'Hawaiian'),
               ('Hot Dogs', 'Hot Dogs'), ('Ice Cream & Frozen Yogurt', 'Ice Cream & Frozen Yogurt'),
               ('Indian', 'Indian'), ('Italian', 'Italian'),
               ('Japanese', 'Japanese'), ('Juice Bars & Smoothies', 'Juice Bars & Smoothies'),
               ('Korean', 'Korean'), ('Latin American', 'Latin American'), ('Lounges', 'Lounges'),
               ('Mediterranean', 'Mediterranean'), ('Mexican', 'Mexican'),
               ('Middle Eastern', 'Middle Eastern'), ('Nightlife', 'Nightlife'),
               ('Pizza', 'Pizza'), ('Pubs', 'Pubs'), ('Restaurants', 'Restaurants'),
               ('Salad', 'Salad'), ('Sandwiches', 'Sandwiches'), ('Seafood', 'Seafood'),
               ('Southern', 'Southern'), ('Specialty Food', 'Specialty Food'),
               ('Sports Bars', 'Sports Bars'), ('Steakhouses', 'Steakhouses'),
               ('Sushi Bars', 'Sushi Bars'), ('Tex-Mex', 'Tex-Mex'), ('Thai', 'Thai'),
               ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Vietnamese', 'Vietnamese'),
               ('Wine Bars', 'Wine Bars')]

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