# import sys
# sys.stdin = open("input.txt", "r")

def solve():
    input()

    playlist_cnt = int(input())

    playlists = dict()

    for iter in range(playlist_cnt):
        playlist = input()

        playlist_name = playlist.rsplit(" ", 1)[0]
        songs_cnt = int(playlist.rsplit(" ", 1)[1])

        playlists[playlist_name] = []

        for jter in range(songs_cnt):
            song = input().strip()

            song_name = song.split(" length ")[0]
            song_length = int( (song.split(" length ")[1])[:2] )*60 + int( (song.split(" length ")[1])[3:] )

            playlists[playlist_name].append([song_name, song_length])



    songs_listen_cnt = dict()


    actions_cnt = int(input())

    ost_time = dict()

    for iter in range(actions_cnt):
        action = input()

        act = action.split(" ", 1)[0]
        tmp = action.split(" ", 1)[1].rsplit(" ", 2)
        playlist_name = tmp[0]
        playlist_length = int( (tmp[2])[:2] )*60 + int( (tmp[2])[3:] )
        
        if (act == "Restart"):
            ost_time[playlist_name] = 0

        ost = ost_time.get(playlist_name, 0)
        ost_time[playlist_name] = ost + playlist_length


        for song in playlists[playlist_name]:
            
            if (ost == 0 and playlist_length == 0):
                break


            if (ost == 0):
                songs_listen_cnt[song[0]] = songs_listen_cnt.get(song[0], 0) + 1

            if (ost != 0):
                ost -= song[1]
            else:
                playlist_length -= song[1]

    print(len(songs_listen_cnt))
    out = []
    for el in (songs_listen_cnt.keys()):
        out.append([-songs_listen_cnt[el], el])
        
    out.sort()

    for el in out:
        print(el[1], "played", -el[0], "times")



t = int(input())

for i in range(t):
    solve()
