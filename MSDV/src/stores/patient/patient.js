import { defineStore } from 'pinia';
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import router from '@/router';
export const usePatientStore = defineStore({
    id: 'patients',

    state: () => ({
        patient_list: [],
        patient: [],
        filters: {
            by_name: null,
            by_type: null,
            by_birthdate: null,
            by_doctor: null,
            by_nurse: null,
            by_condition: null,
            by_medications: null,
            by_creator: null
        }
    }),

    actions: {
        async getAllPatients() {
            this.patient_list = [];
            await axios
                .get('/api/patients/')
                .then((response) => {
                    this.patient_list = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async getPatients() {
            this.patient_list = [];
            await axios
                .get('/api/patients/filtered', { params: this.filters })
                .then((response) => {
                    this.patient_list = response.data;
                })
                .catch((error) => {
                    console.log('error', error);
                });
        },
        updateFilters(newFilters) {
            this.filters = newFilters;
        },
        removeFilter() {
            this.filters = '';
        },
        async getPatient(id) {
            await axios
                .get(`/api/patients/${id}`)
                .then((response) => {
                    this.patient = response.data;
                })
                .catch((error) => {
                    console.log('error', error.response.status);
                    if (error.response && error.response.status === 403) {
                        router.push({ name: 'view' });
                    }
                });
        }
    },
    persist: true
});
