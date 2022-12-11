var score = 0;

function highlightImage(img, img_type, option, finish=false) {
    // console.log("HERE");
    // Skip if already coloured
    if (img.style.opacity == 0.4) return score;
    // console.log("HERE");
    // If image was clicked, we want image to match prompt. Otherwise it's the opposite
    let correct = (img_type == option);
    if (finish) correct = !correct;
    let colour = "red";
    if (correct) colour = "green";

    // Update Score and set colour
    score += correct * 1;
    img.style.background = colour;
    img.style.opacity = 0.4;
    return score;
  }

function nextOption(){
    // Send an AJAX request to the server
    var xhr = new XMLHttpRequest();
        xhr.open('GET', '/quiz?continuation=yes');
        xhr.onload = function() {
            // document.getElementById('next-button').hidden = false;
            // document.getElementById('finish-button').hidden = true;
            window.location.reload();
        }
        xhr.send();
}


function finish(images, option='TEM') {
    let overlays = document.getElementsByClassName('overlay');

    for (var i = 0; i < overlays.length; i++) {
        console.log(images[i][0]);
        highlightImage(overlays[i], images[i][0], option, finish=true);
      };
    
    if (score >= 7) document.getElementById('response').hidden = false;

    document.getElementById('next-button').hidden = false;
    document.getElementById('finish-button').hidden = true;
}