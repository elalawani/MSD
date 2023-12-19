<template>
    <suspense>
        <template #default>
            <div
                class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2"
            >
                <div class="w-full bg-sky-700">
                    <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                        Konsultation der/ des Patient
                    </h1>
                </div>
                <div v-if="consultations.length">
                    <div class="flex flex-row justify-between container px-4">
                        <select
                            v-model="selected"
                            class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit"
                        >
                            <option
                                v-for="(_, index) in consultations"
                                :value="index"
                                :key="index"
                            >
                                sehe Dokumentation Nr: {{ index + 1 }}
                            </option>
                        </select>
                    </div>
                    <div
                        v-for="(consultation, index) in consultations"
                        class="flex justify-start items-start"
                    >
                        <table
                            v-if="index === selected"
                            class="rounded text-sm text-left text-slate-500 dark:text-slate-100 w-full"
                        >
                            <tbody>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        code
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.code }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-1/4"
                                    >
                                        hinzugefügt von
                                    </th>
                                    <td class="pl-2 py-4 flex flex-row">
                                        {{ consultation.created_by.username }}
                                    </td>
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-1/4"
                                    >
                                        role
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{ consultation.documentation_role }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        dauer
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.duration }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        erstellt sm
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.created_at }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Arzt-Initialen
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.doctor_initials }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Entscheidungen
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.decisions }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Grund der Aufnahme
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.reason_for_admission }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Krankenhauseinweisung erforderlich
                                    </th>
                                    <td
                                        v-if="
                                            consultation.hospital_admission_required ===
                                            true
                                        "
                                        class="pl-2 py-4"
                                    >
                                        Ja
                                    </td>
                                    <td v-else class="pl-2 py-4">Nein</td>
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Kliniktermin erforderlich
                                    </th>
                                    <td
                                        v-if="
                                            consultation.clinic_appointment_required ===
                                            true
                                        "
                                        class="pl-2 py-4"
                                    >
                                        Ja
                                    </td>
                                    <td v-else class="pl-2 py-4">Nein</td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Grund für den Kliniktermin
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{
                                            consultation.reason_for_clinic_appointment
                                        }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Maßnahmen nach Vereinbarung
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{
                                            consultation.measures_after_appointment
                                        }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Messungen durchgeführt
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.measures_taken }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        note
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ consultation.note }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div v-else class="text-4xl flex h-96 justify-center items-end">
                    keine Data
                </div>
            </div>
        </template>
        <template #fallback> loading ... </template>
    </suspense>
</template>
<script setup>
import { useDocumentationsStore } from '@/stores/documentation/documentation';
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const consultation = useDocumentationsStore();
const patient_id = useRoute().params.id;

const fetchData = async () => {
    await consultation.get_consultation(patient_id);
};
onMounted(fetchData);

const consultations = computed(() => consultation.consultation);
let selected = ref(consultations.value.length - 1);
watch(
    consultations,
    async (newConsultations) => {
        selected.value = newConsultations.length - 1;
    },
    { immediate: true }
);
</script>
