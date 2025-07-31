.PHONY: build serve tags install docker-build-dev docker-run-dev docker-build-prod docker-run-prod update

docker-build-dev:
	docker build -t e-dorigatti.github.io/blog/dev --target dev .

docker-run-dev: docker-build-dev
	docker run -p 4000:4000 -v $$(pwd):/app/blog e-dorigatti.github.io/blog/dev

docker-build-prod:
	docker build -t e-dorigatti.github.io/blog/prod --target prod .

docker-run-prod: docker-build-prod
	docker run -p 4000:4000 e-dorigatti.github.io/blog/prod

serve: build
	bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

build: #images/cv/cv1.png images/cv/cv2.png update ${ENV}
	rm -rf _site
	bundle exec jekyll build

## NB - two-pages CV
images/cv/cv1.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pages=1 --export-filename images/cv/cv1.png

images/cv/cv2.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pages=2 --export-filename images/cv/cv2.png

update:
	bundle install
	bundle update

