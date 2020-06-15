.PHONY: build serve tags

build:
	rm -rf _site
	bundle exec jekyll build

serve:
	rm -rf _site
	bundle exec jekyll serve --drafts --future --incremental --host 0.0.0.0

update:
	bundle install
	bundle update
