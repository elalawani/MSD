<template>
    <section>
        <div class="flex flex-col items-center justify-center lg:py-0">
            <div class="w-full md:mt-0 xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <form
                        class="space-y-4 md:space-y-6 pb-7"
                        @submit.prevent="submitForm"
                    >
                        <div>
                            <label
                                for="first_name"
                                class="block mb-2 text-sm font-medium"
                                >Vorname</label
                            >
                            <input
                                type="text"
                                v-model="form.first_name"
                                name="first_name"
                                id="first_name"
                                :class="
                                    errors.first_name
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="Vorname"
                            />
                            <span
                                v-if="errors.first_name"
                                class="ml-4 text-red-500"
                                >{{ errors.first_name }}</span
                            >
                        </div>
                        <div>
                            <label
                                for="last_name"
                                class="block mb-2 text-sm font-medium"
                                >Nachname</label
                            >
                            <input
                                type="text"
                                v-model="form.last_name"
                                name="last_name"
                                id="last_name"
                                :class="
                                    errors.last_name
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="Nachname"
                            />
                            <span
                                v-if="errors.last_name"
                                class="ml-4 text-red-500"
                                >{{ errors.last_name }}</span
                            >
                        </div>
                        <div class="flex justify-around">
                            <button
                                type="submit"
                                class="text-sky-700 hover:text-white border dark:border-0 border-sky-700 dark:text-slate-100 dark:bg-sky-700 hover:bg-sky-700 dark:hover:bg-sky-500 rounded-lg text-sm px-14 py-2.5"
                            >
                                Speichern
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import { useUserStore } from '@/stores/accounts/user';
import { useProfileStore } from '@/stores/accounts/user-details';

export default {
    name: 'updateProfileForm',
    setup() {
        const toastStore = useToastStore();
        const userId = useUserStore().user.id;
        const profileStore = useProfileStore();

        return {
            toastStore,
            userId,
            profileStore
        };
    },
    data() {
        return {
            form: {
                first_name: '',
                last_name: ''
            },
            errors: {
                first_name: '',
                last_name: ''
            }
        };
    },
    methods: {
        submitForm() {
            this.errors.first_name = '';
            this.errors.last_name = '';
            if (this.form.first_name === '') {
                this.errors.first_name = 'bitte Vorname eingeben';
            }

            if (this.form.last_name === '') {
                this.errors.last_name = 'bitte Nachname eingeben';
            }
            if (this.errors.first_name === '' && this.errors.last_name === '') {
                this.profileStore.updateProfile(this.userId, this.form);
                window.location.reload();
            }
        }
    }
};
</script>
