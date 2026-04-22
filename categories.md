---
layout: categories
title: "전체 카테고리 목록"
author_profile: false
permalink: /categories/
---

<div id="empty-message" style="display: none; text-align: center; padding: 50px; color: #888;">
  <h3>아직 작성된 글이 없습니다.</h3>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const categorySections = document.querySelectorAll('.taxonomy__section');
  const taxonomyIndex = document.querySelector('.taxonomy__index');
  const emptyMessage = document.getElementById('empty-message');
  const pageTitle = document.querySelector('.page__title');

  // 그룹 정의 (navigation.yml의 해시값과 매칭)
  const groups = {
    'ai': ['algorithm', 'c-lang', 'csharp', 'rust', '파이썬'],
    'posting': ['ai-성능-비교', 'development']
  };

  function filter() {
    let hash = window.location.hash.substring(1);
    try { hash = decodeURIComponent(hash); } catch(e) {}

    if (hash) {
      if (taxonomyIndex) taxonomyIndex.style.display = 'none';
      let found = false;
      const isGroup = groups.hasOwnProperty(hash);
      const targets = isGroup ? groups[hash] : [hash];

      categorySections.forEach(sec => {
        const id = sec.id.toLowerCase();
        const match = targets.some(t => id === t.replace(/ /g, '-').toLowerCase());
        if (match) {
          sec.style.display = 'block';
          found = true;
        } else {
          sec.style.display = 'none';
        }
      });

      if (pageTitle) pageTitle.innerText = isGroup ? " 그룹 전체 보기" : " " + hash.toUpperCase();
      emptyMessage.style.display = found ? 'none' : 'block';
    } else {
      if (taxonomyIndex) taxonomyIndex.style.display = 'block';
      categorySections.forEach(sec => sec.style.display = 'block');
    }
  }

  filter();
  window.addEventListener('hashchange', filter);
});
</script>
