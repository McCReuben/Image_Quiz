
function highlightImage(img, img_type, option) {
    let colour = "green"
    if (img_type != option) colour = "red"
    img.style.background = colour;
    img.style.opacity = 0.4;
  }