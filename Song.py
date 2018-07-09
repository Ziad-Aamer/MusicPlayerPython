import pymysql
from playsound import playsound

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="music_player")
cur = conn.cursor()

class Song:
    PATH = "C:/Users/Zoro/Music/test/"

    def __init(self):
        self.name = ""
        self.release_date = ""
        self.genres = ""
        self.lyrics = ""
        self.length = ""
        self.album_id = 0
        self.featured_artists = ""
        self.band_id = 0
        self.song_id = 0

    def addSong(self):
        sql = """INSERT INTO songs (name,band_id,featured_artists,album_id,release_date,genres,
                lyrics,length) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql, (self.name, str(self.band_id), self.featured_artists
                          , str(self.album_id), self.release_date, self.genres
                          , self.lyrics, self.length ))
        conn.commit()
        print("successfully added")

    def deleteSong(self,id):
        sql = "DELETE from songs where song_id = '" + str(id) + "'"
        cur.execute(sql)
        conn.commit()
        print("Total number of rows deleted :", cur.rowcount)
        print("successfully deleted")

    def playSong(self):
        print("Playing ", self.name)
        playsound(Song.PATH + self.name)

    def getBandName(self):
        sql = """SELECT band_name FROM band WHERE band_id = (%s)"""
        cur.execute(sql, str(self.band_id))
        bandName = ""
        for row in cur:
            bandName = row[0]

        return bandName

    def getAlbumName(self):
        sql = """SELECT title FROM album WHERE album_id = (%s)"""
        cur.execute(sql, str(self.album_id))
        albumName = ""
        for row in cur:
            albumName = row[0]

        return albumName

    def viewSong(self):
        print("name: ", self.name)
        print("Band:", self.getBandName())

        if self.album_id == 0 :
            print("Album: Single")
        else:
            print("Album:", self.getAlbumName())
        print("featured artists : ", self.featured_artists)
        print("lyrics: ", self.lyrics)
        print("length: ", self.length)
        print("genres: ", self.genres)
        print("release date: ", self.release_date)



