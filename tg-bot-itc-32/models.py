from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey

from config import Base


class Author(Base):

    __tablename__ = "authors"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(150), unique=True, nullable=False)
    birth_date = Column(Date(), default=datetime.now().date())

    def __str__(self):
        return f"Author: {self.id}"

    def __repr__(self):
        return f"Author: {self.id}"


class Genre(Base):

    __tablename__ = "genres"

    id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)

    def __str__(self):
        return f"Genre: {self.id}"

    def __repr__(self):
        return f"Genre: {self.id}"


class Album(Base):

    __tablename__ = "albums"

    id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)
    author = Column(ForeignKey("authors.id"))
    created_date = Column(Date(), default=datetime.now().date())

    def __str__(self):
        return f"Album: {self.id}"

    def __repr__(self):
        return f"Album: {self.id}"


class Music(Base):

    __tablename__ = "musics"

    id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)
    genre = Column(ForeignKey("genres.id"), nullable=False)
    duration = Column(String(10))
    author = Column(ForeignKey("authors.id"))
    mp3_file_path = Column(String, unique=True)

    def __str__(self):
        return f"Genre: {self.id}"

    def __repr__(self):
        return f"Genre: {self.id}"


class AlbumMusic(Base):

    __tablename__ = "album_music"

    id = Column(Integer(), primary_key=True)
    album_id = Column(ForeignKey("albums.id"))
    music_id = Column(ForeignKey("musics.id"))

    def __str__(self):
        return f"Album: {self.album_id} Music: {self.music_id}"

    def __repr__(self):
        return f"Album: {self.album_id} Music: {self.music_id}"


if __name__ == "__main__":
    Base.metadata.create_all()
0.

