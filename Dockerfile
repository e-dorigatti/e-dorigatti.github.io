# --- Base image ---
FROM debian:latest AS base

RUN apt-get update \
    && apt-get install -y ruby ruby-bundler ruby-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock

RUN useradd -m jekylluser \
    && chown -R jekylluser:jekylluser /app

ENV GEM_HOME=/app/.gem/
ENV PATH=$GEM_HOME/bin:$PATH

USER jekylluser

RUN cd /app \
    && gem install bundler \
    && bundle install \
    && bundle update

# --- Development image ---
# blog source should be added as a volume to allow for live updates

FROM debian:latest AS dev

RUN apt-get update \
    && apt-get install -y ruby ruby-bundler \
    && rm -rf /var/lib/apt/lists/*

COPY --from=base /app/.gem /app/.gem

# mount the blog source code as a volume here
WORKDIR /app/blog

ENV GEM_HOME=/app/.gem/
ENV PATH=$GEM_HOME/bin:$PATH

EXPOSE 4000

RUN useradd -m jekylluser \
    && chown -R jekylluser:jekylluser /app
USER jekylluser

CMD bash -c 'rm -rf _site && bundle exec jekyll serve --watch --drafts --future --incremental --port 4000 --host 0.0.0.0'

# --- Production image ---
# blog is embedded in the image and can be served without a volume

FROM debian:latest AS prod

RUN apt-get update \
    && apt-get install -y ruby ruby-bundler \
    && rm -rf /var/lib/apt/lists/*

COPY --from=base /app/.gem /app/.gem

ADD . /app/blog

WORKDIR /app/blog

ENV GEM_HOME=/app/.gem/
ENV PATH=$GEM_HOME/bin:$PATH

RUN useradd -m jekylluser \
    && chown -R jekylluser:jekylluser /app

USER jekylluser

EXPOSE 4000

CMD bundle exec jekyll serve --port 4000 --host 0.0.0.0 --no-watch
