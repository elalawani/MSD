<template>
    <div
        class="p-6 space-y-4 md:space-y-6 sm:p-8 text-slate-900 dark:text-slate-50"
    >
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Telefonische Rücksprache mit dem Feedback-Betreuungsteam
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="mb-5">
                Neue telefonische Beratung des Feedback-Care-Teams für Patient:
                <span class="font-bold">
                    {{ currentPatient.last_name }},
                    {{ currentPatient.first_name }}
                </span>
            </div>
            <div class="flex flex-row items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label
                        for="blood_cholesterol"
                        class="block mb-2 text-sm font-medium"
                        >Rückmeldung notwendig</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="radio"
                            value="false"
                            id="no"
                            v-model="form.feedback_necessary"
                        />
                        <label class="mx-3" for="no">nein</label>
                        <input
                            type="radio"
                            value="true"
                            id="yes"
                            v-model="form.feedback_necessary"
                        />
                        <label class="mx-3" for="Yes">ja</label>
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
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 text-slate-700 dark:border-slate-600"
                        placeholder="code"
                    />
                </div>
                <div class="ml-10 flex flex-col w-full">
                    <label for="status" class="block mb-2 text-sm font-medium"
                        >Feedback-Empfänger</label
                    >
                    <select
                        class="p-2.5 rounded-l text-slate-700"
                        v-model="form.feedback_to"
                    >
                        <option
                            v-for="option in receiver"
                            :value="option.id"
                            :key="option.id"
                        >
                            {{ option.text }}
                        </option>
                    </select>
                </div>
            </div>
            <div class="flex flex-col w-full">
                <label for="status" class="block mb-2 text-sm font-medium"
                    >Besuchsgrund</label
                >
                <textarea
                    type="text"
                    v-model="form.visit_reason"
                    name="status"
                    id="status"
                    class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 text-slate-700 dark:border-slate-600"
                    placeholder="Besuchsgrund"
                >
                </textarea>
            </div>
            <div class="flex flex-col mt-8 w-full">
                <label for="status" class="block mb-2 text-sm font-medium"
                    >Fragen</label
                >
                <textarea
                    type="text"
                    v-model="form.feedback_questions"
                    name="status"
                    id="status"
                    class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 text-slate-700 dark:border-slate-600"
                    placeholder="Fragen"
                >
                </textarea>
            </div>
            <div class="flex flex-col mt-8 w-full">
                <label for="status" class="block mb-2 text-sm font-medium"
                    >Empfehlungen</label
                >
                <textarea
                    type="text"
                    v-model="form.recommendations"
                    name="status"
                    id="status"
                    class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 text-slate-700 dark:border-slate-600"
                    placeholder="Empfehlungen"
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
            receiver: [],
            form: {
                patient: this.currentPatient.id,
                feedback_necessary: false,
                code: '',
                feedback_questions: '',
                feedback_to: '',
                recommendations: '',
                visit_reason: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post(
                    '/api/documentation/feedback_care_team_telephone_consultation/create/',
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
    },
    created() {
        axios
            .get(
                '/api/documentation/feedback_care_team_telephone_consultation_choices/'
            )
            .then((response) => {
                this.receiver = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
    }
};
</script>
