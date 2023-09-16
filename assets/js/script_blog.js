function set_value(id) {
    document.getElementById('parent_id').value = id;
    var name = document.getElementById('full_name')
    textarea = $('#message')[0];
    textarea.placeholder = 'reply to ' + name.innerText;
    window.location.href = '#message';
}

function like(slug) {
    var element_like = document.getElementById('like')
    var likes = document.getElementById('like_count')
    var dislikes = document.getElementById('dislike_count')
    var element_dislike = document.getElementById('dislike')
    $.get(`/blogs/postlike/${slug}`).then(response => {
        if (response['response'] === 'liked') {
            element_like.className = 'fa fa-thumbs-up'
            if (element_dislike.className === 'fa fa-thumbs-down') {
                element_dislike.className = 'fa fa-thumbs-o-down'
                dislikes.innerText = Number(dislikes.innerText) - 1
            }
            likes.innerText = Number(likes.innerText) + 1


        } else {
            element_like.className = 'fa fa-thumbs-o-up'
            likes.innerText = Number(likes.innerText) - 1

        }
    })
}

function dislike(slug) {
    var element_like = document.getElementById('like')
    var likes = document.getElementById('like_count')
    var dislikes = document.getElementById('dislike_count')
    var element_dislike = document.getElementById('dislike')
    $.get(`/blogs/postdislike/${slug}`).then(response => {
        if (response['response'] === 'dislike') {
            element_dislike.className = 'fa fa-thumbs-down'
            if (element_like.className === 'fa fa-thumbs-up') {
                element_like.className = 'fa fa-thumbs-o-up'
                likes.innerText = Number(likes.innerText) - 1
            }
            dislikes.innerText = Number(dislikes.innerText) + 1
        } else {
            element_dislike.className = 'fa fa-thumbs-o-down'
            dislikes.innerText = Number(dislikes.innerText) - 1
        }


    })
}

function search_value(querry) {
    var element = document.getElementById('search_bar')
    element.placeholder = querry



}