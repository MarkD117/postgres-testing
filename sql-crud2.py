# Creating a new database entry for favourite games

from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Games(base):
    __tablename__ = "Favourite Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_year = Column(Integer)
    console_played_on = Column(String)
    rating_out_of_10 = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Games table
black_ops_2 = Games(
    name="Black Ops 2",
    release_year=2012,
    console_played_on="Xbox 360",
    rating_out_of_10=10
)

overwatch = Games(
    name="Overwatch",
    release_year=2016,
    console_played_on="Xbox/PC",
    rating_out_of_10=9
)

halo = Games(
    name="Halo 4",
    release_year=2012,
    console_played_on="Xbox 360",
    rating_out_of_10=8
)

assassins_creed_3 = Games(
    name="Assassins Creed III",
    release_year=2012,
    console_played_on="Xbox 360",
    rating_out_of_10=10
)

fortnite = Games(
    name="Fortnite",
    release_year=2017,
    console_played_on="Xbox/PC",
    rating_out_of_10=9
)

gta_v = Games(
    name="GTA V",
    release_year=2013,
    console_played_on="Xbox/PC",
    rating_out_of_10=10
)


# add each instance of our games to our session
session.add(black_ops_2)
session.add(overwatch)
session.add(halo)
session.add(assassins_creed_3)
session.add(fortnite)
session.add(gta_v)


# commit our session to the database
session.commit()

# query the database to find all games
games = session.query(Game)
for game in games:
    print(
        game.id,
        game.name,
        game.release_year,
        game.console_played_on,
        game.rating_out_of_10,
        sep=" | "
    )
