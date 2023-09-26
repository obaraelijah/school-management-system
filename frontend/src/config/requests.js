import axios from 'axios';
import { baseUrl as url } from '../consts';
import fetchToken from '../utils/getNewToken';

const authRequest = axios.create({
  baseURL: url,
});

authRequest.interceptors.request.use(
  (config) => {
    // add authorization token to api requests
    const auth = JSON.parse(localStorage.getItem('auth'));
    const token = auth?.access;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

authRequest.interceptors.response.use(
  (res) => {
    return Promise.resolve(res);
  },
  async (error) => {
    // use refresh token to get new access token if expired
    const auth = JSON.parse(localStorage.getItem('auth'));
    const token = auth?.access;
    if (error.response.status === 401 && token) {
      await fetchToken();
    }
  }
);
export default authRequest;
