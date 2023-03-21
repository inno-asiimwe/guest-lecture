.PHONY: $(MAKECMDGOALS)

DOCKER_DEV_COMPOSE_FILE := docker-compose.yml

# `make setup` will be used after cloning or downloading to fulfill
# dependencies, and setup the the project in an initial state.
# This is where you might download rubygems, node_modules, packages,
# compile code, build container images, initialize a database,
# anything else that needs to happen before your server is started
# for the first time

setup: ## Project Setup
	@ ${INFO} "Create default environment files"
	@ cp backend/.env.sample backend/.env && cp frontend/.env.sample frontend/.env
	@ ${INFO} "Building required docker images"
	@ docker compose -f ${DOCKER_DEV_COMPOSE_FILE} build api frontend
	@ ${INFO} "Images successfully built"
	@ echo " "

# `make server` will be used after `make setup` in order to start
# an http server process that listens on any unreserved port
#	of your choice (e.g. 8080). 
server:setup
	@ ${INFO} "Starting local development servers"	
	@ docker compose -f $(DOCKER_DEV_COMPOSE_FILE) up

# `make test` will be used after `make setup` in order to run
# your test suite.
test:setup
	@ ${INFO} "Running backend tests"
	@ docker compose -f $(DOCKER_DEV_COMPOSE_FILE) run --rm api nose2 -v --with-coverage --coverage app

clean:
	@ ${INFO} "Cleaning up ..."
	@ docker compose -f $(DOCKER_DEV_COMPOSE_FILE) down --rmi all

# colors
YELLOW := $(shell tput -Txterm setaf 3)
NC := "\e[0m"

#shell Functions
INFO := @bash -c 'printf $(YELLOW); echo "===> $$1"; printf $(NC)' SOME_VALUE