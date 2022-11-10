const songContainer = document.getElementById("song_scroll");
const songContainerWidth = songContainer.scrollWidth;
window.addEventListener('load', () => {
    self.setInterval(() => {
      if(songContainer.scrollLeft <= songContainerWidth){
        songContainer.scrollLeft = songContainer.scrollLeft + 50;
      }
      else{
        songContainer.scrollLeft -= 50;
      }
    }, 50);
  });