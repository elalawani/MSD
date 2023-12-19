import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';
import { useToastStore } from '@/stores/toast';

export const useAddInformation = defineStore({
    id: 'addInformation',
    state: () => ({}),
    actions: {
        async addSurgery(data) {
            await axios
                .post('/api/patients/surgery/create/', data)
                .then((response) => {
                    if (response.data.message === 'success') {
                        useToastStore().showToast(
                            3000,
                            'surgery addiert',
                            'border border-green-500 bg-green-100 text-green-900'
                        );
                        router.push('/profile');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async addMedication(data) {
            await axios
                .post('/api/patients/medication/create/', data)
                .then((response) => {
                    if (response.data.message === 'success') {
                        useToastStore().showToast(
                            3000,
                            'medication addiert',
                            'border border-green-500 bg-green-100 text-green-900'
                        );
                        router.push('/profile');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async addChronicCondition(data) {
            await axios
                .post('/api/patients/chronic_conditions/create/', data)
                .then((response) => {
                    if (response.data.message === 'success') {
                        useToastStore().showToast(
                            3000,
                            'Chronic Condition addiert',
                            'border border-green-500 bg-green-100 text-green-900'
                        );
                        router.push('/profile');
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});
