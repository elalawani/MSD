<template>
    <div
        class="p-6 space-y-4 md:space-y-6 sm:p-8 text-slate-900 dark:text-slate-50"
    >
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            Telefonische Beratung
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="mb-5">
                Telefonische Beratung für patient:
                <span class="font-bold">
                    {{ currentPatient.last_name }},
                    {{ currentPatient.first_name }}
                </span>
            </div>
            <div class="flex items-center mb-8">
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
            <div class="flex flex-row justify-around items-center space-x-3">
                <div class="w-full flex-col flex">
                    <label for="Doctors" class="block mb-2 text-sm font-medium"
                        >Berater</label
                    >
                    <div>
                        <multiselect
                            v-model="form.consultation_by"
                            :options="consulters"
                            mode="tags"
                            :close-on-select="false"
                            :searchable="true"
                            placeholder="Select Berater"
                        />
                    </div>
                </div>
                <div class="w-full flex-col flex">
                    <label for="category" class="block mb-2 text-sm font-medium"
                        >Beratungsgrund</label
                    >
                    <select
                        class="p-2.5 rounded-lg text-slate-900"
                        v-model="form.consultation_reason"
                    >
                        <option
                            v-for="option in reasons"
                            :value="option.id"
                            :key="option.id"
                        >
                            {{ option.text }}
                        </option>
                    </select>
                </div>
            </div>
            <div class="mt-10">
                <div class="flex flex-row justify-between space-x-3">
                    <div class="w-full flex-col flex">
                        <label
                            for="category"
                            class="block mb-2 text-sm font-medium"
                            >Gesprächsthema</label
                        >
                        <input
                            type="text"
                            v-model="form.conversation_topics"
                            name="category"
                            id="category"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                            placeholder="Gesprächsthema"
                        />
                    </div>
                    <div class="w-full flex-col flex">
                        <label
                            for="recommendations"
                            class="block mb-2 text-sm font-medium"
                            >Empfehlungen</label
                        >
                        <input
                            type="text"
                            v-model="form.recommendations"
                            name="recommendations"
                            id="recommendations"
                            class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                            placeholder="Empfehlungen"
                        />
                    </div>
                </div>
            </div>
            <div class="mt-10 flex flex-row justify-between space-x-3">
                <div class="w-full flex-col flex">
                    <label
                        for="recommendation_issued"
                        class="block mb-2 text-sm font-medium"
                        >Empfehlung ausgesprochen</label
                    >
                    <input
                        type="text"
                        v-model="form.recommendation_issued"
                        name="recommendation_issued"
                        id="recommendation_issued"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                        placeholder="Empfehlung ausgesprochen"
                    />
                </div>
                <div class="w-full flex-col flex">
                    <label for="others" class="block mb-2 text-sm font-medium"
                        >Andere</label
                    >
                    <input
                        type="text"
                        v-model="form.others"
                        name="others"
                        id="others"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
                        placeholder="Andere"
                    />
                </div>
            </div>
            <div class="w-full flex-col flex mt-10">
                <label for="category" class="block mb-2 text-sm font-medium"
                    >note</label
                >
                <textarea
                    type="text"
                    v-model="form.note"
                    name="category"
                    id="category"
                    class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:text-slate-900 dark:border-slate-600"
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
import Multiselect from '@vueform/multiselect';

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
            consulters: [],
            reasons: [],
            form: {
                patient: this.currentPatient.id,
                duration: '',
                code: '',
                consultation_by: [],
                consultation_reason: '',
                conversation_topics: '',
                recommendations: '',
                recommendation_issued: '',
                others: '',
                note: ''
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post(
                    '/api/documentation/telephone_consultations/create/',
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
    async mounted() {
        const response_doctors = await axios.get('/api/doctors/');
        this.consulters = response_doctors.data.map((doctors) => ({
            value: doctors.id,
            label: doctors.username
        }));
    },
    created() {
        axios
            .get('/api/documentation/consultation_reason_choices/')
            .then((response) => {
                this.reasons = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
    }
};
</script>
