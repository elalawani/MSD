<template>
    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 class="text-xl font-bold leading-tight tracking-tight md:text-2xl">
            add Parkinson
        </h1>
        <form class="flex flex-col w-full" @submit.prevent="submitForm">
            <div class="flex flex-row items-center mb-8">
                <div class="flex flex-col w-4/5">
                    <label
                        for="tremor_severity"
                        class="block mb-2 text-sm font-medium"
                        >tremor_severity</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="formData.tremor_severity"
                            name="tremor_severity"
                            id="tremor_severity"
                            class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="tremor_severity Rate"
                        />
                    </div>
                </div>
                <div class="flex flex-col w-4/5">
                    <label
                        for="gait_speed"
                        class="block mb-2 text-sm font-medium"
                        >gait_speed</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="formData.gait_speed"
                            name="gait_speed"
                            id="gait_speed"
                            class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="gait_speed"
                        />
                    </div>
                </div>
                <div class="flex flex-col w-4/5">
                    <label
                        for="daily_assessment"
                        class="block mb-2 text-sm font-medium"
                        >daily_assessment</label
                    >
                    <div class="flex flex-row items-center mr-12">
                        <input
                            type="number"
                            v-model="formData.daily_assessment"
                            name="daily_assessment"
                            id="daily_assessment"
                            class="border text-slate-50 border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 dark:border-slate-600"
                            placeholder="daily_assessment"
                        />
                    </div>
                </div>

                <div class="ml-10 flex flex-col w-full">
                    <label
                        for="status"
                        class="block mb-2 text-sm font-medium pointer-events-none"
                        >status</label
                    >
                    <input
                        type="text"
                        v-model="formData.status"
                        name="status"
                        id="status"
                        class="border pointer-events-none border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600"
                        placeholder="Completed"
                    />
                </div>
            </div>
            <div class="flex flex-row w-full justify-around items-center">
                <div class="flex flex-col w-full">
                    <label
                        for="code"
                        class="block mb-2 text-sm font-medium pointer-events-none"
                        >code</label
                    >
                    <input
                        type="text"
                        v-model="formData.code"
                        name="code"
                        id="code"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600 pointer-events-none"
                        placeholder="HRT001"
                    />
                </div>
                <div class="w-full flex-col flex">
                    <label
                        for="category"
                        class="block mb-2 text-sm font-medium pointer-events-none"
                        >category</label
                    >
                    <input
                        type="text"
                        v-model="formData.category"
                        name="category"
                        id="category"
                        class="border border-gray-300 sm:text-sm rounded-lg focus:border-sky-600 block p-2.5 dark:bg-slate-700 text-slate-500 dark:border-slate-600 pointer-events-none"
                        placeholder="Heart Rate"
                    />
                </div>
            </div>
        </form>
        <button
            @click="submitForm"
            class="px-5 py-3 dark:bg-sky-900 bg-sky-700 hover:bg-sky-500 dark:hover:bg-sky-700 text-slate-50 w-fit rounded-xl"
        >
            send
        </button>
    </div>
</template>
<script>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { computed, onMounted, ref, watch } from 'vue';
import { useToastStore } from '@/stores/toast';
import router from '@/router';
import { usePatientStore } from '@/stores/patient/patient';

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
            formData: {
                tremor_severity: '',
                gait_speed: '',
                daily_assessment: '',
                status: 'Completed',
                code: 'PKN001',
                category: 'Parkinson',
                patient: this.currentPatient.id
            }
        };
    },
    methods: {
        submitForm() {
            axios
                .post('/api/sensor/parkinson/', this.formData)
                .then((response) => {
                    this.toastStore.showToast(
                        5000,
                        'measurement added',
                        'border border-green-500 bg-green-100 text-green-900'
                    );
                    router.push({
                        path: `/details/${this.currentPatient.id}/sensor`
                    });
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    }
};
</script>
