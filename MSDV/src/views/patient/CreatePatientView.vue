<template>
    <section class="mt-14">
        <div
            class="flex flex-col items-center justify-center px-6 py-10 mx-auto h-screen lg:py-0"
        >
            <div class="w-full rounded-lg md:mt-0 sm:max-w-screen-sm xl:p-0">
                <div
                    class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-slate-300 dark:bg-slate-700 rounded-xl"
                >
                    <form
                        method="post"
                        class="space-y-4 md:space-y-6"
                        @submit.prevent="submitForm"
                    >
                        <div v-if="step === 1">
                            <h1
                                class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6"
                            >
                                Personale Informationen
                            </h1>
                            <span class="mr-3">
                                <input
                                    class="mb-4 hover:cursor-pointer"
                                    type="radio"
                                    id="mr"
                                    value="M"
                                    v-model="patInfo.gender"
                                />
                                <label for="mr"> Männlich </label>
                            </span>
                            <input
                                class="hover:cursor-pointer"
                                type="radio"
                                id="ms"
                                value="F"
                                v-model="patInfo.gender"
                            />
                            <label for="ms"> Weiblich </label>
                            <span
                                v-if="errors.gender"
                                class="ml-4 text-red-500"
                                >{{ errors.gender }}</span
                            >
                            <div>
                                <label
                                    for="firstname"
                                    class="block mb-2 text-sm font-medium"
                                    >Vorname</label
                                >
                                <input
                                    type="text"
                                    v-model="patInfo.first_name"
                                    name="firstname"
                                    id="firstname"
                                    class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                    placeholder="Vorname"
                                    required=""
                                />
                                <span
                                    v-if="errors.first_name"
                                    class="ml-4 text-red-500"
                                    >{{ errors.first_name }}</span
                                >
                            </div>
                            <div
                                class="flex justify-between flex-row space-x-2 items-center"
                            >
                                <div class="w-full">
                                    <label
                                        for="lastname"
                                        class="block my-2 text-sm font-medium"
                                        >Nachname</label
                                    >
                                    <input
                                        type="text"
                                        v-model="patInfo.last_name"
                                        name="lastname"
                                        id="lastname"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        placeholder="Nachname"
                                        required=""
                                    />
                                    <span
                                        v-if="errors.last_name"
                                        class="ml-4 text-red-500"
                                        >{{ errors.last_name }}</span
                                    >
                                </div>
                                <div>
                                    <label
                                        for="birthdate"
                                        class="block my-2 text-sm font-medium"
                                        >birthdate</label
                                    >
                                    <input
                                        type="date"
                                        v-model="patInfo.date_of_birth"
                                        name="birthdate"
                                        id="birthdate"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        required=""
                                    />
                                    <span
                                        v-if="errors.date_of_birth"
                                        class="ml-4 text-red-500"
                                        >{{ errors.date_of_birth }}</span
                                    >
                                </div>
                            </div>
                            <div
                                class="flex justify-between flex-row space-x-2 items-center"
                            >
                                <div class="w-full">
                                    <label
                                        for="street"
                                        class="block my-2 text-sm font-medium"
                                        >Straße</label
                                    >
                                    <input
                                        type="text"
                                        v-model="patInfo.street"
                                        name="street"
                                        id="street"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        placeholder="Straße"
                                        required=""
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
                                        class="block my-2 text-sm font-medium"
                                        >Hausnummer</label
                                    >
                                    <input
                                        type="text"
                                        v-model="patInfo.house_number"
                                        name="nr"
                                        id="nr"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        placeholder="Hausnummer"
                                        required=""
                                    />
                                    <span
                                        v-if="errors.house_number"
                                        class="ml-4 text-red-500"
                                        >{{ errors.house_number }}</span
                                    >
                                </div>
                            </div>
                            <div
                                class="flex justify-between flex-row space-x-2 items-center"
                            >
                                <div>
                                    <label
                                        for="plz"
                                        class="block my-2 text-sm font-medium"
                                        >PLZ</label
                                    >
                                    <input
                                        type="text"
                                        v-model="patInfo.postal_code"
                                        name="plz"
                                        id="plz"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        placeholder="PLZ"
                                        required=""
                                    />
                                    <span
                                        v-if="errors.postal_code"
                                        class="ml-4 text-red-500"
                                        >{{ errors.postal_code }}</span
                                    >
                                </div>
                                <div class="w-full">
                                    <label
                                        for="city"
                                        class="block my-2 text-sm font-medium"
                                        >Stadt</label
                                    >
                                    <input
                                        type="text"
                                        v-model="patInfo.city"
                                        name="city"
                                        id="city"
                                        class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                        placeholder="Stadt"
                                        required=""
                                    />
                                    <span
                                        v-if="errors.city"
                                        class="ml-4 text-red-500"
                                        >{{ errors.city }}</span
                                    >
                                </div>
                            </div>
                            <div>
                                <label
                                    for="email"
                                    class="block my-2 text-sm font-medium text-gray-900 dark:text-white"
                                >
                                    Email Addresse
                                </label>
                                <input
                                    type="email"
                                    v-model="patInfo.email"
                                    name="email"
                                    placeholder="email addresse"
                                    class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                />
                                <span
                                    v-if="errors.email"
                                    class="ml-4 text-red-500"
                                    >{{ errors.email }}</span
                                >
                                <label
                                    for="phone"
                                    class="block my-2 text-sm font-medium text-gray-900 dark:text-white"
                                >
                                    Mobile
                                </label>
                                <input
                                    type="text"
                                    v-model="patInfo.phone"
                                    name="phone"
                                    placeholder="Mobile-nummer"
                                    class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-slate-50 dark:border-slate-600"
                                />
                                <span
                                    v-if="errors.phone"
                                    class="ml-4 text-red-500"
                                    >{{ errors.phone }}</span
                                >
                            </div>
                        </div>
                        <div v-if="step === 2">
                            <h1
                                class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6"
                            >
                                zusatzinformationen
                            </h1>
                            <div>
                                <label
                                    for="reason_of_visiting"
                                    class="block mb-2 text-sm font-medium"
                                    >Gründe für den Besuch</label
                                >
                                <textarea
                                    type="text"
                                    v-model="patInfo.reason_of_visiting"
                                    name="reason_of_visiting"
                                    id="reason_of_visiting"
                                    class="placeholder-slate-500 text-slate-700 border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block w-full p-2.5 dark:border-slate-600"
                                    placeholder="z.B: kopfschmerz"
                                >
                                </textarea>
                            </div>
                        </div>
                        <div v-if="step === 3">
                            <h1
                                class="text-xl font-bold leading-tight tracking-tight md:text-2xl mb-6"
                            >
                                Ärzte und Pflege zuweisen
                            </h1>
                            <div>
                                <label
                                    for="Doctors"
                                    class="block mb-2 text-sm font-medium"
                                    >Ärzte</label
                                >
                                <div>
                                    <multiselect
                                        v-model="patInfo.doctors"
                                        :options="doctors"
                                        mode="tags"
                                        :close-on-select="false"
                                        :searchable="true"
                                        class="text-sky-800"
                                        placeholder="whälen"
                                    />
                                </div>
                            </div>
                            <div>
                                <label
                                    for="nurses"
                                    class="block mt-12 mb-2 text-sm font-medium"
                                    >Pfleger:in</label
                                >
                                <div>
                                    <multiselect
                                        v-model="patInfo.nurses"
                                        :options="nurses"
                                        mode="tags"
                                        :close-on-select="false"
                                        :searchable="true"
                                        class="text-sky-800"
                                        placeholder="whälen"
                                    />
                                </div>
                            </div>
                            <div class="flex justify-around">
                                <button
                                    type="submit"
                                    class="text-gray-50 bg-sky-800 hover:bg-sky-600 rounded-lg text-sm mt-5 px-14 py-2.5"
                                >
                                    Add Patient
                                </button>
                            </div>
                        </div>
                    </form>

                    <div class="flex justify-around">
                        <button @click="previous" v-if="step > 1">
                            &lt; Previous
                        </button>
                        <button @click="next" v-if="step < 3">next &gt;</button>
                    </div>
                    <div v-if="errors.length">
                        <div class="bg-red-300 text-gray-50 rounded">
                            <p v-for="error in errors" :key="error">
                                {{ error }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import router from '@/router';
import Multiselect from '@vueform/multiselect';

export default {
    name: 'signupForm',

    setup() {
        const toastStore = useToastStore();

        return {
            toastStore
        };
    },
    components: {
        Multiselect
    },
    data() {
        return {
            step: 1,
            doctors: [],
            nurses: [],
            medications: [],
            chronic_conditions: [],
            patInfo: {
                first_name: '',
                last_name: '',
                gender: '',
                street: '',
                house_number: '',
                postal_code: '',
                city: '',
                date_of_birth: '',
                email: '',
                phone: '',
                reason_of_visiting: '',
                doctors: [],
                nurses: []
            },
            errors: {
                first_name: '',
                last_name: '',
                gender: '',
                street: '',
                house_number: '',
                postal_code: '',
                city: '',
                date_of_birth: '',
                email: '',
                phone: '',
                reason_of_visiting: '',
                doctors: [],
                nurses: []
            }
        };
    },
    methods: {
        next() {
            this.errors.first_name = '';
            this.errors.last_name = '';
            this.errors.gender = '';
            this.errors.street = '';
            this.errors.house_number = '';
            this.errors.city = '';
            this.errors.postal_code = '';
            this.errors.date_of_birth = '';
            this.errors.email = '';
            this.errors.phone = '';
            if (this.step === 1) {
                if (this.patInfo.first_name === '') {
                    this.errors.first_name = 'Bitte geben Sie Vorname ein';
                }
                if (this.patInfo.last_name === '') {
                    this.errors.last_name = 'Bitte geben Sie nachname ein';
                }
                if (this.patInfo.gender === '') {
                    this.errors.gender = 'Bitte wählen Sie';
                }
                if (this.patInfo.street === '') {
                    this.errors.street = 'Bitte geben Sie Straße ein';
                }
                if (this.patInfo.city === '') {
                    this.errors.city = 'Bitte geben Sie Stadt ein';
                }
                if (this.patInfo.house_number === '') {
                    this.errors.house_number = 'Bitte geben Sie Hausnummer ein';
                }
                if (this.patInfo.postal_code === '') {
                    this.errors.postal_code = 'Bitte geben PLZ ein';
                }
                if (this.patInfo.email === '') {
                    this.errors.email = 'Bitte geben Sie E-Mail-Adresse ein';
                }
                if (this.patInfo.phone === '') {
                    this.errors.phone = 'Bitte geben ein Mobile nummer ein';
                }
            }
            if (
                this.step < 3 &&
                this.errors.first_name === '' &&
                this.errors.last_name === '' &&
                this.errors.gender === '' &&
                this.errors.street === '' &&
                this.errors.city === '' &&
                this.errors.house_number === '' &&
                this.errors.postal_code === '' &&
                this.errors.email === '' &&
                this.errors.phone === ''
            ) {
                this.step += 1;
            }
        },
        previous() {
            if (this.step > 1) {
                this.step -= 1;
            }
        },
        submitForm() {
            axios
                .post('/api/patients/create/', this.patInfo)
                .then((response) => {
                    if (response.data.message === 'success') {
                        this.toastStore.showToast(
                            5000,
                            'neue Patient wurde hinzugefügt',
                            'border border-green-500 bg-green-100 text-green-900'
                        );

                        this.patInfo.first_name = '';
                        this.patInfo.last_name = '';
                        this.patInfo.gender = '';
                        this.patInfo.street = '';
                        this.patInfo.house_number = '';
                        this.patInfo.city = '';
                        this.patInfo.postal_code = '';
                        this.patInfo.date_of_birth = '';
                        this.patInfo.email = '';
                        this.patInfo.phone = '';
                        this.patInfo.reason_of_visiting = '';
                        this.patInfo.doctors = [];
                        this.patInfo.nurses = [];

                        router.push({ name: 'view' });
                    } else {
                        this.toastStore.showToast(
                            5000,
                            'irgendwas ist schiefgelaufen',
                            'border border-red-500 bg-red-100 text-red-900'
                        );
                    }
                })
                .catch((error) => {
                    console.log('error', error);
                });
        }
    },

    async mounted() {
        const response_doctors = await axios.get('/api/doctors/');
        this.doctors = response_doctors.data.map((doctors) => ({
            value: doctors.id,
            label: doctors.username
        }));

        const response_nurses = await axios.get('/api/nurses/');
        this.nurses = response_nurses.data.map((nurses) => ({
            value: nurses.id,
            label: nurses.username
        }));
    }
};
</script>
