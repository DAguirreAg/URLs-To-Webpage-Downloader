# Simple-Webpage-Downloader

There are times that we need to download webpages in some intervals (hourly, daily, weekly, ...). This repository solves this issue by providing an easy to setup service that will trigger the download in a coordinated way.

<div>
    <div align="middle">
        <img src="documentation/Main design.png" alt="Main design" width=700>
    </div>
    <div align="middle">
      <i>Overview of architectural design.</i>
    </div>
</div>

## 1. Introduction



## 2. How to use it

Follow next steps:
* Clone this repository to your computer.
* Open `URL_LIST.json` file and modify the URLs and save folder location. Note that you should add the URLs of the webpages that you will like to download in the corresponding section (daily section if you want to download that webpage daily, ...).
* Open `docker-compose.yml` file and modify the `volumes` section with the location of where the downloaded files should be saved and the location of the `URL_LIST.json`.

<div>
    <div align="middle">
        <img src="documentation/URL_LIST.json file.png" alt="URL_LIST.json file" height="250px">
        <img src="documentation/docker-compose.yml file.png" alt="docker-compose.yml file" height="250px">
    </div>
    <div align="middle">
      <i>URL_LIST.json and docker-compose.yml files.</i>
    </div>
</div>

* Open a terminal window and `cd` to the `source` folder of this repository.
* In the terminal type `docker compose up` to launch the services.
* Open a browser and visit [http://localhost:8001/](http://localhost:8001/).
<div>
    <div align="middle">
        <img src="documentation/Backend endpoints.png" alt="Backend endpoints" width=700>
    </div>
    <div align="middle">
      <i>Backend endpoints.</i>
    </div>
</div>

* (Option 1) Setup several cron jobs to call the endpoint in a hourly, daily, weekly, ... manner. Remember that you should pass the `frequency` paratemer in the endpoint URL call so the scripts knows which URLs to download.
* (Option 2) Setup a data-pipeline orchestration tool (like Airflow) to call the endpoint accordingly. Note that a dag script is already provided into this repository so you can easily modify it.


## 3. Technical details


## Considerations
It must be noted that a simple database could be used to replace the `URL_LIST.json` file (such as SQLite). However, this would require managing connections and would make the code a bit more complicated. Thus a simple json file solution was adopted.

The URLs are downloaded in a sequential order, this shouldn't be an issue as the highest frequency implemented is hourly. However, it should be possible to implement concurrency. Note though, that if a concurrency solution is imlpemented you will need to ensure that two concurring threads don't try to access the same domain at the same time, as the server may consider your calls as part as a DDoS attack (rare but possible) and block your IP.


