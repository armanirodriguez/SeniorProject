const songContainer = document.getElementById('song_scroll');
const songContainerWidth = songContainer.scrollWidth;

window.addEventListener('load', () => {
    self.setInterval(() => {
      songContainer.scrollLeft += 50;
    }, 15);
  });