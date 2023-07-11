import axios from 'axios';

const apiCall = axios.create({
  baseURL: process.env.server_url
});
apiCall.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
// apiCall.defaults.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Origin, Access-Control-Allow-Methods, Access-Control-Allow-Credentials, Origin, Content-Type, Authorization';
// apiCall.defaults.headers['Access-Control-Allow-Credentials'] = true;
// apiCall.defaults.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS,DELETE';
// apiCall.defaults.headers['Access-Control-Allow-Origin'] = process.env.url || '';

apiCall.interceptors.request.use(  
  response => response,
  error => {
    // const statusCode = error.response.status;
    // if (statusCode === 401 || statusCode === 403) {
    //   window.location.href = '/';
    // }

    if (process.env.NODE_ENV !== 'production') {
      if (error.response) {
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        console.log(error.request);
      } else {
        console.log('Error', error.message);
      }
      console.log(error.config);
    }

    throw error;
  }
);

export default apiCall;