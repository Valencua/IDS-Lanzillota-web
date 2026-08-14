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
        const email = document.getElementById('edit-email');
        const form = document.getElementById('edit-docente-form');
        const openEdit = (btn) => {
            nombre.value = btn.dataset.nombre || '';
            apellido.value = btn.dataset.apellido || '';
            rol.value = btn.dataset.rol || 'Ayudante';
            email.value = btn.dataset.email || '';
            if (form) {
                form.action = btn.dataset.editUrl || '#';
            }
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

    const deleteModal = document.getElementById('delete-docente-modal');
    if (deleteModal) {
        const deleteName = document.getElementById('delete-docente-nombre');
        const deleteForm = document.getElementById('delete-docente-form');

        const openDelete = (btn) => {
            const nombre = [btn.dataset.nombre, btn.dataset.apellido].filter(Boolean).join(' ');
            if (deleteName) deleteName.textContent = nombre || 'este docente';
            if (deleteForm) deleteForm.action = btn.dataset.deleteUrl || '#';
            deleteModal.classList.add('is-open');
            deleteModal.setAttribute('aria-hidden', 'false');
        };
        const closeDelete = () => {
            deleteModal.classList.remove('is-open');
            deleteModal.setAttribute('aria-hidden', 'true');
        };

        document.querySelectorAll('.js-delete-docente').forEach((btn) => {
            btn.addEventListener('click', () => openDelete(btn));
        });
        deleteModal.querySelectorAll('[data-close]').forEach((el) => {
            el.addEventListener('click', closeDelete);
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeDelete();
        });
    }
    const claseModal = document.getElementById('edit-clase-modal');
    if (claseModal) {
        const fecha = document.getElementById('edit-fecha');
        const tipo = document.getElementById('edit-tipo');
        const titulo = document.getElementById('edit-titulo');
        const contenidos = document.getElementById('edit-contenidos');
        const hito = document.getElementById('edit-hito');

        const openClase = (btn) => {
            fecha.value = btn.dataset.fecha || '';
            tipo.value = btn.dataset.tipo || 'Virtual';
            titulo.value = btn.dataset.titulo || '';
            contenidos.value = (btn.dataset.contenidos || '').split(' || ').join('\n');
            hito.value = btn.dataset.hito || '';
            claseModal.classList.add('is-open');
            claseModal.setAttribute('aria-hidden', 'false');
        };
        const closeClase = () => {
            claseModal.classList.remove('is-open');
            claseModal.setAttribute('aria-hidden', 'true');
        };

        document.querySelectorAll('.js-edit-clase').forEach((btn) => {
            btn.addEventListener('click', () => openClase(btn));
        });
        claseModal.querySelectorAll('[data-close]').forEach((el) => {
            el.addEventListener('click', closeClase);
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeClase();
        });
    }
});