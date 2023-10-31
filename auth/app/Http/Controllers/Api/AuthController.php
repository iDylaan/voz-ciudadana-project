<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Validator;
use Symfony\Component\HttpFoundation\Response;
use Tymon\JWTAuth\Facades\JWTAuth;
use Tymon\JWTAuth\Exceptions\JWTException;



class AuthController extends Controller
{
    public function register(Request $request){
        $validator = Validator::make($request->all(),[
            'username' => 'required|string|max:255',
            'email' => 'required|email|string| unique:users',
            'password' => 'required|string|min:8'
        ]);

        if($validator->fails()){
            return response()->json($validator->errors());
        }

        $user = User::create([
            'username' => $request->username,
            'email' => $request->email,
            'password' => $request->password
        ]);

        $token = $user->createToken('auth_token')->plainTextToken;
        return response()
            ->json(['data'=>$user,'access_token'=>$token,'token_type'=> 'Bearer', ]);
    }


    public function login(Request $request){
        // Creamos un array de credenciales
        $credentials = $request->only('email', 'password');
        
        // Añadimos el criterio de 'is_active' al array de credenciales
        $credentials['is_active'] = 1;

        // Verificamos que las credenciales sean correctas y que el usuario esté activo
        if(!Auth::attempt($credentials)){
            return response()
                ->json(['message'=>'No se encontraron las credenciales o la cuenta no está activa'], 401);
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

    public function logout(){
        auth()->user()->tokens()->delete();
        return[
            'message' => 'You have successfully logged out and the token was successfully delete'
        ];
    } 
}

