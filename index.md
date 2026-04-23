---
layout: single
title: "개발자 김재준의 블로그"
sidebar:
  nav: "category_nav"
---

{% for category in site.categories %}
  {% assign cat_name = category[0] %}
  {% assign cat_posts = category[1] %}
  
  <h2 class="archive__subtitle" style="margin-top: 2em; border-bottom: 2px solid #f2f2f2; padding-bottom: 10px;">
    <a href="/categories/#{{ cat_name | slugify }}" style="text-decoration: none; color: #333;">
      📂 {{ cat_name }}
    </a>
  </h2>

  <div class="entries-list">
    {% for post in cat_posts limit:3 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>
  
  <div style="text-align: right; margin-bottom: 3em;">
    <a href="/categories/#{{ cat_name | slugify }}" style="font-size: 0.9em; color: #007bff; font-weight: bold;">
      {{ cat_name }} 글 더보기 &rarr;
    </a>
  </div>
{% endfor %}
