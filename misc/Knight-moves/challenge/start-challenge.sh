docker image build -t knight-moves .
docker container run -p 1337:1337 --rm --name knight-moves-container knight-moves:latest