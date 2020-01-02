import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import datetime
import requests as req
import random
import spotify_token as st 

uid = "<username..get it from account settings>"
client_id = '<client id >'
client_secret = '<client secret>'
# get the client secret and id from dev console of spotify
data = st.start_session(uid,"<password>")
post_token=data[0]
cred = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=cred)
def get_songs(artist,sp=sp):

	uris = ""
	song_uris = ""
	result = sp.search(artist)
	uri = result['tracks']['items'][0]['artists'][0]['uri']
	sp_albums = sp.artist_albums(uri, album_type='album')
	if len(sp_albums['items']) >1:
		b = random.randint(0,len(sp_albums['items'])-1)
		uris = sp_albums['items'][b]['uri']
		songs = sp.album_tracks(uris)
		n = random.randint(0,len(songs['items'])-1)
		sname = songs['items'][n]['name']
		song_uris=songs['items'][n]['uri']
	return song_uris

def addSongs(tracks,pl_id,uid=uid):
	# req_header = {'Authorization':'Bearer {}'.format(get_token)}
	uid = "<username...same as the global one>"
	post_header = {'Authorization': 'Bearer {}'.format(post_token), 'Accept': 'application/json','Content-Type':'application/json'}		
	body = {'uris': [tracks]}
	r = req.post('https://api.spotify.com/v1/users/{}/playlists/{}/tracks'.format(uid,pl_id),headers=post_header,json=body)
	print(r.status_code)	

def createPlaylist(artist):
	_day = datetime.datetime.today().strftime('%m/%d')
	if _day[0]=="0":
		_day = _day[1:]
	name = str(_day)+":{}".format(artist)
	playlist_id = ''
	body = {'name':name,'description':'Just a playlist','public':'false'}
	header = {'Authorization': 'Bearer {}'.format(post_token),'Content-Type': 'application/json'}
	r = req.post('https://api.spotify.com/v1/users/{}/playlists'.format(uid),headers=header,json=body)
	if r.status_code in [200,201]:
		playlist_id = r.json()['id']
	return playlist_id	

f = open('list366.txt','r')
d = open('last.txt','r+')
c=d.read().split("\n")
d_data = c[len(c)-1]
tracklist=[]
__f = f.read().split("\n")
_artist=""
if d_data =="":
	_artist = __f[0]
elif d_data!="":
	_artist = __f[__f.index(d_data)+1]
plID=createPlaylist(_artist)
for p in range(0,16):
	tracklist.append(get_songs(_artist))
print(tracklist)	
for q in range(0,len(tracklist)):
	addSongs(tracklist[q],plID);			
d.write("\n"+_artist)
f.close()
d.close()	
