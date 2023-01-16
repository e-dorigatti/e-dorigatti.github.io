.PHONY: build serve tags

## NB - two-pages CV
images/cv/cv1.svg: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-plain-svg --pdf-page=1 --export-dpi=300 --export-filename images/cv/cv1.svg

images/cv/cv2.svg: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-plain-svg --pdf-page=2 --export-dpi=300 --export-filename images/cv/cv2.svg

build: images/cv/cv1.svg images/cv/cv2.svg
	rm -rf _site
	bundle exec jekyll build

serve: build
	bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

update:
	bundle install
	bundle update
