let closeBtn = document.querySelector(".fa.fa-close")
let linksMedia = document.querySelector(".links-media")
let menu = document.querySelector(".fa-solid.fa-bars")


menu.addEventListener("click", () => {
    linksMedia.style.marginLeft = "0%"
})
closeBtn.addEventListener("click", () => {
    linksMedia.style.marginLeft = "-500%"
})


