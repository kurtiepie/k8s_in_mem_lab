#Start Minikube
MINIKUBE_MEM ?=2048
MINIKUBE_CPU ?=4

##
## Start minikube
##

launch-minikube: ## Launch Minikube
	minikube start --memory=${MINIKUBE_MEM} --cpus=${MINIKUBE_CPU} --driver hyperkit

deploy:  ## Deploy Lab
	@echo "Creating Lab"
	@kubectl create ns frontend
	@kubectl create ns backend
	@kubectl apply -n frontend -f frontend-deployment.yaml
	@kubectl apply -n frontend -f frontend-nodeport-service.yaml
	@kubectl apply -n backend -f backend-postgres-deployment.yaml
	@kubectl apply -n backend -f  backend-postgres-service.yaml
	@kubectl apply -n backend -f backend-rolebinding-clusteradmin.yaml

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
