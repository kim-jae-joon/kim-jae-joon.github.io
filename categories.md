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
  const taxonomyIndex = document.querySelector('.taxonomy__index'); // 상단 카테고리 요약 그리드
  const emptyMessage = document.getElementById('empty-message');
  const pageTitle = document.querySelector('.page__title'); // 최상단 큰 제목
  const originalTitle = pageTitle ? pageTitle.innerHTML : "";

  function filterCategory() {
    let targetId = window.location.hash.substring(1);
    
    // 한글 및 띄어쓰기 URL 디코딩
    try { targetId = decodeURIComponent(targetId); } catch(e) {}

    if (targetId) {
      // 1. 상단 '전체 카테고리 요약 그리드(Image 1)' 숨기기 (헷갈림 원인 제거!)
      if (taxonomyIndex) taxonomyIndex.style.display = 'none';
      
      let found = false;
      
      // 2. 클릭한 카테고리와 일치하는 본문만 보이기
      categorySections.forEach(section => {
        // 지킬은 ID를 소문자+하이픈(-)으로 생성합니다. (예: ai-성능-비교)
        if (section.id === targetId || section.id === targetId.toLowerCase()) {
          section.style.display = 'block';
          found = true;
          
          // 페이지의 큰 제목을 클릭한 카테고리 이름으로 예쁘게 변경
          const catName = section.querySelector('h2.archive__subtitle').innerText;
          if (pageTitle) pageTitle.innerText = "📂 " + catName;
        } else {
          section.style.display = 'none';
        }
      });

      // 3. 만약 해당 카테고리에 글이 단 하나도 없다면 안내 메시지 띄우기
      if (!found) {
        emptyMessage.style.display = 'block';
        // 하이픈(-)을 띄어쓰기로 바꿔서 예쁘게 제목 표시
        const cleanTitle = targetId.replace(/-/g, ' '); 
        if (pageTitle) pageTitle.innerText = "📂 " + cleanTitle.toUpperCase();
      } else {
        emptyMessage.style.display = 'none';
      }
      
    } else {
      // 해시가 없을 때 (처음 /categories/ 로 들어왔을 때)
      if (taxonomyIndex) taxonomyIndex.style.display = 'block';
      emptyMessage.style.display = 'none';
      if (pageTitle) pageTitle.innerHTML = originalTitle;
      
      categorySections.forEach(section => {
        section.style.display = 'block';
      });
    }
  }

  // 처음 들어왔을 때 실행
  filterCategory();

  // 좌측 사이드바를 클릭할 때마다 실시간으로 화면 변경
  window.addEventListener('hashchange', filterCategory);
});
</script>
