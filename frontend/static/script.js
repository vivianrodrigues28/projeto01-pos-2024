document.addEventListener('DOMContentLoaded', function() {
    const fetchBoletinsBtn = document.getElementById('fetch-boletins');
    const boletinsList = document.getElementById('boletins-list');

    fetchBoletinsBtn.addEventListener('click', function() {
        const year = document.getElementById('year').value;
        const semester = document.getElementById('semester').value;

        if (!year || !semester) {
            alert('Por favor, insira ano e semestre!');
            return;
        }

        // Aqui você pode fazer a chamada para a rota de boletins e processar a resposta
    });
});
