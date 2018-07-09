'''main here '''
from MusicPlayer import MusicPlayer
from Song import Song
from Artist import Artist
from Band import Band
from Album import Album
from PlayList import PlayList
from random import randint
import operator


MP = MusicPlayer()
while True:
    print("Welcome To Musicly \n 1. Playlists 2. Artists 3. Albums 4. Library 5. bands")
    choice = input("Enter Choice: ")
    if choice == "1":
        while True:
            choice2 = input("1. add new PlayList 2. Delete PlayList 3. View PlayList"
                            + " 4. View all PlayLists 5. back:\n")
            if choice2 == "1":
                playList = PlayList()
                playList.name = input("Enter PlayList name:")
                playList.description = input("Enter PlayList description:")
                playList.addPlayList()

            if choice2 == "2":
                pID = int(input("Enter # of PlayList:"))
                MP.retrievePlayLists()
                MP.myPlayLists[pID-1].deletePlayList()

            if choice2 == "3":
                plNum = int(input("Enter PlayList # :"))-1
                MP.retrievePlayLists()
                print(MP.myPlayLists[plNum].name)
                print(MP.myPlayLists[plNum].description)
                ascending = "1"
                by = "1"
                while True:
                    playListSongs = MP.myPlayLists[plNum].retrievePlayListSongs()
                    playListSongs = MP.sortedPlayList(ascending, by, playListSongs)
                    print("List of Songs:")
                    for i in range(0, len(playListSongs)):
                        print(i + 1, ".", playListSongs[i].name, "\tDuration: "
                              ,playListSongs[i].length)

                    print("\n1. add Song to PlayList 2. Delete song from PlayList "
                          + "3. Play Song by # 4. Play Song Randomly 5.Order "
                          + "6. back:")
                    choice21 = input()
                    print("")
                    if choice21 == "1":
                        MP.retrieveSongs()
                        MP.viewLibrary()
                        songNum = int(input("Enter song #:")) - 1
                        MP.myPlayLists[plNum].addSongToPlayList(MP.myLibrary[songNum].song_id)

                    if choice21 == "2":
                        songNum = int(input("Enter song #:")) - 1
                        MP.myPlayLists[plNum].deleteSongFromPlayList(playListSongs[songNum].song_id)
                    if choice21 == "3":
                        songNum = int(input("Enter song #:")) - 1
                        playListSongs[songNum].playSong()
                    if choice21 == "4":
                        if len(playListSongs) > 0:
                            playListSongs[randint(0, len(playListSongs)-1)].playSong()
                    if choice21 == "5":
                        ascending = input("1.Ascending  \t2.Descending")
                        by = input("by\n1.name 2.artist 3.album 4.genre 5.release date.")
                    if choice21 == "6":
                        break
                    else:
                        continue

            if choice2 == "4":
                MP.retrievePlayLists()
                MP.viewPlayLists()

            if choice2 == "5":
                break

    if choice == "2":
        while True:
            choice2 = input("1. add new Artist 2. Delete Artist 3. Play Songs to a certain Artist"
                            + " 4. View all Artist 5. back:\n")
            if choice2 == "1":
                artist = Artist()
                artist.name = input("Enter Artist name:")
                artist.birth_date = input("Enter birth date:")
                artist.addArtist()

            if choice2 == "2":
                aID = int(input("Enter # of artist:"))
                MP.myArtists[aID-1].deleteArtist()

            if choice2 == "3":
                MP.retrieveArtists()
                MP.viewArtists()
                artistNum = int(input("Enter # of artist:"))-1
                artistSongs = MP.myArtists[artistNum].retrieveArtistSongs()
                for i in range(0, len(artistSongs)):
                    print(i+1, ". ", artistSongs[i].name)
                while True:
                    songNum = int(input("Enter Song # to play or Enter 0 to back:"))-1
                    if songNum < 0 or songNum >= len(artistSongs):
                        print("back")
                        break
                    else:
                        artistSongs[songNum].playSong()

            if choice2 == "4":
                MP.retrieveArtists()
                MP.viewArtists()

            if choice2 == "5":
                break

    if choice == "3":
        while True:
            choice2 = input("1. add new Album 2. Delete Album 3. Play Songs to a certain Album"
                            + " 4. View all Albums 5. back:\n")
            if choice2 == "1":
                album = Album()
                album.title = input("Enter album title:")
                MP.retrieveBands()
                MP.viewBands()
                bandNum = int(input("Enter band #:"))-1
                album.band_name = MP.myBands[bandNum].name
                album.band_id = MP.myBands[bandNum].band_id
                album.addAlbum()

            if choice2 == "2":
                aID = int(input("Enter # of album:"))
                MP.retrieveAlbums()
                MP.myAlbums[aID-1].deleteAlbum()

            if choice2 == "3":
                MP.retrieveAlbums()
                MP.viewAlbums()
                albumNum = int(input("Enter # of album:"))-1
                albumSongs = MP.myAlbums[albumNum].retrieveAlbumSongs()
                for i in range(0, len(albumSongs)):
                    print(i+1, ". ", albumSongs[i].name)
                while True:
                    songNum = int(input("Enter Song # to play or Enter 0 to back:"))-1
                    if songNum < 0 or songNum >= len(albumSongs):
                        print("back")
                        break
                    else:
                        albumSongs[songNum].playSong()

            if choice2 == "4":
                MP.retrieveAlbums()
                MP.viewAlbums()

            if choice2 == "5":
                break

    if choice == "4":
        while True:

            choice4 = input("1. add new Song 2. Delete Song 3. Play Song 4. "
                            + "View Song 5.View All Songs 6.play certain genre 7.back :\n")
            #add song
            if choice4 == "1":
                s = Song()
                s.name = input("name:")
                s.genres = input("genres: ")
                s.lyrics = input("lyrics: ")
                s.length = input("length: ")
                s.release_date = input("release date: ")
                s.featured_artists = input("featured artists:")
                MP.retrieveBands()
                MP.viewBands()
                bandNum = int(input("band number:"))-1
                s.band_id = MP.myBands[bandNum].band_id
                #get albums of this band
                albumList = MP.myBands[bandNum].retrieveBandAlbums()
                alb = -1
                if len(albumList) == 0:
                    print("NO Albums for this band song is added single")
                else:
                    print("List of Albums for this band:")
                    for i in range(0,len(albumList)):
                        print(i + 1, ".", albumList[i].title, "\ttracks:"
                              , len(albumList[i].retrieveAlbumSongs()))
                    alb = int(input("Enter album number or 0 if single: "))-1
                if alb == -1 :
                    s.album_id = 0
                else:
                    s.album_id = albumList[alb].album_id
                s.addSong()
            # delete song
            elif choice4 == "2":
                sID = int(input("Enter song # to delete"))-1
                MP.myLibrary[sID].deleteSong(MP.myLibrary[sID].song_id)
            #play song
            elif choice4 == "3":
                sID = int(input("Enter song # to play "))
                MP.myLibrary[sID-1].playSong()
            #view song
            elif choice4 == "4":
                sID = int(input("Enter song # to View:"))
                MP.myLibrary[sID - 1].viewSong()
            elif choice4 == "5":
                MP.retrieveSongs()
                MP.viewLibrary()
            elif choice4 == "6":
                MP.retrieveSongs()
                genre = input("enter genre")
                for song in MP.myLibrary:
                    if song.genres == genre:
                        song.playSong()

            else:
                break

    if choice == "5":
        while True:
            choice5 = input("1. add new Band 2. Play Songs to a certain Band"
                            + " 3. View all Bands 4. back:\n")
            if choice5 == "1":
                band = Band()
                band.name = input("Enter Band name:")
                bandNum = int(input("Enter # of band Members:"))
                MP.retrieveArtists()
                MP.viewArtists()
                artistsIDsList = []
                for i in range(0, bandNum):
                    artistsIDsList.append(MP.myArtists[int(input("Enter # of the artist:"))-1].artist_id)

                band.addBand(artistsIDsList)

            if choice5 == "2":
                MP.retrieveBands()
                MP.viewBands()
                bandNum = int(input("Enter # of band"))-1
                bandSongs = MP.myBands[bandNum].retrieveBandSongs()
                for i in range(0, len(bandSongs)):
                    print(i+1, ". ", bandSongs[i].name)
                while True:
                    songNum = int(input("Enter Song # to play or Enter 0 to back:"))-1
                    if songNum < 0 or songNum >= len(bandSongs):
                        print("back")
                        break
                    else:
                        print("Playing")
                        bandSongs[songNum].playSong()

            if choice5 == "3":
                MP.retrieveBands()
                MP.viewBands()

            if choice5 == "4":
                break

else:
        print("No such a choice")




