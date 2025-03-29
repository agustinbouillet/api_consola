#!/bin/bash

# Check if the "data" directory exists
if [ ! -d "data" ]; then
    # If it doesn't exist, create it
    mkdir "data"
    echo "Created directory: data"
else
    echo "Directory 'data' already exists."
fi


alias api_build='docker build --tag api-consola --file Dockerfile .'
alias api_bash='docker run --rm -it -p 9999:9999 --name api-consola -v $PWD:/usr/src/app api-consola bash'
alias api_py='docker run --rm -it -p 9999:9999 --name api-consola -v $PWD:/usr/src/app api-consola python'
alias api_pip='docker exec -it api-consola pip'