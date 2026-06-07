document.addEventListener('DOMContentLoaded', function() {
    const langBtn = document.querySelector('.lang-dropbtn');
    const langContent = document.querySelector('.lang-dropdown-content');
    const langDropdown = document.querySelector('.lang-dropdown');

    // Безопасный клик для переключателя языков
    if (langBtn && langContent) {
        langBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation(); // Предотвращаем мгновенное закрытие через window
            console.log("Клик по переключателю языков!");
            
            langContent.classList.toggle('show');
            
            // Если используется класс для поворота стрелочки
            if (langDropdown) {
                langDropdown.classList.toggle('active');
            }
        });
    }

    // Закрытие языкового меню при клике в любую другую область экрана
    window.addEventListener('click', function() {
        if (langContent && langContent.classList.contains('show')) {
            console.log("Клик вне меню языков -> закрываем");
            langContent.classList.remove('show');
            
            if (langDropdown) {
                langDropdown.classList.remove('active');
            }
        }
    });
});