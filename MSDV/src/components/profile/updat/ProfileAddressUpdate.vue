<template>
    <section>
        <div class="flex flex-col items-center lg:py-0">
            <div class="w-full md:mt-0 xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 shadow-xl">
                    <form
                        class="space-y-4 md:space-y-6"
                        @submit.prevent="submitForm"
                    >
                        <div>
                            <label
                                for="street"
                                class="block mb-2 text-sm font-medium"
                                >Straße</label
                            >
                            <input
                                type="text"
                                v-model="form.street"
                                name="street"
                                id="street"
                                :class="
                                    errors.street
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="straße"
                            />
                            <span
                                v-if="errors.street"
                                class="ml-4 text-red-500"
                                >{{ errors.street }}</span
                            >
                        </div>
                        <div>
                            <label
                                for="nr"
                                class="block mb-2 text-sm font-medium"
                                >Haus nummer</label
                            >
                            <input
                                type="text"
                                v-model="form.nr"
                                name="nr"
                                id="nr"
                                :class="
                                    errors.nr
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="haus nummer"
                            />
                            <span v-if="errors.nr" class="ml-4 text-red-500">{{
                                errors.nr
                            }}</span>
                        </div>
                        <div>
                            <label
                                for="PLZ"
                                class="block mb-2 text-sm font-medium"
                                >PLZ</label
                            >
                            <input
                                type="text"
                                v-model="form.PLZ"
                                name="PLZ"
                                id="PLZ"
                                :class="
                                    errors.PLZ
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="PLZ"
                            />
                            <span v-if="errors.PLZ" class="ml-4 text-red-500">{{
                                errors.PLZ
                            }}</span>
                        </div>
                        <div>
                            <label
                                for="city"
                                class="block mb-2 text-sm font-medium"
                                >Stadt</label
                            >
                            <input
                                type="text"
                                v-model="form.city"
                                name="city"
                                id="city"
                                :class="
                                    errors.city
                                        ? 'border-red-500 dark:border'
                                        : ''
                                "
                                class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-500 dark:border-slate-600"
                                placeholder="haus nummer"
                            />
                            <span
                                v-if="errors.city"
                                class="ml-4 text-red-500"
                                >{{ errors.city }}</span
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
                street: '',
                nr: '',
                PLZ: '',
                city: ''
            },
            errors: {
                street: '',
                nr: '',
                PLZ: '',
                city: ''
            }
        };
    },
    methods: {
        submitForm() {
            this.errors.street = '';
            this.errors.nr = '';
            this.errors.PLZ = '';
            this.errors.city = '';
            if (this.form.street === '') {
                this.errors.street = 'bitte Straße eingeben';
            }
            if (this.form.nr === '') {
                this.errors.nr = 'bitte haus nummer eingeben';
            }
            if (this.form.PLZ === '') {
                this.errors.PLZ = 'bitte PLZ eingeben';
            }
            if (this.form.city === '') {
                this.errors.city = 'bitte Stadt eingeben';
            }
            if (
                this.errors.street === '' &&
                this.errors.nr === '' &&
                this.errors.PLZ === '' &&
                this.errors.city === ''
            ) {
                this.profileStore.updateAddress(this.userId, this.form);
                window.location.reload();
            }
        }
    }
};
</script>
