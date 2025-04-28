document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const slideCounter = document.querySelector('.slide-counter');

    let currentSlide = 0;
    const totalSlides = slides.length;

    // Инициализация слайдера
    function initSlider() {
        slides[currentSlide].classList.add('active');
        updateCounter();
    }

    // Показать следующий слайд
    function nextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % totalSlides;
        slides[currentSlide].classList.add('active');
        updateCounter();
    }

    // Показать предыдущий слайд
    function prevSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        slides[currentSlide].classList.add('active');
        updateCounter();
    }

    // Обновить счетчик слайдов
    function updateCounter() {
        slideCounter.textContent = `Изображение ${currentSlide + 1} из ${totalSlides}`;
    }

    // Обработчики событий для кнопок
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    // Инициализация при загрузке
    initSlider();

    // Добавляем обработчики клавиатуры
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight') {
            nextSlide();
        } else if (e.key === 'ArrowLeft') {
            prevSlide();
        }
    });
});