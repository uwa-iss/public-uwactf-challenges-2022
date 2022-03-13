docker image build -t rock-paper-scissors .
docker container run -p 1337:1337 --rm --name rock-paper-scissors-container rock-paper-scissors:latest