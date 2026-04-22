---
layout: categories
title: "📚 전체 카테고리 목록"
author_profile: false
permalink: /categories/
---

<div id="empty-message" style="display: none; text-align: center; padding: 60px 0; color: #888;">
  <h3 style="font-size: 1.2em; font-weight: normal;">아직 작성된 게시글이 없습니다. 📝</h3>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const categorySections = document.querySelectorAll('.taxonomy__section');
  const taxonomyIndex = document.querySelector('.taxonomy__index');
  const emptyMessage = document.getElementById('empty-message');
  const pageTitle = document.querySelector('.page__title');
  const originalTitle = pageTitle ? pageTitle.innerHTML : "";

  // 📂 그룹별 하위 카테고리 매핑 설정
  // navigation.yml에 설정된 해시값과 실제 카테고리 ID를 매칭합니다.
  const categoryGroups = {
    'ai': ['algorithm', 'c-언어', 'c', 'rust', '파이썬'],
    'posting': ['ai-성능-비교', 'development']
  };

  function filterCategory() {
    let targetId = window.location.hash.substring(1);
    try { targetId = decodeURIComponent(targetId); } catch(e) {}

    if (targetId) {
      if (taxonomyIndex) taxonomyIndex.style.display = 'none';
      let foundCount = 0;

      // 그룹 전체 보기인지, 단일 카테고리 보기인지 판별
      const isGroup = categoryGroups.hasOwnProperty(targetId);
      const targets = isGroup ? categoryGroups[targetId] : [targetId];

      categorySections.forEach(section => {
        const sectionId = section.id.toLowerCase();
        // 하이픈(-)이나 대소문자 차이 보정 후 체크
        const isMatch = targets.some(t => sectionId === t.toLowerCase() || sectionId === t.replace(/ /g, '-').toLowerCase());

        if (isMatch) {
          section.style.display = 'block';
          foundCount++;
        } else {
          section.style.display = 'none';
        }
      });

      // 제목 변경 및 메시지 처리
      if (foundCount > 0) {
        emptyMessage.style.display = 'none';
        if (pageTitle) {
           const displayTitle = isGroup ? (targetId === 'ai' ? "AI 강의 전체" : "포스팅 전체") : targets[0].toUpperCase();
           pageTitle.innerText = "📂 " + displayTitle;
        }
      } else {
        emptyMessage.style.display = 'block';
        if (pageTitle) pageTitle.innerText = "📂 " + targetId.toUpperCase();
      }
    } else {
      // 초기 상태: 모두 보여줌
      if (taxonomyIndex) taxonomyIndex.style.display = 'block';
      emptyMessage.style.display = 'none';
      if (pageTitle) pageTitle.innerHTML = originalTitle;
      categorySections.forEach(section => section.style.display = 'block');
    }
  }

  filterCategory();
  window.addEventListener('hashchange', filterCategory);
});
</script>
