alias api-build='docker build --tag api-consola --file Dockerfile .'
alias api-bash='docker run --rm -it -p 9999:9999 --name api-consola -v $PWD:/usr/src/app api-consola bash'
alias api-py='docker run --rm -it -p 9999:9999 --name api-consola -v $PWD:/usr/src/app api-consola python'
alias api-pip='docker exec -it api-consola pip'