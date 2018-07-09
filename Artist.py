from Song import Song
import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="music_player")
cur = conn.cursor()


class Artist:
    def __init(self, artist_id, name, birth_date):
        self.artist_id = artist_id
        self.name = name
        self.birth_date = birth_date

    def addArtist(self):
        sql = """INSERT INTO artist (artist_name,date_of_birth) VALUES (%s,%s)"""
        cur.execute(sql, (self.name, self.birth_date))
        #create new band called soloArtistName
        sql = """INSERT INTO band (band_name) VALUES (%s)"""
        cur.execute(sql, "solo" + self.name)
        conn.commit()

        #link it with the artist
        band_id = ""
        artist_id = ""
        cur.execute("select band_id from band where band_name = '" + "solo"+self.name + "'")
        for row in cur:
            band_id = row[0]
        cur.execute("select artist_id from artist where artist_name = '" + self.name + "'")
        for row in cur:
            artist_id = row[0]
        sql = """INSERT INTO band_artist (band_id,artist_id) VALUES (%s, %s)"""
        cur.execute(sql, (str(band_id), str(artist_id)))
        conn.commit()
        print("successfully added")

    def deleteArtist(self):
        sql = "DELETE from artist where artist_id = '" + str(self.artist_id) + "'"
        cur.execute(sql)
        sql = "DELETE from band where band_name = '" + "solo"+self.name + "'"
        cur.execute(sql)
        conn.commit()
        print("Total number of rows deleted :", cur.rowcount)
        print("successfully deleted")

    def retrieveBandsIDs(self):
        bandIDs = []
        sql = "SELECT band_id from band_artist where artist_id = '" + str(self.artist_id) + "'"
        cur.execute(sql)
        for row in cur:
            bandIDs.append(row[0])

        return bandIDs

    def retrieveArtistSongs(self):
        songs = []
        bandIDs = self.retrieveBandsIDs()
        for bid in bandIDs:
            sql = "SELECT * from songs where band_id = '" + str(bid) + "'"
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
