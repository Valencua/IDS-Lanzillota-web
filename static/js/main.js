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

    const editModal = document.getElementById('edit-docente-modal');
    if (editModal) {
        const nombre = document.getElementById('edit-nombre');
        const apellido = document.getElementById('edit-apellido');
        const rol = document.getElementById('edit-rol');

        const openEdit = (btn) => {
            nombre.value = btn.dataset.nombre || '';
            apellido.value = btn.dataset.apellido || '';
            rol.value = btn.dataset.rol || 'Ayudante';
            editModal.classList.add('is-open');
            editModal.setAttribute('aria-hidden', 'false');
        };
        const closeEdit = () => {
            editModal.classList.remove('is-open');
            editModal.setAttribute('aria-hidden', 'true');
        };

        document.querySelectorAll('.js-edit-docente').forEach((btn) => {
            btn.addEventListener('click', () => openEdit(btn));
        });
        editModal.querySelectorAll('[data-close]').forEach((el) => {
            el.addEventListener('click', closeEdit);
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeEdit();
        });
    }
});