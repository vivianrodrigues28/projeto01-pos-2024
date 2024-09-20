document.addEventListener('DOMContentLoaded', function() {
    const profileSection = document.getElementById('profile-section');
    const loginSection = document.getElementById('login-section');
    const boletinsSection = document.getElementById('boletins-section');
    const fetchBoletinsBtn = document.getElementById('fetch-boletins');
    const boletinsList = document.getElementById('boletins-list');

    // Simular autenticação e exibição do perfil
    const userLoggedIn = false;  // Troque para "true" após autenticação real

    if (userLoggedIn) {
        loginSection.classList.add('hidden');
        profileSection.classList.remove('hidden');
        boletinsSection.classList.remove('hidden');

        // Simular dados do perfil
        document.getElementById('user-name').textContent = 'João Silva';
        document.getElementById('profile-photo').src = 'https://via.placeholder.com/150';
    } else {
        loginSection.classList.remove('hidden');
        profileSection.classList.add('hidden');
        boletinsSection.classList.add('hidden');
    }

    // Simular busca de boletins
    fetchBoletinsBtn.addEventListener('click', function() {
        const year = document.getElementById('year').value;
        const semester = document.getElementById('semester').value;

        if (!year || !semester) {
            alert('Por favor, insira ano e semestre!');
            return;
        }

        // Simular resposta de boletins
        const boletins = [
            { disciplina: 'Matemática', nota: 8.5 },
            { disciplina: 'História', nota: 7.3 },
            { disciplina: 'Física', nota: 9.0 }
        ];

        boletinsList.innerHTML = '';  // Limpar lista
        boletins.forEach((boletim) => {
            const boletimCard = document.createElement('div');
            boletimCard.classList.add('boletim-card');
            boletimCard.innerHTML = `
                <h3>${boletim.disciplina}</h3>
                <p>Nota: ${boletim.nota}</p>
            `;
            boletinsList.appendChild(boletimCard);
        });
    });
});
