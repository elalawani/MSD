import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';

export const useQuestionnaireStore = defineStore({
    id: 'questionnaire',
    state: () => ({
        barthelIndex: []
    }),

    actions: {
        async getBarthelIndex(patient_id) {
            this.barthelIndex = [];
            await axios
                .get(`/api/questionnaires/${patient_id}/barthel_indexes/`)
                .then((response) => {
                    this.barthelIndex = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});
