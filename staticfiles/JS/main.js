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

function like(){
    let like_btn = document.getElementById('liked');
    if (like_btn.style.color === 'black'){
        like_btn.style.color = 'red';
    }
    else {
        like_btn.style.color = 'black';
    }
}


function category(cat){
    let Mens = document.getElementById('mens-cat')
    let Women = document.getElementById('women-cat')
    let Kids  = document.getElementById('kids-cat')
    let subCategories = document.getElementById('categories')
    let catDisplay = document.getElementById('category-text').innerHTML = `${cat}`
    if (subCategories.style.display === 'none'){
        if (cat === 'Men'){
            Women.style.display = 'none';
            Kids.style.display = 'none';
            subCategories.style.display = 'grid';
        }else if (cat === 'Women'){
            Mens.style.display = 'none';
            Kids.style.display = 'none';
            subCategories.style.display = 'grid';
        }else if (cat === 'Kids'){
            Mens.style.display = 'none';
            Women.style.display = 'none';
            subCategories.style.display = 'grid';
        }
    }
    else {
        subCategories.style.display = 'none';
        Mens.style.display = 'block';
        Women.style.display = 'block';
        Kids.style.display = 'block';
    }


}

function searchc(param){
    let category = document.getElementById('category-text')
    category.innerHTML = `${category.innerHTML}/${param}`;
}

function red(){
    let qq = document.getElementById('category-text')
    location.href=`/?q=${qq.innerHTML}`;
}
