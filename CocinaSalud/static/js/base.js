
/* 
Function to add a class in an element when a different element is mouseover, and to remove
the class when is mouseout 
*/

function mouseOverAndOut(elementListener, elementModify, className){
    elementListener.addEventListener('mouseover', function(){
        elementModify.classList.add(className);
    });

    elementListener.addEventListener('mouseout', function(){
        elementModify.classList.remove(className);
    });
}

// When we hover the social media text, the icon should hover as well, and viceversa
const instagramIcon = document.getElementById('instagram-icon');
const instagramText = document.getElementById('instagram-text');
mouseOverAndOut(instagramIcon, instagramText, 'footer__redes-hover');
mouseOverAndOut(instagramText, instagramIcon, 'footer__redes-hover');

const youtubeIcon = document.getElementById('youtube-icon');
const youtubeText = document.getElementById('youtube-text');
mouseOverAndOut(youtubeIcon, youtubeText, 'footer__redes-hover');
mouseOverAndOut(youtubeText, youtubeIcon, 'footer__redes-hover');

const locationIcon = document.getElementById('location-icon');
const locationText = document.getElementById('location-text');
mouseOverAndOut(locationIcon, locationText, 'footer__redes-hover');
mouseOverAndOut(locationText, locationIcon, 'footer__redes-hover');

const mailIcon = document.getElementById('mail-icon');
const mailText = document.getElementById('mail-text');
mouseOverAndOut(mailIcon, mailText, 'footer__redes-hover');
mouseOverAndOut(mailText, mailIcon, 'footer__redes-hover');