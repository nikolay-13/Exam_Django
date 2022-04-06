function show_filters() {
    let filter_display = document.getElementById('filter-funcs')
    if (filter_display.style.display === 'grid') {
        filter_display.style.display = 'none';

    } else {
        filter_display.style.display = 'grid';
    }
}

function show_product_det(id) {
    let product_pic = document.getElementById(`img${id}`)
    let description = document.getElementById(`item-description${id}`)
    let thumbnail_text = document.getElementById(`thumbnail-text${id}`)
    product_pic.style.display = 'none';
    thumbnail_text.style.display = 'none';
    description.style.display = 'grid';

}

function hide_product_det(c_id) {
    let product_pic = document.getElementById(`img${c_id}`)
    let description = document.getElementById(`item-description${c_id}`)
    let thumbnail_text = document.getElementById(`thumbnail-text${c_id}`)
    description.style.display = 'none';
    product_pic.style.display = 'block';
    thumbnail_text.style.display = 'block';
}

function welcome(){
    let banner = document.getElementById('banner')
    banner.style.display = 'block'
}

function close_banner(){
    let main_content = document.getElementById('main-page')
    let banner = document.getElementById('banner')
    banner.style.display = 'none';
    main_content.style.display = 'flex';
}

