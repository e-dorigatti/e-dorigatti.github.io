.PHONY: build serve tags install

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

