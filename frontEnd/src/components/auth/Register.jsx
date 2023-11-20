
import '../../assets/css/auth.css'
import logo from '../../assets/img/logo.svg'
import { useForm  } from "react-hook-form"
import { useStore } from '@nanostores/react'
import { $ErrorsUser, $IsLoadingsUser, userRegister } from '../../store/auth/authStore'
import { useEffect } from 'react'
import { useMessage } from '@/react/hooks/useMessage'

export const Register = () => {

  const {register, handleSubmit, formState:{errors}, getValues } = useForm()
  const error = useStore($ErrorsUser)
  const isLoading = useStore($IsLoadingsUser)
  const { errorMessage } = useMessage(error)

  const onSubmit = (data) => {
      userRegister(data)
  };

    useEffect(() => {

        errorMessage()
    
    }, [error]);
    
  return (
    <>
    <img src={logo.src} width="100" height="100" />
    <h1>Iniciar Sesion</h1>
    <form onSubmit={handleSubmit(onSubmit)}>

        <input type="text" placeholder="Nombre del usuario" {...register('username',{
          required: 'El nombre es requerido'
        })} />

        {
            errors.username && 
            <p>{errors.username.message}</p>
        }

        <input type="text"  placeholder="Email" {...register('email', {
                required: 'El email es requerido', 
                pattern: {
                    value:/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i, 
                    message:'No es un correo valido'}
                }   
            )} 
        />

        {
            errors.email && 
            <p>{errors.email.message}</p>
        }
        
        <input type="password"  placeholder="Password" {
            ...register('password', {
                        required: 'La contraseña es requerida',
                        minLength:{
                            value: 8,
                            message: 'La contraseña tiene que contener minimo 8 caracteres'
                        }
                    }
                )
            }
        />
      
        {
            errors.password && 
            <p>{errors.password.message}</p>
        }

        <input type="password"  placeholder="Password" {
            ...register('password2', {
                  required: 'La contraseña de confimacion es requerida',
                  validate: (val) => {
                    const {password} = getValues()
                    return password === val || "Las contraseñas no coinciden";
                  }
                }
        )}/>

        {
          errors.password2 && 
          <p>{errors.password2.message}</p>
        }

        <input type="submit" value="Iniciar Sesion" disabled={isLoading ? true : false} />

    </form>
    <p>No tienes cuenta?, <a href="/auth/login">Inicia Sesion</a></p>
      
    </>
  )
}
