sudo chmod 666 /var/run/docker.sock
sudo service docker restart
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up

// to change readonly mode
sudo chown -R $(whoami) .
