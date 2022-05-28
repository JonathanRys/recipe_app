# Recipe App

### Architecture

* Ubuntu
* ElasticSearch
* Flask
* uWSGI
* Nginx
* React
* MobX


### To Run

Install Vagrant and VirtualBox
https://www.vagrantup.com/docs/installation

create folder structure

```
\recipe_app
    \app
    \db
```

Check out the code from GitHub in the appropriate folder:
* https://github.com/JonathanRys/recipe_app.git
* https://github.com/JonathanRys/recipe_app_db.git

cd into the `app` folder and run
`vagrant up`

The react site should be available at http://localhost:8086

SSH into the server with
`vagrant ssh`
