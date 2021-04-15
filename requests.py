search_artista = 'https://musicbrainz.org/ws/2/artist?query=ed+sheeran&limit=1'
artists[0].id

search_albums = 'https://musicbrainz.org/ws/2/release-group?artist=b8a7c51f-362c-4dcb-a259-bc6e0095f0a6&type=album'
album[0].release_group[0].id

search_canciones = 'https://musicbrainz.org/ws/2/release-group/05ce100c-eddf-4967-8d7e-33fc0883fe39?inc=releases'
recordings[].title

search_ls='https://www.theaudiodb.com/api/v1/json/1/search.php?s=coldplay'

get_imge='coverartarchive.org/release/976ea795-9dfd-4d85-9a49-ceb310014236'