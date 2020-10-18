async function addArticle(event) {
    event.preventDefault();
    let response = await makeRequest(BASE_API_URL + 'article/create/', 'POST', {
        title: document.getElementById('id_title').value,
        text: document.getElementById('id_text').value
    });
    console.log("csdcsdcsd");
    let data = await response.json();
    console.log(data);
    window.location.href = `${BASE_URL}article/${data.id}/`;
}


window.addEventListener('load', function() {
    const form = document.forms['article_create_form'];
    form.onsubmit = addArticle;
});
