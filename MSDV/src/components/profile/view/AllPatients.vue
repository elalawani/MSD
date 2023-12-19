<template>
    <div
        class="flex flex-col bg-slate-100 shadow-lg dark:bg-slate-700 rounded-lg overflow-auto h-96"
    >
        <div class="flex flex-row border-b justify-between mx-4 p-4">
            <div class="text-2xl">Patienten</div>
        </div>
        <div
            v-for="(patient, index) in patientsView"
            :key="index"
            class="mx-4 flex flex-col space-y-6"
        >
            <div
                class="flex flex-col space-y-2 pt-3"
                :class="
                    index + 1 === patientsView.length
                        ? ''
                        : 'border-b border-b-slate-400'
                "
            >
                <div class="flex flex-row space-x-2">
                    <label class="font-bold"> Name: </label>
                    <div>{{ patient.first_name }} {{ patient.last_name }}</div>
                </div>
                <div
                    class="flex flex-row space-x-2"
                    v-if="patient.reason_of_visiting.length"
                >
                    <label class="font-bold"> gründ für den Besuch:</label>
                    <div>{{ patient.reason_of_visiting }}</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { usePatientStore } from '@/stores/patient/patient';
import { computed, onMounted } from 'vue';
import ProfileAddressUpdate from '@/components/profile/updat/ProfileAddressUpdate.vue';

const patients = usePatientStore();

const getAllPatients = async () => {
    await patients.getAllPatients();
};

onMounted(getAllPatients);

const patientsView = computed(() => patients.patient_list);
</script>
