function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (response) {
        return response.json();
    })
    .then(function(films)  {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for(let i = 0; i < films.length; i++) {
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td'); 
            let tdTitleRus = document.createElement('td'); 
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');


            tdTitle.innerText = films[i].title == films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru; 
            tdYear.innerText = films[i].year;

            let editButton = document.createElement('button');
            editButton.innerText = 'Редактировать';         
            editButton.onclick = function() {
                editFilm(i);
            };
        
            let delButton = document.createElement('button');
            delButton.innerText = 'Удалить';
            delButton.onclick = function() {
                deleteFilm(i, films[i].title_ru);
            };

            tdActions.append(editButton); 
            tdActions.append(delButton);
        
            tr.append(tdTitle);
            tr.append(tdTitleRus);
            tr.append(tdYear);
            tr.append(tdActions);

            tbody.append(tr);
        }
    })
    .catch(function(error) {
        console.error('Error fetching films:', error);
    });
}

function deleteFilm(id, title) {
    if(!confirm(`Вы точно хотите удалить фильм "${title}"?`))
        return;

    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
    .then(function (response) {
        if(response.ok) {
            fillFilmList();
        }
    });
}