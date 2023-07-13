---
layout: default
---


<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}

  <div>
    <h2>About me</h2>
    <p>
My name is Emilio, I am a PhD student in statistics applied to computational
immunology; in other words, I use mathematics and computers to study how the
body fights diseases. My PhD is broadly focused on finding better ways to design
a particular kind of vaccines (<a href="{% post_url 2019-08-16-what_is_my_phd_about %}">read more</a>).
</p>

<p>
Previously, I studied computer science and data science, and I have a minor
degree in innovation & entrepreneurship. I also have experience in the industry
as a software developer, web developer, data engineer, data scientist, and
consulting.
</p>

  </div>

  <div class="bot-margin">
      <h2> I write about </h2>
      {% for category in site.categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <button class="category">
      <a
         href="{{ site.baseurl }}/categories#{{ category_name | slugize }}">
      {{ category_name }}
      </a>
      </button>
      {% endfor %}
  </div>

  <div class="bot-margin">
    <h2>Recent News</h2>
    <div class="news-list">
        {% for n in site.data.news limit:3 %}
        <div class="news-item">
            <div class="news-text-container">
            <p class="news-text"> {{ n.text }} </p>
            </div>
            <p class="news-date"> {{ n.date | date: site.date_format }} </p>
        </div>
        {% endfor %}
    </div>
    <p style="text-align:right"><a href="/news/">See all</a></p>
  </div>

  <div class="latest">
    <h2 class="post-list-heading">All posts</h2>
    <ul class="post-list">
      {%- for post in site.posts -%}
        <li>
          <span class="post-meta">{{ post.date | date: site.date_format }}</span>
          <h3>
            <a class="post-link" href="{{ post.url | relative_url }}">
              {{ post.title | escape }}
            </a>
          </h3>
          {%- if site.show_excerpts -%}
              {{ post.excerpt | strip_html }}
          {%- endif -%}
        </li>
      {%- endfor -%}
    </ul>
    <!-- <a href="/posts">View all posts</a> -->
  </div>

</div>
