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

Install Vagrant and VirtualBox
https://www.vagrantup.com/docs/installation

create folder structure

```
\recipe_app
    \app
    \db
```

Check out the code from GitHub in the appropriate folder
https://github.com/JonathanRys/recipe_app.git
https://github.com/JonathanRys/recipe_app_db.git

cd into the `app` folder and run
`vagrant up`

this might fail the first time with an error about the creator_uid.  If that happens, update this file to contain the number listed in the error:
`.vagrant/machines/default/virtualbox/creator_uid`

SSH into the server with
`vagrant ssh`
