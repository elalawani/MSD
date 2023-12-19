import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';

export const useParkinsonMeasurementStore = defineStore({
    id: 'ParkinsonMeasurement',

    state: () => ({
        parkinsonMeasurements: []
    }),

    actions: {
        async getParkinsonMeasurement(patient_id) {
            this.parkinsonMeasurements = [];
            await axios
                .get(`/api/measure_fhir/get_all_measurements/${patient_id}`)
                .then((response) => {
                    this.parkinsonMeasurements = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'all_patients' });
                    }
                });
        }
    }
});
