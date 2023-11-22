APP=app-aishima
VERSION=0.4
REGISTRY="kvad"

build:  ## Build Docker Image
	@echo "Building Application ${APP}:${VERSION}"
	docker build -t ${APP}:${VERSION} .
	docker tag ${APP}:${VERSION} ${REGISTRY}/${APP}:${VERSION}

push:  ## push image to docker hub
	@echo "Pushing ${REGISTRY}/${APP}:${VERSION} to Dockerhub"
	docker push ${REGISTRY}/${APP}:${VERSION}

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
