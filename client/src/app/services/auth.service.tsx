import apiCall from './api.service';

type LoginCredentials = {
  username: string,
  password: string,
}

export const login = async (data: LoginCredentials) => {
  try {
    const response = await apiCall.post('/login', data);
    console.log(response);
    return response;
  } catch (error) {}
}