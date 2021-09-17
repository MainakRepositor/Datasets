import requests
import pandas as pd
url = 'https://raw.githubusercontent.com/AbdoSabri99/Face-Recognition-Using-PCA/main/face_data.csv'
res = requests.get(url, allow_redirects=True)
with open('face.csv','wb') as file:
    file.write(res.content)
face_data = pd.read_csv('face.csv')
