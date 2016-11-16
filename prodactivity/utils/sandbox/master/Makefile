.PHONY: all build publish run

registry := "docker-registry.pdbld.f5net.com"
namespace := "sandbox"
date := $(shell date +"%Y%m%d")
img_name := "bbot-master"
img := $(registry)/$(namespace)/$(img_name)
nfs_uid := 10007
bbot_ui_port := 8010
bbot_pb_port := 9989
gitlab_host := "bldr-git.int.lineratesystems.com"
gitlab_ssh_port := 22

all: build publish

build:
	@echo "building image $(img):$(date) ..."
	docker build \
		-t $(img):$(date) \
		--build-arg NFS_UID=$(nfs_uid) \
		--build-arg BBOT_UI_PORT=$(bbot_ui_port) \
		--build-arg BBOT_PB_PORT=$(bbot_pb_port) \
		--build-arg GITLAB_HOST=$(gitlab_host) \
		--build-arg GITLAB_SSH_PORT=$(gitlab_ssh_port) \
		.

publish:
	@echo "publishing image $(img):$(date) ..."
	docker tag $(img):$(date) $(img):latest
	docker push $(img)
