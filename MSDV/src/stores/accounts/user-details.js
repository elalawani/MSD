import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router';
import { useToastStore } from '@/stores/toast';

export const useProfileStore = defineStore({
    id: 'profile',

    state: () => ({
        infos: {}
    }),

    actions: {
        async getProfileInfo() {
            this.infos = {};
            await axios
                .get('api/profile/')
                .then((response) => {
                    this.infos = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        async updateProfile(userId, data) {
            await axios
                .put(`api/profile/${userId}/`, data)
                .then((response) => {
                    if (response.data.message === 'success') {
                        useToastStore().showToast(
                            3000,
                            'form gespeichert',
                            'border border-green-500 bg-green-100 text-green-900'
                        );
                        router.push('/profile');
                    }
                })
                .catch((error) => {
                    console.log(error);
                    useToastStore().showToast(
                        3000,
                        'versuchen sie später nochmal',
                        'border border-red-500 bg-red-100 text-red-900'
                    );
                });
        },
        async updateAddress(user_id, data) {
            await axios
                .put(`api/profile/address/${user_id}/`, data)
                .then((response) => {
                    if (response.data.message === 'success') {
                        useToastStore().showToast(
                            3000,
                            'form gespeichert',
                            'border border-green-500 bg-green-100 text-green-900'
                        );

                        router.push('/profile');
                    }
                })
                .catch((error) => {
                    console.log(error);
                    useToastStore().showToast(
                        3000,
                        'versuchen sie später nochmal',
                        'border border-red-500 bg-red-100 text-red-900'
                    );
                });
        }
    }
});
