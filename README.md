# Simple-Webpage-Downloader

There are times where we need to download webpages in some intervals (hourly, daily, weekly, ...). This repository solves this issue by providing an easy to setup service that will trigger the downloads and save the files to an specified folder in a coordinated way by simply modifying the `URL_LIST.json` file.

<div>
    <div align="middle">
        <img src="documentation/Main design.png" alt="Main design" width=700>
    </div>
    <div align="middle">
      <i>Overview of architectural design.</i>
    </div>
</div>

## 1. Introduction

Many data engineers face the issue of having to manually download websites in recurring intervals. For these cases, this repository should come handy. It has a central file (`URL_LIST.json`) that specifies the URLs to visit and download the HTML from, as well as the location where these files should be saved to.

This json file is read everytime a download cycle happens, as this allows to modify the file live, without having to restart the service (and build the image in case docker is used).

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

### 3.1. Back-of-the-envelope calculations
Find below a rough estimation of the storage capacity requirements:

Assumptions:
* Size per page: 1 Mb
* Max pages downloaded: 10 Pages/cycle
* Cycle: Hourly
* Data history retention: 5 years

Memory requirements:
* 1 Mb * 10 Pages/cycle * 24 hours/day * 365 days/year * 5 years = 485 Gb

(Note that it should be possible to reduce this number by compressing the downloaded files).

### 3.2. Architectural design

When designing this solution the following points have been considered:
* Keep it as simple as possible to easy troubleshooting and reduce memory footprint.
* Make it modular so it can be deployed easily and it can play nicelly with other applications that may use similar services and features (ports, folders, selenium, ...).
* Make it in such a way that it is easy to add/remove URLs

Based on above points, the following solution was designed:
<div>
    <div align="middle">
        <img src="documentation/Main design.png" alt="Main design" width=700>
    </div>
    <div align="middle">
      <i>Overview of architectural design.</i>
    </div>
</div>

### 3.3. Technical decisions

While working on this project the following choices have been done, that although not critical, they are interesting to consider:

* Files are being saved locally. This is done in such way to reduce the network utilization and ease the saving of the downloaded files. This obviously creates the downside of limiting the amount of webpages you can store in your local drive (although based on the back-of-the-envelope calculations, this shouldn't be a big issue). However, something that must be mentioned is the lack of redundancy, which could mean the loss of all the data if the harddrive crashes.

* Manually managing the save location. This is decided due to the needs of each URL downloads being different (some URLs may contain news info, while other may be music record related). This puts a bit of initial burden in the developer to make sure everything is setup correctly, but once setup it shouldn't become an issue.

* "Constantly" reading the file `URL_LIST.json` file. This simple solution is adopted as it allows to easily add/remove URLs without having to stop the services, as well as to facilitate the modification of the file with any text editor (as compared to using SQLITE).

## Considerations
As mentioned previously, it must be noted that a simple database could be used to replace the `URL_LIST.json` file (such as SQLite). However, this would require managing connections and would make the code a bit more complicated. Thus a simple json file solution was adopted.

The URLs are downloaded in a sequential order, this shouldn't be an issue as the highest frequency implemented is hourly. However, it should be possible to implement concurrency. Note though, that if a concurrency solution is implemented you will need to ensure that two concurring threads don't try to access the same domain at the same time, as the server may consider your calls as part as a DDoS attack (rare but possible) and block your IP. You will also need to worry about creating unique names if both threads try to save the file to the same location.
