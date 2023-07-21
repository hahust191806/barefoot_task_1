import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Thông tin xác thực của bạn
client_id = '8f136fd89ed141f787a74b0a26a801dc'
client_secret = '5168366b750e4e8f802ba9f8d6e6b7cd'

# Khởi tạo đối tượng Spotipy
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Thực hiện tìm kiếm bằng chủ đề "rap"
results = sp.search(q='genre:rap', type='track', limit=50, offset=0)

# Lấy danh sách các bài hát
tracks = results['tracks']['items']

# Lặp lại quá trình tìm kiếm và lấy danh sách các bài hát cho đến khi đạt được số lượng bài hát mong muốn
while len(tracks) < 1000:
    results = sp.search(q='genre:rap', type='track', limit=50, offset=len(tracks))
    tracks += results['tracks']['items']

# In số lượng bài hát đã tìm thấy
print(len(tracks))