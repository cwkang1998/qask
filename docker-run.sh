#!/bin/bash
rm -rf data
mkdir -p data/{db,db_log}
sudo chmod 777 data/*
filename="docker-compose.yml"

if [ "$mode" = "rebuild" ]; then
  docker-compose -f $filename up --force-recreate --build
else
  docker-compose -f $filename up
fi