<template>
    <div
        class="text-3xl font-bold p-4 ml-2 text-slate-700 dark:text-slate-50 underline"
    >
        Alle abgeschlossenen Aufgaben
    </div>
    <div v-if="!patientDocu.length">leer</div>
    <div
        v-else
        v-for="(docu, index) in patientDocu"
        :key="index"
        class="flex flex-col dark:bg-slate-700 m-4 rounded-xl text-slate-900 dark:text-slate-50 shadow-lg"
    >
        <div class="text-xl mt-3 ml-6 pb-3">
            {{ index + 1 }}: {{ docu.name }}
        </div>
        <div class="flex flex-row border-t border-t-slate-500 p-1">
            <div class="font-light text-xs ml-4">
                abgeshlossen von : {{ docu.user.username }}
            </div>
        </div>
    </div>
</template>
<script setup>
import { useDocumentationsStore } from '@/stores/documentation/documentation';
import { usePatientStore } from '@/stores/patient/patient';
import { computed, onMounted } from 'vue';
const patient_id = usePatientStore().patient.id;

const docu = useDocumentationsStore();

const fetchData = async () => {
    await docu.get_individual_docu(patient_id);
};
onMounted(fetchData);

const patientDocu = computed(() => docu.patientDocu);
</script>
