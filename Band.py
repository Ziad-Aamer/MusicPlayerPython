import pymysql
from Song import Song
from Album import Album
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="music_player")
cur = conn.cursor()

class Band:

    def __init__(self, band_id, name):
        self.name = name
        self.band_id = band_id

    def __init__(self):
        self.name = ""
        self.band_id = 0

    def addBand(self, artistIDs):
        sql = """INSERT INTO band (band_name) VALUES (%s)"""
        cur.execute(sql, self.name)
        conn.commit()
        #link it with the artist
        band_id = ""
        cur.execute("select band_id from band where band_name = '" + self.name + "'")
        for row in cur:
            band_id = row[0]

        for aID in artistIDs:
            sql = """INSERT INTO band_artist (band_id,artist_id) VALUES (%s,%s) """
            cur.execute(sql, (band_id, aID))

        conn.commit()
        print("successfully added")

    def retrieveBandSongs(self):
        songs = []
        sql = "SELECT * from songs where band_id = '" + str(self.band_id) + "'"
        cur.execute(sql)
        for row in cur:
            s = Song()
            s.song_id = row[0]
            s.name = row[1]
            s.lyrics = row[2]
            s.length = row[3]
            s.genres = row[4]
            s.release_date = row[5]
            s.album_id = row[6]
            s.band_id = row[7]
            s.featured_artists = row[8]
            songs.append(s)

        return songs

    def retrieveBandAlbums(self):
        albums = []
        sql = "SELECT * from album where band_id = '" + str(self.band_id) + "'"
        cur.execute(sql)
        for row in cur:
            a = Album()
            a.album_id = row[0]
            a.title = row[1]
            a.band_name = row[2]
            a.band_id = row[3]
            albums.append(a)

        return albums
