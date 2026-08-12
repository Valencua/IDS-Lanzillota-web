document.addEventListener('DOMContentLoaded', function () {
    const card = document.getElementById('whatsapp-card');
    const modal = document.getElementById('whatsapp-modal');
    if (card && modal) {
        const open = (e) => {
            e.preventDefault();
            modal.classList.add('is-open');
            modal.setAttribute('aria-hidden', 'false');
        };
        const close = () => {
            modal.classList.remove('is-open');
            modal.setAttribute('aria-hidden', 'true');
        };
        card.addEventListener('click', open);
        modal.querySelectorAll('[data-close]').forEach((el) => el.addEventListener('click', close));
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    }
    
    const csv = document.getElementById('csv');
    const csvName = document.getElementById('csv-name');
    if (csv && csvName) {
        csv.addEventListener('change', function () {
            csvName.textContent = this.files[0] ? this.files[0].name : '';
        });
    }
});