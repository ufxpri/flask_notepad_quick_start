function new_memo(title, category, favorite, content) {
    var xhr = new XMLHttpRequest();
    var data = {
        meta: {
            title: title,
            category: category,
            favorite: favorite,
        },
        content: content
    };
    xhr.onload = function () {
        if (xhr.status === 200 || xhr.status === 201) {
            console.log(xhr.responseText);
            window.location.href='/list';
        } else {
            console.error(xhr.responseText);
        }
    };
    xhr.open('POST', '/memo');
    xhr.setRequestHeader('Content-Type', 'application/json'); // 컨텐츠타입을 json으로
    xhr.send(JSON.stringify(data)); // 데이터를 stringify해서 보냄
}

function delete_memo(id) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () { // 요청에 대한 콜백
        if (xhr.readyState === xhr.DONE) { // 요청이 완료되면
            if (xhr.status === 200 || xhr.status === 201) {
                console.log(xhr.responseText);
                window.location.href='/list';
            } else {
                console.error(xhr.responseText);
            }
        }
    };
    xhr.open('DELETE', '/memo?id='+id); // 메소드와 주소 설정
    xhr.send(); // 요청 전송 
    // xhr.abort(); // 전송된 요청 취소
}

function edit_memo(id, title, category, favorite, last_edit, created_time, content) {
    var xhr = new XMLHttpRequest();
    var data = {
        id: id,
        meta: {
            title: title,
            category: category,
            favorite: favorite,
            last_edit: last_edit,
            created_time: created_time
        },
        content: content
    };
    xhr.onload = function () {
        if (xhr.status === 200 || xhr.status === 201) {
            console.log(xhr.responseText);
        } else {
            console.error(xhr.responseText);
        }
    };
    xhr.open('PUT', '/memo');
    xhr.setRequestHeader('Content-Type', 'application/json'); // 컨텐츠타입을 json으로
    xhr.send(JSON.stringify(data)); // 데이터를 stringify해서 보냄
}