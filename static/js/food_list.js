document.addEventListener('DOMContentLoaded', function() {
    const filterBtn = document.getElementById('filterBtn');
    const filterContent = document.getElementById('filterContent');
    const countryBtn = document.getElementById('countryBtn');
    const countryContent = document.getElementById('countryContent');

    // Безопасный клик для Filters
    if (filterBtn && filterContent) {
        filterBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log("Клик по Filters!");
            if (countryContent) countryContent.classList.remove('show');
            filterContent.classList.toggle('show');
        });
    }

    // Безопасный клик для Кухни (флагов)
    if (countryBtn && countryContent) {
        countryBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            console.log("Клик по Кухне!");
            if (filterContent) filterContent.classList.remove('show');
            countryContent.classList.toggle('show');
        });
    }

    // Закрытие при клике по экрану
    window.addEventListener('click', function() {
        if (filterContent) filterContent.classList.remove('show');
        if (countryContent) countryContent.classList.remove('show');
    });
});