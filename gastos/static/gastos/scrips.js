document.addEventListener('DOMContentLoaded', function () {
    // Animación de aparición inicial
    document.querySelectorAll('.animate-fade-in-up, .animate-fade-in-down, .animate-fade-in-left, .animate-fade-in-right, .animate-pop')
        .forEach(function(el, idx) {
            el.style.animationDelay = (el.style.animationDelay || '') || (0.05 * idx) + 's';
        });

    // Validación y feedback en el formulario
    const form = document.getElementById('gastoForm');
    const msg = document.getElementById('form-message');
    if (form && msg) {
        form.addEventListener('submit', function (e) {
            const descripcion = form.descripcion.value.trim();
            const monto = parseFloat(form.monto.value);
            if (!descripcion || isNaN(monto) || monto <= 0) {
                e.preventDefault();
                msg.textContent = "Por favor escribe una descripción válida y un monto mayor a 0.";
                msg.style.color = "#d32f2f";
                return false;
            } else {
                msg.textContent = "¡Gasto registrado con éxito!";
                msg.style.color = "#43a047";
                setTimeout(()=>{ msg.textContent = ""; }, 2500);
            }
        });
    }
});