import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';
import { useToastStore } from '@/stores/toast';

export const useCommentsStore = defineStore({
    id: 'CommentsStore',

    state: () => ({
        comments: [],
        errors: null
    }),

    actions: {
        async creatComment(data) {
            let result = null;
            await axios
                .post('/api/measure_fhir/create_measurement_comment/', data)
                .then((response) => {
                    result = response.data;
                })
                .catch((error) => {
                    console.log(error.response.data);
                });
            return result;
        },
        async getComment(patientId) {
            this.comments = [];
            await axios
                .get(`/api/measure_fhir/get_measurement_comments/${patientId}/`)
                .then((response) => {
                    this.comments = response.data;
                })
                .catch((error) => {
                    if (error.response && error.response.status === 404) {
                        this.errors = 'Comments not found.';
                    } else {
                        this.errors =
                            'An error occurred while fetching the comments.';
                    }
                    console.log(error);
                });
        }
    }
});
