document.querySelector('.section-header').addEventListener("mousemove", function (e) {
    const bg = document.querySelector('.bg');
    const runner = document.querySelector('.runner');
    const textContent = document.querySelector('.text-content');

    bg.style.width = 100 + e.pageX / 100 + '%';
    bg.style.height = 100 + e.pageX / 100 + '%';
    runner.style.right = 100 + e.pageX / 2 + 'px';
    textContent.style.left = 200 + e.pageX / 2.5 + 'px';
})