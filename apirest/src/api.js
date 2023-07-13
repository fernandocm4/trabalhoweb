import axios from 'axios';

const api = axios.create({
  //baseURL: 'https://api.tvmaze.com/search/shows?q=girls'
  baseURL: 'http://localhost:5000'
});

export default api;