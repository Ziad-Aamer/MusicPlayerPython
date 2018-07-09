import PlayList
from Song import Song
from Band import Band
from Artist import Artist
import winsound
from Album import Album
from PlayList import PlayList
from playsound import playsound
import pymysql
import  operator
# playsound('C:/Users/Zoro/Music/test/New Years Day.mp3')
# winsound.PlaySound("C:/Users/Zoro/Music/test/tiny_tim.wav", winsound.SND_FILENAME)
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="music_player")
cur = conn.cursor()


class MusicPlayer:

    def __init__(self):
        self.myLibrary = []
        self.myArtists = []
        self.myPlayLists = []
        self.myAlbums = []
        self.myBands = []
        self.myArtists = []

    def retrievePlayLists(self):
        sql = "SELECT * from playlists"
        cur.execute(sql)
        self.myPlayLists = []
        for row in cur:
            p = PlayList()
            p.playlist_id = row[0]
            p.name = row[1]
            p.description = row[2]
            self.myPlayLists.append(p)

    def retrieveSongs(self):
        sql = "SELECT * from songs"
        cur.execute(sql)
        self.myLibrary = []
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
            self.myLibrary.append(s)

    def retrieveBands(self):
        sql = "SELECT * from band"
        cur.execute(sql)
        self.myBands = []
        for row in cur:
            b = Band()
            b.band_id = row[0]
            b.name = row[1]
            self.myBands.append(b)

    def retrieveArtists(self):
        sql = "SELECT * from artist"
        cur.execute(sql)
        self.myArtists = []
        for row in cur:
            a = Artist()
            a.artist_id = row[0]
            a.name = row[1]
            a.birth_date = row[2]
            self.myArtists.append(a)

    def retrieveAlbums(self):
        sql = "SELECT * from album"
        cur.execute(sql)
        self.myAlbums = []
        for row in cur:
            a = Album()
            a.album_id = row[0]
            a.title = row[1]
            a.band_name = row[2]
            a.band_id = row[3]
            self.myAlbums.append(a)

    def viewLibrary(self):
        self.retrieveSongs()
        print("List of songs in Library:")
        for i in range(0, len(self.myLibrary)):
            print(i + 1, ".", self.myLibrary[i].name)

    def viewArtists(self):
        print("List of artists:")
        for i in range(0, len(self.myArtists)):
            print(i + 1, ".", self.myArtists[i].name)
    def viewAlbums(self):
        print("List of Albums:")
        for i in range(0, len(self.myAlbums)):
            print(i + 1, ".", self.myAlbums[i].title, "\ttracks:"
                  , len(self.myAlbums[i].retrieveAlbumSongs()))
    def viewBands(self):
        print("List of bands:")
        for i in range(0, len(self.myBands)):
            print(i + 1, ".", self.myBands[i].name)

    def viewPlayLists(self):
        print("List of PlayLists:")
        for i in range(0, len(self.myPlayLists)):
            print(i + 1, ".", self.myPlayLists[i].name, "\ttracks:"
                  , len(self.myPlayLists[i].retrievePlayListSongs()))

    def sortedPlayList(self, ascending, by, playListSongs):

        if ascending == "1":
            if by == "1":
                playListSongs.sort(key=operator.attrgetter('name'))
            if by == "2":

                self.retrieveArtists()
                self.myArtists.sort(key=operator.attrgetter('name'))
                songsList = []
                for song in playListSongs:
                    bol = False
                    for art in self.myArtists:
                        if bol:
                            break
                        sql = """SELECT band_id FROM band_artist where artist_id = (%s)"""
                        self.cur.execute(sql, art.artist_id)
                        for row in self.cur:
                            if row[0] == song.band_id and not bol:
                                songsList.append(song)
                                bol = True
                                break


                playListSongs = songsList

            if by == "3":
                self.retrieveAlbums()
                self.myAlbums.sort(key=operator.attrgetter('title'))
                songsList = []
                for album in self.myAlbums:
                    for song in playListSongs:
                        if song.album_id == album.album_id:
                            songsList.append(song)
                for song in playListSongs:
                    if song.album_id == 0:
                        songsList.append(song)
                playListSongs = songsList
            if by == "4":
                playListSongs.sort(key=operator.attrgetter('genres'))
            if by == "5":
                playListSongs.sort(key=operator.attrgetter('release_date'))
        else:
            if by == "1":
                playListSongs.sort(key=operator.attrgetter('name'), reverse=True)
            if by == "2":

                self.retrieveArtists()
                self.myArtists.sort(key=operator.attrgetter('name'), reverse=True)
                songsList = []
                for song in playListSongs:
                    bol = False
                    for art in self.myArtists:
                        if bol:
                            break
                        sql = """SELECT band_id FROM band_artist where artist_id = (%s)"""
                        self.cur.execute(sql, art.artist_id)
                        for row in self.cur:
                            if row[0] == song.band_id and not bol:
                                songsList.append(song)
                                bol = True
                                break


                playListSongs = songsList

            if by == "3":
                self.retrieveAlbums()
                self.myAlbums.sort(key=operator.attrgetter('title'),reverse=True)

                songsList = []
                for song in playListSongs:
                    if song.album_id == 0:
                        songsList.append(song)
                for album in self.myAlbums:
                    for song in playListSongs:
                        if song.album_id == album.album_id:
                            songsList.append(song)
                playListSongs = songsList
            if by == "4":
                playListSongs.sort(key=operator.attrgetter('genres'), reverse=True)
            if by == "5":
                playListSongs.sort(key=operator.attrgetter('release_date'), reverse=True)

        return playListSongs

#by\n1.name 2.artist 3.album 4.genre 5.release date.")