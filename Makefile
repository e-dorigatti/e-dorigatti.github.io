.PHONY: build serve tags install docker-build-dev docker-run-dev docker-build-prod docker-run-prod update

docker-run-dev: docker-build-dev
	docker run -it --rm -p 4000:4000 -v $$(pwd):/app/blog e-dorigatti.github.io/blog/dev #/bin/bash

docker-build-dev:
	docker build -t e-dorigatti.github.io/blog/dev --target dev .

docker-run-prod: docker-build-prod
	docker run -p 4000:4000 e-dorigatti.github.io/blog/prod

docker-build-prod:
	docker build -t e-dorigatti.github.io/blog/prod --target prod .

serve: build
	bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

build:
	rm -rf _site
	bundle exec jekyll build

update:
	bundle install
	bundle update
