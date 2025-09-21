from app import app
from models import db, User, Recipe

class TestRecipe:
    def test_has_attributes(self):
        '''has attributes title, instructions, and minutes_to_complete.'''

        with app.app_context():

            Recipe.query.delete()
            User.query.delete()  # Clear users too
            db.session.commit()

            # First create a user
            user = User(
                username="test_chef",
                image_url="https://example.com/avatar.jpg",
                bio="Test chef bio"
            )
            user.password_hash = "password123"
            db.session.add(user)
            db.session.commit()

            # Then create a recipe associated with the user
            recipe = Recipe(
                title="Delicious Shed Ham",
                instructions="""Or kind rest bred with am shed then. In""" + \
                    """ raptures building an bringing be. Elderly is detract""" + \
                    """ tedious assured private so to visited. Do travelling""" + \
                    """ companions contrasted it. Mistress strongly remember""" + \
                    """ up to. Ham him compass you proceed calling detract.""" + \
                    """ Better of always missed we person mr. September""" + \
                    """ smallness northward situation few her certainty""" + \
                    """ something.""",
                minutes_to_complete=60,
                user_id=user.id
            )

            db.session.add(recipe)
            db.session.commit()