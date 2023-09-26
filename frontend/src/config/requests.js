import axios from 'axios';
import { baseUrl as url } from '../consts';
import fetchToken from '../utils/getNewToken';

const auth = JSON.parse(localStorage.getItem('auth'));
const token = auth.access;

const authRequest = axios.create({
  baseURL: url,
});

// add authorization token to api requests
authRequest.interceptors.request.use(
  (config) => {
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
    if (error.response.status === 401 && token) {
      await fetchToken();
    }
  }
);
export default authRequest;
