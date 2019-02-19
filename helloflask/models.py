from sqlalchemy import Column, Integer, String, Float, ForeignKey, PrimaryKeyConstraint
from helloflask.init_db import Base
from sqlalchemy.orm import relationship, backref


class DailyList(Base):
    __tablename__ = 'DailyList'
    id = Column(Integer,primary_key=True)
    rank = Column(Integer)
    title = Column(String)
    singer = Column(String)
    likecnt = Column(Integer)
    song_id = Column(Integer, ForeignKey('SongInfo.song_id'))
    album_id = Column(Integer, ForeignKey('AlbumInfo.album_id'))
    crawl_date = Column(String)

    song = relationship('SongInfo')    
    album = relationship('AlbumInfo')

class MappingSS(Base):
    __tablename__ = 'MappingSS'
    song_id = Column(Integer, ForeignKey('SongInfo.song_id'), primary_key=True)
    title = Column(String)
    singer_name = Column(String)
    singer_id = Column(Integer, ForeignKey('Singer.singer_id'))

    song = relationship('SongInfo')
    singer = relationship('Singer')

class Singer(Base):
    __tablename__ = 'Singer'
    singer_id = Column(Integer, primary_key=True)
    singer_name = Column(String)

class SongInfo(Base):
    __tablename__ = 'SongInfo'
    song_id = Column(Integer,primary_key=True)
    title = Column(String)
    genre = Column(String)
    singer = Column(String)
    likecnt = Column(Integer)
    album_id = Column(Integer, ForeignKey('AlbumInfo.album_id'))
    album_name = Column(Integer)
    release_date = Column(Integer)

    album = relationship('AlbumInfo')

    
class AlbumInfo(Base):
    __tablename__ = 'AlbumInfo'
    album_id = Column(Integer, primary_key=True)
    album_name = Column(String)
    agency = Column(String)
    rate = Column(Float)
    album_likecnt = Column(Integer)
    type = Column(String)
    singer = Column(String)
    release_date = Column(String)

    songs = relationship('SongInfo')

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String(512), unique=True)
    passwd = Column(String(512))
    nickname = Column(String(512))

    def __init__(self, email=None, nickname='손님'):
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return 'User %s, %r, %r' % (self.id, self.email, self.nickname)
