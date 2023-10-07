.PHONY: build serve tags install

ENV=./.venv/

serve: build ${ENV}
	conda run --prefix ${ENV} --live-stream bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

build: images/cv/cv1.png images/cv/cv2.png update ${ENV}
	rm -rf _site
	conda run --prefix ${ENV} --live-stream bundle exec jekyll build

## NB - two-pages CV
images/cv/cv1.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pdf-page=1 --export-filename images/cv/cv1.png

images/cv/cv2.png: attachments/CV-Emilio-Dorigatti.pdf
	inkscape attachments/CV-Emilio-Dorigatti.pdf --pdf-poppler --export-text-to-path --export-background=white --export-background-opacity=1 --export-dpi=150 --pdf-page=2 --export-filename images/cv/cv2.png

update: ${ENV}
	# nb - in case of error, make sure that bundle is installed in ./venv/
	conda run --prefix ${ENV} --live-stream bundle install
	conda run --prefix ${ENV} --live-stream bundle update

${ENV}:
	conda env create --file environment.yaml --prefix ${ENV}
