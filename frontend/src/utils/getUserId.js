import jwt_decode from 'jwt-decode';

const getUserIdFromToken = () => {
  const token = JSON.parse(localStorage.getItem('auth')) || null;

  const decoded_token = token ? jwt_decode(token.access) : null;

  return decoded_token ? decoded_token.user_id : null;
};

export default getUserIdFromToken;
