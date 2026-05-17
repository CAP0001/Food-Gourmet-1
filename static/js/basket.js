const modal = document.getElementById('confirm-modal');
    const form = document.getElementById('checkout-form');

    function showConfirmModal() {
        modal.style.display = 'flex';
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    function submitCheckout() {
        form.submit();
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }