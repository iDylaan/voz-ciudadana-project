<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;
use Symfony\Component\HttpFoundation\Response;
use Tymon\JWTAuth\Facades\JWTAuth;
use Tymon\JWTAuth\Exceptions\JWTException;
use Tymon\JWTAuth\Exceptions\TokenExpiredException;
use Tymon\JWTAuth\Exceptions\TokenInvalidException;



class AuthController extends Controller
{
    public function register(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'username' => 'required|string|max:255',
            'email' => 'required|email|string| unique:users',
            'password' => 'required|string|min:8'
        ]);

        if ($validator->fails()) {
            return response()->json($validator->errors());
        }

        $user = User::create([
            'username' => $request->username,
            'email' => $request->email,
            'password' => $request->password
        ]);

        $token = $user->createToken('auth_token')->plainTextToken;
        return response()
            ->json(['data' => $user, 'access_token' => $token, 'token_type' => 'Bearer',]);
    }


    public function login(Request $request)
    {
        // Creamos un array de credenciales
        $credentials = $request->only('email', 'password');

        // Añadimos el criterio de 'is_active' al array de credenciales
        $credentials['is_active'] = 1;

        // Verificamos que las credenciales sean correctas y que el usuario esté activo
        if (!Auth::attempt($credentials)) {
            return response()
                ->json(['message' => 'No se encontraron las credenciales o la cuenta no está activa'], 401);
        }

        $user = Auth::user();

        try {
            $customClaims = [
                'name' => $user->username,
                'id' => $user->id,
                'admin' => $user->is_admin
            ];
            $token = JWTAuth::fromUser($user, $customClaims);
        } catch (JWTException $e) {
            return response()->json(['error' => 'could_not_create_token'], 500);
        }

        return response()
            ->json([
                'message' => 'Hi ' . $user->username,
                'accessToken' => $token,
                'token_type' => 'Bearer',
                'user' => $user,
            ]);
    }

    // public function logout()
    // {
    //     auth()->user()->tokens()->delete();
    //     return [
    //         'message' => 'You have successfully logged out and the token was successfully delete'
    //     ];
    // }

    public function update_user_profile(Request $request)
    {
        // Validar los datos de entrada
        $validator = Validator::make($request->all(), [
            'user_id' => 'required|exists:users,id',
            'profile_pic' => 'required|integer|between:1,20',
            'profile_banner' => 'required|integer|between:1,14',
            'jwt' => 'required|string'
        ]);

        // Manejo del caso de falla en la validación
        if ($validator->fails()) {
            return response()->json($validator->errors(), Response::HTTP_UNPROCESSABLE_ENTITY);
        }

        $token = $request->input('jwt'); // Capturar el token JWT de la solicitud

        try {
            // Autenticar el usuario con JWT
            $user = JWTAuth::setToken($token)->authenticate();

            if (!$user) {
                return response()->json(['message' => 'Usuario no encontrado'], 404);
            }

            // Verificar que el user_id proporcionado pertenezca al usuario autenticado
            if ($user->id != $request->input('user_id')) {
                return response()->json(['message' => 'No autorizado para actualizar este perfil'], 403);
            }

            // Actualizar el perfil del usuario
            $user->profile_picture = $request->profile_pic;
            $user->profile_banner = $request->profile_banner;
            $user->first_access = 0;
            $user->save();

            // Retornar una respuesta JSON con los datos del perfil actualizado
            return response()->json(['message' => 'Perfil actualizado con éxito', 'user' => $user]);
        } catch (TokenExpiredException $e) {
            return response()->json(['error' => 'token_expired'], Response::HTTP_UNAUTHORIZED);
        } catch (TokenInvalidException $e) {
            return response()->json(['error' => 'token_invalid'], Response::HTTP_UNAUTHORIZED);
        } catch (JWTException $e) {
            return response()->json(['error' => 'token_absent'], Response::HTTP_UNAUTHORIZED);
        }
    }
}
