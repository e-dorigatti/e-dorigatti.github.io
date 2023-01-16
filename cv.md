---
title: "Curriculum Vitae"
layout: post
markdown: kramdown
---

Download as [PDF](/attachments/CV-Emilio-Dorigatti.pdf)

{% for image in site.static_files %}
{% if image.path contains '/images/cv/' %}
<img class="center-image" border="1px solid gray" src="{{ image.path }}" alt="cv page" />
{% endif %}
{% endfor %}
