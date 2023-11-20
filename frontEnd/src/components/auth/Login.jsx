import logo from '@/img/logo.svg'
import '@/css/auth.css'
import { useForm  } from "react-hook-form"
import { $ErrorsUser, $IsLoadingsUser, userLogin } from '@/store/auth/authStore'
import { useStore } from '@nanostores/react'

import { useEffect } from 'react'
import { useMessage } from '@/react/hooks/useMessage'


const data = {
    email:'',
    password:''
}

export const Login = () => {

    const {register, handleSubmit, formState:{errors} } = useForm(data)
    const error = useStore($ErrorsUser)
    const isLoading = useStore($IsLoadingsUser)
    const { errorMessage } = useMessage(error)

    const onSubmit = (data) => {
        userLogin(data)
    };

    useEffect(() => {

        errorMessage()
        
    }, [error]);

  return (
    <>
        <img src={logo.src} width="150" height="150" />
        <h1>Registro</h1>
        <form onSubmit={handleSubmit(onSubmit)}>
            
            <input type="text"  placeholder="Email" {...register('email', {
                    required: 'El email es requerido', 
                    pattern: {
                        value:/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i, 
                        message:'No es un correo valido'}
            })}/>

            {
                errors.email && 
                <p>{errors.email.message}</p>
            }
            
            <input type="password"  placeholder="Password" {
                ...register('password', {
                            required: 'La contraseña es requerida',
                    }
            )}/>
            
            {
                errors.password && 
                <p>{errors.password.message}</p>
            }

            <input type="submit" value="Iniciar Sesion" disabled={isLoading ? true : false} />

        </form>
        <p>No tienes cuenta?, <a href="/auth/register">Registrate</a></p>
    </>
  )
}

