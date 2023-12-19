<template>
    <suspense>
        <template #default>
            <div
                class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2"
            >
                <div class="w-full bg-sky-700">
                    <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                        Eingangsuntersuchung in der Praxis/ Klinik
                    </h1>
                </div>
                <div v-if="examinations.length">
                    <div class="flex flex-row justify-between container px-4">
                        <select
                            v-model="selected"
                            class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit"
                        >
                            <option
                                v-for="(_, index) in examinations"
                                :value="index"
                                :key="index"
                            >
                                sehe Dokumentation Nr: {{ index + 1 }}
                            </option>
                        </select>
                    </div>
                    <div
                        v-for="(examination, index) in examinations"
                        :key="index"
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
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-1/4"
                                    >
                                        hinzugefügt von
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{ examination.created_by.username }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Dauer
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{ examination.duration }}
                                        {{ examination.duration }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        erstellt am
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{ examination.created_at }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Praxis
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{ examination.centrePick }}
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
                                    <td class="pl-2 py-4">
                                        {{ examination.note }}
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
        <template #fallback>
            <div>loding ...</div>
        </template>
    </suspense>
</template>
<script setup>
import { useDocumentationsStore } from '@/stores/documentation/documentation';
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const initialExamination = useDocumentationsStore();
const patient_id = useRoute().params.id;

const fetchData = async () => {
    await initialExamination.get_initial_examinations(patient_id);
};
onMounted(fetchData);

const examinations = computed(() => initialExamination.initial_examinations);
const selected = ref(examinations.value.length - 1);
watch(
    examinations,
    async (newExaminations) => {
        selected.value = newExaminations.length - 1;
    },
    { immediate: true }
);
</script>
