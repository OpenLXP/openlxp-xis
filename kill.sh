#!/bin/bash
echo '#####################################################'
echo 'Stopping all running containers'
echo '#####################################################'
docker stop $(docker ps -a -q) --force

echo ''
echo '#####################################################'
echo 'Removing all stopped containers'
echo '#####################################################'
docker rm $(docker ps -a -q) --force

echo ''
echo '#####################################################'
echo 'Removing all images'
echo '#####################################################'
docker rmi $(docker images -a -q) --force

echo ''
echo '#####################################################'
echo 'Removing all volumes'
echo '#####################################################'
docker volume rm $(docker volume ls -q) --force

echo ''
echo '#####################################################'
echo 'Pruning the system'
echo '#########################0############################'
docker system prune -a -f --volumes

echo ''
echo "Done nuking everything!"