document.addEventListener('DOMContentLoaded', ()=> {
    document.querySelector('.report').addEventListener('mouseover', ()=>{
        document.querySelector('#reportmessage').innerHTML = "Report user"
    })
    document.querySelector('.report').addEventListener('mouseout', ()=>{
        document.querySelector('#reportmessage').innerHTML = ""
    })
})