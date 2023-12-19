<template>
    <div
        class="p-6 space-y-4 md:space-y-6 sm:p-8 text-slate-900 dark:text-slate-50"
    >
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Telefonische Erstgespräche
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="mb-5">
                Fügen Sie Telefone für Erstgespräche für Patienten:
                <span class="font-bold">
                    {{ currentPatient.last_name }},
                    {{ currentPatient.first_name }}
                </span>
                hinzu
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
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
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
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                        placeholder="code"
                    />
                </div>
                <div class="ml-10 flex flex-col w-full">
                    <label for="status" class="block mb-2 text-sm font-medium"
                        >conversation reason</label
                    >
                    <input
                        type="text"
                        v-model="form.conversation_reason"
                        name="status"
                        id="status"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                        placeholder="conversation reason"
                    />
                </div>
            </div>
            <div class="flex flex-col w-full">
                <label for="status" class="block mb-2 text-sm font-medium"
                    >note</label
                >
                <textarea
                    type="text"
                    v-model="form.note"
                    name="status"
                    id="status"
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
import { computed, onMounted, ref } from 'vue';
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
            form: {
                patient: this.currentPatient.id,
                duration: '',
                code: '',
                conversation_reason: '',
                note: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post(
                    '/api/documentation/initial_interview_telephones/create/',
                    this.form
                )
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
