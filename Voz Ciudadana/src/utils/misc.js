import { jwtDecode } from 'jwt-decode';

export const tokenExpired = (token) => {
    if (!token) return true;
    const decodedToken = jwtDecode(token);
    if (!decodedToken.exp) return true;
    const dateNow = new Date();
    return decodedToken.exp < (dateNow.getTime() / 1000);
};
