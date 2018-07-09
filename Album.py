from Song import Song
import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="music_player")
cur = conn.cursor()


class Album:

    def __init(self):
        self.album_id = 0
        self.title = ""
        self.band_name = ""
        self.band_id = 0

    def addAlbum(self):
        sql = """INSERT INTO album (title,band_name,band_id) VALUES (%s,%s,%s)"""
        cur.execute(sql, (self.title, self.band_name,self.band_id))
        conn.commit()
        print("successfully added")

    def deleteAlbum(self):
        sql = "DELETE from album where album_id = '" + str(self.album_id) + "'"
        cur.execute(sql)
        conn.commit()
        print("Total number of rows deleted :", cur.rowcount)
        print("successfully deleted")

    def retrieveAlbumSongs(self):
        songs = []
        sql = "SELECT * from songs where album_id = '" + str(self.album_id) + "'"
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
