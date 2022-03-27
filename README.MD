# Recipe App

### Architecture

Flux store
Ubuntu
ElasticSearch
Django?
Nginx?

Create an interface for the frontend so that templates can be easily used

### Store Methods

===============
addRecipe
removeRecipe
showRecipe
hideRecipe
adjustQuantity
upVote
downVote
comment
recommend
tag
favorite

Allow dietary preferences and substitutions

Match substitutionson upvoted and starred

Once virtual box is running:

1. configure security and secret management
2. create scripts to pull code from GitHub and restart services

### To Run

Install Vagrant
https://www.vagrantup.com/docs/installation

create folder structure

```
\recipe_app
    \app
    \db
```

Check out hte code from GitHub in the appropriate folder
https://github.com/JonathanRys/recipe_app.git
https://github.com/JonathanRys/recipe_app_db.git

cd into the `app` folder and run
`vagrant up`

SSH into the server with
`vagrant ssh`
