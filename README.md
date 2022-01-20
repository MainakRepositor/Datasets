# Datasets
A bunch of some 200 datasets. You can call it mini-kaggle :)
#### [Download multiple data in csv file from here](https://drive.google.com/drive/folders/1QnVd_0t3NW3GiG8I6Ly1ypyablUawJmO?usp=sharing)

<div align="center"><span><img height="500" width="500" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Data_types_-_en.svg/1200px-Data_types_-_en.svg.png"/>    <img height="500" width="500" src="https://miro.medium.com/max/430/0*rNapZQnyP5EBLYli.png"></span></div>



### Want to download any csv file for local use? Follow the steps mentioned below: 👇

<ol>
  <li>Go to a csv file in a repository of your choice</li>
  <li>From the top right bar just above the file section, select and click on "Raw" button</li>
  <li>A page will appear with comma separated data with no styling</li>
  <li>Copy the page url</li>
  <li>Make a folder in your desktop</li>
  <li>Open that folder in your favourite code editor and make a simple python file inside the folder. Name it as you please.</li>
  <li>Copy this code [From the section below]</li>
  <li>Run the python file</li>
  <li>The csv file will get downloaded within sometime, depending upon file size</li>
  <li>Now you are ready the use it locally!!</li>

</ol>

  ``` 
  import requests
  import pandas as pd
  url = '{(copied url here)}' 
  res = requests.get(url, allow_redirects=True)
  with open('download_file_name.csv','wb') as file:
      file.write(res.content)
  download_file_name = pd.read_csv('download_file_name.csv') 
  ```  
