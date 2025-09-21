from app import app
from models import db, User, Recipe

def seed_database():
    with app.app_context():
        print("🗑️ Clearing existing data...")
        # Clear existing data in the right order to avoid foreign key constraints
        Recipe.query.delete()
        User.query.delete()
        db.session.commit()

        print("👥 Creating users...")
        # Create users
        user1 = User(
            username="chef_john",
            image_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
            bio="Professional chef with 10 years of experience. Love cooking Italian cuisine!"
        )
        user1.password_hash = "password123"

        user2 = User(
            username="baking_betty",
            image_url="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&h=150&fit=crop&crop=face",
            bio="Home baker passionate about desserts and pastries. Always experimenting with new recipes!"
        )
        user2.password_hash = "password123"

        # Add users to session
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        print("🍳 Creating recipes...")
        # Create recipes
        recipe1 = Recipe(
            title="Classic Spaghetti Carbonara",
            instructions="1. Cook spaghetti according to package directions. 2. In a bowl, whisk together eggs and grated cheese. 3. Cook pancetta until crispy. 4. Combine hot pasta with pancetta, then mix in egg mixture quickly to create a creamy sauce. 5. Season with black pepper and serve immediately.",
            minutes_to_complete=25,
            user_id=user1.id
        )

        recipe2 = Recipe(
            title="Chocolate Chip Cookies",
            instructions="1. Cream together butter and sugars. 2. Beat in eggs and vanilla. 3. Mix in flour, baking soda, and salt. 4. Fold in chocolate chips. 5. Drop onto baking sheets and bake at 350°F for 10-12 minutes until golden brown. Let cool before serving.",
            minutes_to_complete=45,
            user_id=user2.id
        )

        recipe3 = Recipe(
            title="Vegetable Stir Fry",
            instructions="1. Heat oil in a wok or large pan. 2. Add minced garlic and ginger, cook until fragrant. 3. Add chopped vegetables and stir fry until crisp-tender. 4. Add soy sauce and sesame oil. 5. Serve over rice or noodles for a complete meal.",
            minutes_to_complete=20,
            user_id=user1.id
        )

        # Add recipes to session
        db.session.add(recipe1)
        db.session.add(recipe2)
        db.session.add(recipe3)
        db.session.commit()

        print("✅ Database seeded successfully!")
        print(f"Created {User.query.count()} users and {Recipe.query.count()} recipes")

if __name__ == "__main__":
    seed_database()