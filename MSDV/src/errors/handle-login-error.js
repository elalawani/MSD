import axios from 'axios';
import router from '@/router';

axios.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        if (!error.response) {
            console.error('network Error: ', error);
            return Promise.reject(error);
        }
        if (error.response && error.response.status === 401) {
            router.push('/login');
        } else {
            throw error;
        }
    }
);
