function skipAds() {
  // Look for "Skip Ads" button
  const skipBtn = document.querySelector(
    ".ytp-ad-skip-button, .ytp-ad-overlay-close-button"
  );
  if (skipBtn) {
    skipBtn.click();
    console.log("Ad skipped!");
  }

  // Remove overlay ads (small banners)
  const overlay = document.querySelector(".ytp-ad-overlay-container");
  if (overlay) {
    overlay.remove();
    console.log("Overlay ad removed!");
  }
}

// Check every 500ms for ads
setInterval(skipAds, 1000);
