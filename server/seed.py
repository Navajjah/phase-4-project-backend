from app import db, app
from models import Book, Review, User

def seed_data():
    user1 = User(username='Harry Potter')
    user2 = User(username='Hermione Granger')
    user3 = User(username='Ron Weasley')
    user4 = User(username='Draco Malfoy')
    user5 = User(username='Nevile Longbottom')

    book1 = Book(
        title='The Monster Book of Monsters',
        rarity='Rare',
        spell_type='None',
        author='Edwardus Lima',
        hogwarts_class='Care of Magical Creatures by Rudeus Hagrid'
    )
    book2 = Book(
        title='Fantastic Beasts and Where to Find Them',
        rarity='Common',
        spell_type='Magizoology',
        author='Newt Scamander',
        hogwarts_class='Care of Magical Creatures by Rudeus Hagrid'
    )
    book3 = Book(
        title='One Thousand Magical Herbs and Fungi',
        rarity='Common',
        spell_type='None',
        author='Phyllida Spore',
        hogwarts_class='Herbology by Pomona Sprout'
    )
    book4 = Book(
        title='Advanced Potion-Making',
        rarity='Rare',
        spell_type='Potions',
        author='Libatius Borage',
        hogwarts_class='Potions by Severus Snape'
    )
    book5 = Book(
        title='Dark Arts Defence: Basics for Beginners',
        rarity='Common',
        spell_type='Defence',
        author='Unknown',
        hogwarts_class='Defence Against the Dark Arts by Quirinus Quirrell'
    )

    review1 = Review(
        content = 'To all would-be owners take care to stroke the spine of the book, or else the book might bite you',
        rating = 3,
        book_id = 1,
        user_id = 1
    )
    review2 = Review(
        content = 'A must-have for any aspiring magizoologist',
        rating = 5,
        book_id = 2,
        user_id = 2
    )
    review3 = Review(
        content = 'Good for plants, not so much for fungi, if you\'re into that sort of thing',
        rating = 4,
        book_id = 3,
        user_id = 3
    )
    review4 = Review(
        content = 'Precision, power, and perfection, though it would be as good as a wate on the likes of you',
        rating = 5,
        book_id = 4,
        user_id = 4
    )
    review5 = Review(
        content = 'Good book, if only I remembered to bring it to class',
        rating = 3,
        book_id = 1,
        user_id = 1
    )

    user1.favorites.append(book1)
    user1.favorites.append(book2)
    user2.favorites.append(book3)
    user2.favorites.append(book4)
    user3.favorites.append(book1)
    user4.favorites.append(book4)
    user5.favorites.append(book5)
    

    db.session.add_all([user1, user2, user3, user4, user5, book1, book2, book3, book4, book5, review1, review2, review3, review4, review5])
    db.session.commit()
    print('Data seeded successfully')

if __name__ == '__main__':
    with app.app_context():
        seed_data()