<template>
    <div
        class="p-6 space-y-4 md:space-y-6 sm:p-8 text-slate-900 dark:text-slate-50"
    >
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Fallprüfungsrat
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="mb-5">
                Fallbesprechung für den Patienten:
                <span class="font-bold">
                    {{ currentPatient.last_name }},
                    {{ currentPatient.first_name }}
                </span>
                hinzufügen
            </div>
            <div class="flex flex-row items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label
                        for="blood_cholesterol"
                        class="block mb-2 text-sm font-medium"
                        >Dauer in min</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="form.duration"
                            name="blood_cholesterol"
                            id="blood_cholesterol"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                            placeholder="minuten"
                        />
                        <span class="ml-2"> min </span>
                    </div>
                </div>

                <div class="ml-10 flex flex-col w-full">
                    <label for="status" class="block mb-2 text-sm font-medium"
                        >code</label
                    >
                    <input
                        type="text"
                        v-model="form.code"
                        name="status"
                        id="status"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                        placeholder="code"
                    />
                </div>
            </div>
            <div class="flex flex-row w-full justify-around items-center">
                <div class="w-full mr-4">
                    <label
                        for="participants"
                        class="block mb-2 text-sm font-medium"
                        >Teilnehmer</label
                    >
                    <div>
                        <multiselect
                            v-model="form.participants"
                            :options="allParticipants"
                            mode="tags"
                            :close-on-select="false"
                            :searchable="true"
                            placeholder="Select Teilnehmer"
                        />
                    </div>
                </div>
                <div class="w-full flex-col flex">
                    <label for="category" class="block mb-2 text-sm font-medium"
                        >Anamnese besprochen</label
                    >
                    <input
                        type="text"
                        v-model="form.anamnese_discussed"
                        name="category"
                        id="category"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                        placeholder="Anamnese besprochen"
                    />
                </div>
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
import Multiselect from '@vueform/multiselect';
import { useToastStore } from '@/stores/toast';

export default {
    components: {
        Multiselect
    },
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
            allParticipants: [],
            form: {
                patient: this.currentPatient.id,
                duration: '',
                code: '',
                participants: [],
                anamnese_discussed: '',
                note: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post(
                    '/api/documentation/case_review_council/create/',
                    this.form
                )
                .then((response) => {
                    this.toastStore.showToast(
                        5000,
                        'Messung hinzugefügt',
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
    },
    async mounted() {
        const response_doctors = await axios.get('/api/doctors/');
        this.allParticipants = response_doctors.data.map((doctors) => ({
            value: doctors.id,
            label: doctors.username
        }));
    }
};
</script>
