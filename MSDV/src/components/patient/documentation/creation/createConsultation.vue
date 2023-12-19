<template>
    <div
        class="p-6 space-y-4 md:space-y-6 sm:p-8 text-slate-900 dark:text-slate-50"
    >
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Beratung
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="mb-5">
                Beratung für patient:
                <span class="font-bold">
                    {{ currentPatient.last_name }},
                    {{ currentPatient.first_name }}
                </span>
            </div>
            <div class="flex items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label for="duration" class="block mb-2 text-sm font-medium"
                        >Dauer in min</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="form.duration"
                            name="duration"
                            id="duration"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="minuten"
                        />
                        <span class="ml-2"> min </span>
                    </div>
                </div>
                <div class="ml-10 flex flex-col w-full">
                    <label for="code" class="block mb-2 text-sm font-medium"
                        >code</label
                    >
                    <input
                        type="text"
                        v-model="form.code"
                        name="code"
                        id="code"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                        placeholder="code"
                    />
                </div>
            </div>
            <div class="flex flex-row justify-around items-center space-x-3">
                <div class="w-full flex-col flex">
                    <label
                        for="doctor_initials"
                        class="block mb-2 text-sm font-medium"
                        >Arzt-Initialen</label
                    >
                    <input
                        type="text"
                        v-model="form.doctor_initials"
                        name="doctor_initials"
                        id="doctor_initials"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                        placeholder="Arzt-Initialen"
                    />
                </div>
            </div>
            <div class="flex flex-row justify-around items-center space-x-3">
                <div class="w-full flex-col flex">
                    <label
                        for="decisions"
                        class="block mb-2 text-sm font-medium"
                        >Entscheidungen des Arztes</label
                    >
                    <input
                        type="text"
                        v-model="form.decisions"
                        name="decisions"
                        id="decisions"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                        placeholder="Entscheidungen des Arztes"
                    />
                </div>
            </div>
            <div
                class="mt-10 flex flex-row justify-around items-center space-x-3"
            >
                <div class="flex flex-col w-4/5">
                    <label class="block mb-2 text-sm font-medium"
                        >Krankenhauseinweisung erforderlich</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="radio"
                            value="false"
                            id="no"
                            v-model="form.hospital_admission_required"
                        />
                        <label class="mx-3" for="no">nein</label>
                        <input
                            type="radio"
                            value="true"
                            id="yes"
                            v-model="form.hospital_admission_required"
                        />
                        <label class="mx-3" for="Yes">ja</label>
                    </div>
                </div>
                <div class="flex flex-col w-4/5">
                    <label
                        for="reason_for_clinic_appointment"
                        class="block mb-2 text-sm font-medium"
                        >Grund der Aufnahme</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="text"
                            v-model="form.reason_for_admission"
                            name="reason_for_clinic_appointment"
                            id="reason_for_clinic_appointment"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="Grund der Aufnahme"
                        />
                    </div>
                </div>
            </div>
            <div
                class="mt-10 flex flex-row justify-around items-center space-x-3"
            >
                <div class="flex flex-col w-full">
                    <label class="block mb-2 text-sm font-medium"
                        >Kliniktermin erforderlich</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="radio"
                            value="false"
                            id="no"
                            v-model="form.clinic_appointment_required"
                        />
                        <label class="mx-3" for="no">nein</label>
                        <input
                            type="radio"
                            value="true"
                            id="yes"
                            v-model="form.clinic_appointment_required"
                        />
                        <label class="mx-3" for="Yes">ja</label>
                    </div>
                </div>
                <div class="flex flex-col w-full">
                    <label
                        for="reason_for_admission"
                        class="block mb-2 text-sm font-medium"
                        >Grund für den Kliniktermin</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="text"
                            v-model="form.reason_for_clinic_appointment"
                            name="reason_for_admission"
                            id="reason_for_admission"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="Grund für den Kliniktermin"
                        />
                    </div>
                </div>
            </div>
            <div class="mt-10">
                <div class="flex flex-row justify-between space-x-3">
                    <div class="w-full flex-col flex">
                        <label
                            for="measures_after_appointment"
                            class="block mb-2 text-sm font-medium"
                            >Maßnahmen nach Vereinbarung</label
                        >
                        <input
                            type="text"
                            v-model="form.measures_after_appointment"
                            name="measures_after_appointment"
                            id="measures_after_appointment"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="Maßnahmen nach Vereinbarung"
                        />
                    </div>
                    <div class="w-full flex-col flex">
                        <label
                            for="measures_taken"
                            class="block mb-2 text-sm font-medium"
                            >Messungen durchgeführt</label
                        >
                        <input
                            type="text"
                            v-model="form.measures_taken"
                            name="measures_taken"
                            id="measures_taken"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="Messungen durchgeführt"
                        />
                    </div>
                </div>
            </div>
            <div class="w-full flex-col flex mt-10">
                <label for="note" class="block mb-2 text-sm font-medium"
                    >note</label
                >
                <textarea
                    type="text"
                    v-model="form.note"
                    name="note"
                    id="note"
                    class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                    placeholder="note"
                >
                </textarea>
            </div>
        </form>
        <button
            @click="submitForm"
            class="px-5 py-3 dark:bg-sky-900 bg-sky-700 hover:bg-sky-500 dark:hover:bg-sky-700 text-slate-50 w-fit rounded-xl"
        >
            absenden
        </button>
    </div>
</template>
<script>
import axios from 'axios';
import { usePatientStore } from '@/stores/patient/patient';
import { useRoute } from 'vue-router';
import { computed, onMounted, ref, watch } from 'vue';
import router from '@/router';
import { useToastStore } from '@/stores/toast';

export default {
    setup() {
        const route = useRoute();
        const store = usePatientStore();
        const id = ref(route.params.id);
        const toastStore = useToastStore();

        const fetchData = async () => {
            await store.getPatient(id.value);
        };

        onMounted(fetchData);

        const currentPatient = computed(() => store.patient);

        return { currentPatient, toastStore };
    },
    data() {
        return {
            consulters: [],
            form: {
                patient: this.currentPatient.id,
                duration: '',
                code: '',
                doctor_initials: '',
                decisions: '',
                reason_for_admission: '',
                hospital_admission_required: false,
                clinic_appointment_required: false,
                reason_for_clinic_appointment: '',
                measures_after_appointment: '',
                measures_taken: '',
                note: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post('/api/documentation/consultation/create/', this.form)
                .then((response) => {
                    this.toastStore.showToast(
                        5000,
                        'measurement added',
                        'border border-green-500 bg-green-100 text-green-900'
                    );
                    router.push({
                        path: `/details/${this.currentPatient.id}/documentation`
                    });
                })
                .catch((error) => {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx
                        console.error('Data:', error.response.data);
                        console.error('Status:', error.response.status);
                        console.error('Headers:', error.response.headers);
                    } else if (error.request) {
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser
                        console.error('No response received:', error.request);
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        console.error('Error', error.message);
                    }
                });
        }
    }
};
</script>
