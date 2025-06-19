document.addEventListener("DOMContentLoaded", () => {
  const cards = [...document.querySelectorAll("#blogGrid > div")];
  const postsPerPage = 4;
  let currentIndex = 0;

  function showNext() {
    for (let i = currentIndex; i < currentIndex + postsPerPage; i++) {
      if (cards[i]) cards[i].style.display = "block";
    }
    currentIndex += postsPerPage;
    if (currentIndex >= cards.length) {
      document.getElementById("loadMoreBtn").style.display = "none";
    }
  }

  cards.forEach(c => c.style.display = "none");
  showNext();

  document.getElementById("loadMoreBtn").addEventListener("click", showNext);

  // Search
  document.getElementById("searchInput").addEventListener("input", e => {
    const keyword = e.target.value.toLowerCase();
    cards.forEach(card => {
      card.style.display = card.innerText.toLowerCase().includes(keyword) ? "block" : "none";
    });
  });

  // Filter
  document.querySelectorAll(".category-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const cat = btn.dataset.category;
      cards.forEach(card => {
        card.style.display = (cat === "all" || card.dataset.category === cat) ? "block" : "none";
      });
    });
  });
});
