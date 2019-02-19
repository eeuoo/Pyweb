from collections import namedtuple

Song = namedtuple("Song", "songno title likecnt")

print(Song)

s1 = Song(111, '만남', 100)
s2 = Song(songno=222, title='강남스타일', likecnt=200)
s3 = Song._make([333, '노래노래', 300])
d1 = s1._asdict()

print("d1 === ", d1)

for s in [s1,s2,s3]:
    print(s, getattr(s, 'title'), s.title)