---
layout: categories
title: "📚 언어별 강의 목록"
author_profile: true
permalink: /categories/
---

<script>
document.addEventListener("DOMContentLoaded", function() {
  const categorySections = document.querySelectorAll('.taxonomy__section');

  function filterCategory() {
    // URL에서 # 뒤의 카테고리 이름 가져오기
    let targetId = window.location.hash.substring(1);
    
    // 한글 URL 인코딩 처리
    try {
      targetId = decodeURIComponent(targetId);
    } catch(e) {}

    if (targetId) {
      // 1. 모든 카테고리 본문 숨기기
      categorySections.forEach(section => {
        section.style.display = 'none';
      });
      
      // 2. 일치하는 카테고리만 보이기
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        targetSection.style.display = 'block';
      }
    } else {
      // 해시가 없을 때(처음 진입 시)는 모두 보이기
      categorySections.forEach(section => {
        section.style.display = 'block';
      });
    }
  }

  // 페이지에 처음 들어왔을 때 실행
  filterCategory();

  // 좌측 사이드바 카테고리 메뉴를 클릭했을 때(URL 해시가 바뀔 때) 즉시 실행
  window.addEventListener('hashchange', filterCategory);
});
</script>
