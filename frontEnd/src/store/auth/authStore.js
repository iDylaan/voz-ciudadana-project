import { atom, task } from 'nanostores'
import authApi from '@/api/authApi'

const initialUser = {
    email:'',
    username: ''
}

const errors = []
const isLoading = false

export const $User = atom(initialUser)
export const $ErrorsUser = atom(errors)
export const $IsLoadingsUser = atom(isLoading)

export const isLoadingToggle = () =>{
    $IsLoadingsUser.set(!$IsLoadingsUser.get())
}

export const updateErrors = (error) =>{
    $ErrorsUser.set([...$ErrorsUser.get(), error])
}

export const cleanErrors = () =>{
    $ErrorsUser.set([])
}

export const updateUser = (user) =>{
    $User.set(user)
}

export const logOut = () =>{
    $User.set(initialUser)
}

export const userLogin = (user) =>{
    task(async()=>{
        isLoadingToggle()
        cleanErrors()
        try {
            const res = await authApi.post('/auth/login', user)

            const {access_token, nombre, email} = res.data

            const newUser = {
                username: nombre,
                email: email
            }

            localStorage.setItem('token', access_token)
            updateUser(newUser)
            window.location.href = '/home'

            cleanErrors()
            
        } catch (error) {
            updateErrors(error.response.data.messgae)

        }finally{
            isLoadingToggle()
        }

    })
}

export const userRegister = (user) =>{
    task(async() =>{
        isLoadingToggle()
        cleanErrors()
        try {
            const res = await authApi.post('/auth/register', user)
            if (res.status == 200) {
                const resLog = await authApi.post('/auth/login', user)
                const {access_token, nombre, email} = resLog.data

                const newUser = {
                    username: nombre,
                    email: email
                }

                localStorage.setItem('token', access_token)
                updateUser(newUser)
                window.location.href = '/home'

                cleanErrors()
            }else{
                throw new Error('Error al iniciar sesion')
            }
        } catch (error) {
            updateErrors(error.response.data.message)
        }finally{
            isLoadingToggle()
        }
    })
}