#!/bin/sh
docker build -t flask_plot_docker_nginx:0.0.1 -f nginx/Dockerfile nginx/
docker build -t xaratustrah/flask_plot_docker:0.0.1 -f flask_plot/Dockerfile flask_plot/
docker stack deploy -c docker-compose_stack.yml flask_plot_docker_stack
