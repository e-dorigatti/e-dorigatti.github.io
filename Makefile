.PHONY: build serve tags

## NB - two-pages CV
images/cv/cv1.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pdf-page=1 --export-filename images/cv/cv1.png

images/cv/cv2.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pdf-page=2 --export-filename images/cv/cv2.png

build: images/cv/cv1.png images/cv/cv2.png
	rm -rf _site
	bundle exec jekyll build

serve: build
	bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

update:
	bundle install
	bundle update
