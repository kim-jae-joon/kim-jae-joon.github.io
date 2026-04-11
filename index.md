---
layout: default
---

# 📚 프로그래밍 자동화 강의 목록

<br>

<ul>
  {% for post in site.posts %}
    <li style="margin-bottom: 15px; font-size: 18px;">
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span style="color: gray; font-size: 14px;"> - {{ post.date | date: "%Y-%m-%d" }}</span>
    </li>
  {% endfor %}
</ul>
