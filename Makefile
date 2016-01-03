ARTIFACT_NAME="nickw444/mediabrowser"
build:
	docker build --rm -t $(ARTIFACT_NAME) .
push:
	docker push  $(ARTIFACT_NAME)

