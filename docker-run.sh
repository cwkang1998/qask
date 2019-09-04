#!/bin/bash
mkdir -p data/{db,db_log}
sudo chmod 777 data/*
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up