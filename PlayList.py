from Song import Song
import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="music_player")
cur = conn.cursor()


class PlayList:
    def __init(self,playlist_id, name, description, songs):
        self.playlist_id = playlist_id
        self.name = name
        self.description = description

    def addPlayList(self):
        sql = """INSERT INTO playlists (name,description) VALUES (%s,%s)"""
        cur.execute(sql, (self.name, self.description))
        conn.commit()
        print("successfully added")

    def deletePlayList(self):
        sql = "DELETE from playlists where playlist_id = '" + str(self.playlist_id) + "'"
        cur.execute(sql)
        conn.commit()
        print("Total number of rows deleted :", cur.rowcount)
        print("successfully deleted")

    def retrievePlayListSongs(self):
        songs = []
        songsIDs = []
        sql = "SELECT song_id from playlists_songs where playlist_id = '" + str(self.playlist_id) + "'"
        cur.execute(sql)
        for row in cur:
            sid = row[0]
            songsIDs.append(sid)

        for sid in songsIDs:
            sql = "SELECT * from songs where song_id = '" + str(sid) + "'"
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

    def addSongToPlayList(self,sid):
        sql = """INSERT INTO playlists_songs (song_id,playlist_id) VALUES (%s,%s)"""
        cur.execute(sql, (str(sid), str(self.playlist_id)))
        conn.commit()
        print("successfully added")

    def deleteSongFromPlayList(self, sid):
        sql = "DELETE FROM playlists_songs WHERE song_id = '" + str(sid) + "'"
        cur.execute(sql)
        conn.commit()
        print("Total number of rows deleted :", cur.rowcount)
        print("successfully deleted")
