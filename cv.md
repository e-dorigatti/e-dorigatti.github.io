---
title: "Curriculum Vitae"
layout: post
markdown: kramdown
---

Download as [PDF](/attachments/CV-Emilio-Dorigatti.pdf)

Note: I am graduating soon and <b>looking for a job</b> as a Senior Data Scientist
in the greater Munich metropolitan area or remotely starting in September or
later.
If interested, feel free to contact me!

{% for image in site.static_files %}
{% if image.path contains '/images/cv/' %}
<img class="center-image" border="1px solid gray" src="{{ image.path }}" alt="cv page" />
{% endif %}
{% endfor %}
