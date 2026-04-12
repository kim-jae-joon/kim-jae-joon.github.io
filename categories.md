---
layout: categories
title: "📚 언어별 강의 목록"
author_profile: true
permalink: /categories/
---

<!-- 전체 보기 버튼 -->
<div style="margin-bottom: 20px; text-align: right;">
  <button id="show-all-btn" class="btn btn--primary">전체 강의 다시 보기</button>
</div>

<!-- 카테고리 필터링 JS -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  // 카테고리 링크들 (상단 메뉴)
  const categoryLinks = document.querySelectorAll('.taxonomy__index a');
  // 카테고리 본문 섹션들
  const categorySections = document.querySelectorAll('.taxonomy__section');
  const showAllBtn = document.getElementById('show-all-btn');

  // 카테고리 클릭 시 필터링 수행
  categoryLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault(); // 화면 아래로 내려가는 기본 동작 방지

      // 1. 모든 섹션 숨기기
      categorySections.forEach(section => {
        section.style.display = 'none';
      });

      // 2. 선택된 섹션만 보이기
      let targetId = this.getAttribute('href').substring(1);
      
      // 한글 URL 인코딩 처리
      try {
        targetId = decodeURIComponent(targetId);
      } catch(e) {}
      
      const targetSection = document.getElementById(targetId);
      if(targetSection) {
        targetSection.style.display = 'block';
      }
    });
  });

  // '전체 보기' 버튼 동작
  if(showAllBtn) {
    showAllBtn.addEventListener('click', function() {
      categorySections.forEach(section => {
        // 기존 CSS 흐름으로 복구
        section.style.display = 'block';
      });
    });
  }
});
</script>
