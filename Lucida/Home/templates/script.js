document.addEventListener('DOMContentLoaded', function() {
    const logoImg = document.querySelector('.image');
    const textSpans = document.querySelectorAll('.logo span');
  
    setTimeout(() => {
      logoImg.classList.add('rotate');
      textSpans.forEach((span, index) => {
        setTimeout(() => {
          span.classList.add('fade-out');
        }, (index + 1) * 100);
      });
    }, 1000); // Rotate logo after 3 seconds
  });
  