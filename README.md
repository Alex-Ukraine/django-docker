Step by step:
sudo chmod 666 /var/run/docker.sock
sudo service docker restart
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up

// to change readonly mode
sudo chown -R $(whoami) .

sudo apt install npm
npm init -y
put to package.json scripts "dev": "webpack --mode development ./src/index.js --output ./static/frontend/main.js"
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm run dev