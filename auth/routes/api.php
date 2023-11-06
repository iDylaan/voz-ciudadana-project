<?php

use App\Http\Controllers\Api\AuthController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;



Route::post('register', [AuthController::class, 'register']);
Route::post('login', [AuthController::class, 'login']);
Route::post('update_user_profile', [AuthController::class, 'update_user_profile']);


Route::middleware(['auth:sanctum'])->group(function (){

    Route::get('logout', [AuthController::class, 'logout']);
});






Route::middleware('auth:sanctum')->get('/username', function (Request $request) {
    return $request->user();
});
