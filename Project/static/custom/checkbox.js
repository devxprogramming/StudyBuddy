const checkBox = document.getElementById('checkBox')
const username = document.getElementById('username')
const passwordField = document.getElementById('password')
const confirmField = document.getElementById('confirm')
const helpId = document.getElementById('helpId')

const id_password2 = document.getElementById('id_password2')
const id_password1 = document.getElementById('id_password1')



checkBox.addEventListener('click', () =>{
    if(passwordField.type === 'password'){
        passwordField.type = "text"
        confirmField.type = "text"
        id_password1.type = 'text'
        id_password2.type = 'text'
    } else{
        passwordField.type = 'password'
        confirmField.type = 'password'
        id_password1.type = 'password'
        id_password2.type = 'password'
    }
})
