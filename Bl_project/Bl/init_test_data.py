from models import *

def init_data():
    tag1 = Tag(name="SQL", description="Tahat")
    tag1.save()

    tag2 = Tag(name="PHP", description="Much Tahat")
    tag2.save()

    status = GameRequestStatus(status="WAITING", message="Waiting for another player...")
    status.save()
    status = GameRequestStatus(status="DEPLOYING", message="Found a player, creating a game")
    status.save()
    status = GameRequestStatus(status="DONE", message="Challenge accepted!")
    status.save()
    status = GameRequestStatus(status="ERROR", message="Sorry... no challenges for you today :(")
    status.save()

    img = Image(docker_name="shassaro/challenge1", description="POC image", level=1, allow_in_game=True, hints=["Try to tahat (not too much tahat)"], goal_description=['tahat','another-tahat'], duration_minutes=60)
    img.save()

    docker_server = DockerServer(name="primary", protocol="http", ip="192.168.2.109", port="4243")
    docker_server.save()

    docker_mgr = DockerManager(name="docker-manager", ip="localhost", port="8000")
    docker_mgr.save()