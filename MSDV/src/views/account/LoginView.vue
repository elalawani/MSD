<template>
    <section>
        <div
            class="flex flex-col items-center justify-center px-6 py-8 mx-auto h-screen lg:py-0"
        >
            <div class="w-full rounded-lg md:mt-0 sm:max-w-md xl:p-0">
                <div
                    class="p-6 space-y-4 md:space-y-6 sm:p-8 shadow-xl border dark:border-0 dark:bg-slate-700 rounded-xl"
                >
                    <h1
                        class="dark:text-slate-100 text-xl font-extrabold leading-tight tracking-tight md:text-2xl"
                    >
                        Sign in
                    </h1>
                    <form
                        class="space-y-4 md:space-y-6"
                        @submit.prevent="submitForm"
                    >
                        <div>
                            <label
                                for="email"
                                class="block mb-2 text-sm font-medium text-slate-900 dark:text-slate-100"
                                >email</label
                            >
                            <input
                                type="email"
                                name="email"
                                v-model="form.email"
                                :class="
                                    errors.email
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border-2 dark:border-0 sm:text-sm rounded-lg focus:border-sky-500 w-full p-2.5 dark:bg-slate-500 dark:text-slate-100 dark:placeholder:text-slate-100"
                                placeholder="email"
                            />
                            <span
                                v-if="errors.email"
                                class="ml-4 text-red-500"
                                >{{ errors.email }}</span
                            >
                        </div>
                        <div>
                            <label
                                for="password"
                                class="block mb-2 text-sm font-medium text-slate-900 dark:text-slate-100"
                                >Password</label
                            >
                            <input
                                type="password"
                                name="password"
                                v-model="form.password"
                                :class="
                                    errors.email
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                placeholder="password"
                                class="border-2 dark:border-0 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-500 dark:text-slate-100 dark:placeholder:text-slate-100"
                            />
                            <span
                                v-if="errors.password"
                                class="ml-4 text-red-500"
                                >{{ errors.password }}</span
                            >
                        </div>
                        <div class="flex justify-around">
                            <button
                                type="submit"
                                class="text-sky-700 hover:text-white border dark:border-0 border-sky-700 dark:text-slate-100 dark:bg-sky-700 hover:bg-sky-700 dark:hover:bg-sky-500 rounded-lg text-sm px-14 py-2.5"
                            >
                                Sign in
                            </button>
                        </div>
                    </form>
                    <div v-if="errors.length">
                        <div class="bg-red-300 text-gray-50 rounded">
                            <p v-for="error in errors" :key="error">
                                {{ error }}
                            </p>
                        </div>
                    </div>
                    <div class="flex justify-around">
                        <router-link to="/signup">signup</router-link>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
import router from '@/router';
import { useUserStore } from '@/stores/accounts/user';

export default {
    name: 'loginform',
    setup() {
        const userStore = useUserStore();

        return {
            userStore
        };
    },

    data() {
        return {
            form: {
                email: '',
                password: ''
            },
            errors: {
                email: '',
                password: ''
            }
        };
    },
    methods: {
        async submitForm() {
            this.errors.email = '';
            this.errors.password = '';

            if (this.form.email === '') {
                this.errors.email = 'Bitte geben Sie ihre E-Mail-Adresse ein';
            }
            if (this.form.password === '') {
                this.errors.password = 'Bitte geben Sie ihre password ein';
            }

            if (this.errors.password === '' && this.errors.email === '') {
                await axios
                    .post('/api/login/', this.form)
                    .then((response) => {
                        this.userStore.setToken(response.data);

                        axios.defaults.headers.common['Authorization'] =
                            'Bearer ' + response.data.access;
                    })
                    .catch((error) => {
                        console.log('error', error);
                    });
                await axios
                    .get('/api/profile/')
                    .then((response) => {
                        this.userStore.setUserInfo(response.data);
                        router.push('/');
                    })
                    .catch((error) => {
                        console.log('error', error);
                    });
            }
        }
    }
};
</script>
