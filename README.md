# Spotify-Playlist-Generator

## Desscription

For the first time, I made a New Year's resolution: NYR 2020-366 days, 366 bands. So I made a script which will make playlists of 366 bands , bands I have not heard before, on Spotify. 

## Different Scripts Used
1. list366.py : This creates a list of 366 bands based on the bands I like
2. playlist_a.py : This creates the playlist. Run once to create one playlist. 

## Text Files

1. `artist_list.txt` : List of artists I really,really like. I use this information to find similar artists
2. `blacklist.txt` : The artists I have already listened to (and a few I don't like). I don't want repitition in the final list of 366 artists
3. `all.txt` : List generated after using the artist_list.txt . In my case the list contained around 430 artists after filtering out the ones from `blacklist.txt`
4. `list366.txt` : The final list of 366 artists, picked out at random from `all.txt`
5. `last.txt` : stores the name of the last artist whose playlist was created. So the next playlist will be of the artist right after this one in the `list366.txt`

## How To Use 

1. If your tastes are like mine, just directly run `python3 playlist_a.txt` . 
2. You can delete contents of every txt file, and in `artist_list.txt` add a bunch of artists you like, in the `blacklist.txt` add a bunch of artists you don't want to repeat, and then run `python3 list366.py`. Check that the list of 366 artists is created, and then run `python3 playlist_a.txt` 
