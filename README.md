# Episode Tracker
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26d4663ca6294e249336bd23a24abc6e)](https://www.codacy.com/project/jonathankamau/EpisodeTracker-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jonathankamau/EpisodeTracker-API&amp;utm_campaign=Badge_Grade_Dashboard)
[![Maintainability](https://api.codeclimate.com/v1/badges/ba0dcc23849921ad710a/maintainability)](https://codeclimate.com/github/jonathankamau/EpisodeTracker-API/maintainability)

# Overview

Episode Tracker is an API that enables the user to be able to keep track of the TV Shows they are watching. They are able to search for TV Shows, view details of the shows and their episodes as well as log the episodes they have watched, They also able to tag their favourite shows and are able to get suggestions of similar shows.

# Requirements
Python (3.6)
Django (2.0.5)

# Installation
1. create a working directory

	      $ mkdir -p work-dir
	      $ cd workdir


2. clone this repo to local
    - Via SSH

          	git clone git@github.com:jonathankamau/EpisodeTracker-API.git

    - via HTTPS

          	git clone https://github.com/jonathankamau/EpisodeTracker-API.git
          
3. Navigate to project directory
    
    
      		$ cd EpisodeTracker-API
      		$ git checkout develop

4. Run the following commmand:

            $ make dev

    This command creates a docker instance for the postgres database as well as for the API and runs the server as well.

    Open your browser to http://0.0.0.0:8000 and you should see the browsable version of the API

5. Running tests

    Run the following command in order to run tests:

        $ make test

## Authors

* **Jonathan Kamau** - [Github Profile](https://github.com/jonathankamau)


## License

This project is licensed under the MIT License.



