#!/bin/bash
rm -rf data
mkdir -p data/{db,db_log}
sudo chmod 777 data/*
docker-compose -f docker-compose.yml up --force-recreate --build