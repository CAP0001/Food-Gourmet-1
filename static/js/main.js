const btn = document.getElementById('filterBtn');
const content = document.getElementById('filterContent');

btn.addEventListener('click', (e) => {
    content.classList.toggle('show');
    e.stopPropagation(); 
});

content.addEventListener('click', (e) => {
    e.stopPropagation();
});
window.addEventListener('click', () => {
    if (content.classList.contains('show')) {
        content.classList.remove('show');
        
        const allDetails = content.querySelectorAll('details');
        allDetails.forEach(details => {
            details.removeAttribute('open');
        });
    }
});