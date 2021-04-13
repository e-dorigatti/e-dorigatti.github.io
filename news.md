---
layout: page
permalink: /news/
title: News
---

<ul>
{% for n in site.data.news %}
<li>
    <p> "{{ n.text }}" - {{ n.date | date: site.date_format }} </p>
</li>
{% endfor %}
</ul>

