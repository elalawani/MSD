<template>
    <suspense>
        <template #default>
            <div
                class="left flex flex-col h-full border-r border-r-slate-500 w-full p-2"
            >
                <div class="w-full bg-sky-700">
                    <h1 class="flex justify-around text-[min(10vw,30px)] p-4">
                        Instruktion in Wearable und App (57203A02)
                    </h1>
                </div>
                <div v-if="instructionWearables.length">
                    <div class="flex flex-row justify-between container px-4">
                        <select
                            v-model="selected"
                            class="flex justify-end items-end py-2 my-1 rounded bg-sky-900 px-1 w-fit"
                        >
                            <option
                                v-for="(_, index) in instructionWearables"
                                :value="index"
                                :key="index"
                            >
                                sehe Dokumentation Nr: {{ index + 1 }}
                            </option>
                        </select>
                    </div>
                    <div
                        v-for="(
                            instructionWearable, index
                        ) in instructionWearables"
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
                                        {{ instructionWearable.code }}
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
                                        {{
                                            instructionWearable.created_by
                                                .username
                                        }}
                                    </td>
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-1/4"
                                    >
                                        role
                                    </th>
                                    <td class="pl-2 py-4">
                                        {{
                                            instructionWearable.documentation_role
                                        }}
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
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ instructionWearable.duration }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        Erstellt am
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ instructionWearable.created_at }}
                                    </td>
                                </tr>
                                <tr
                                    class="border dark:bg-slate-800 dark:border-slate-700"
                                >
                                    <th
                                        class="pl-2 py-4 dark:bg-sky-700 bg-sky-600 text-slate-50 w-fit"
                                    >
                                        center
                                    </th>
                                    <td colspan="3" class="pl-2 py-4">
                                        {{ instructionWearable.centrePick }}
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
                                        {{ instructionWearable.note }}
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

const instructionWearable = useDocumentationsStore();
const patient_id = useRoute().params.id;

const fetchData = async () => {
    await instructionWearable.get_instruction_wearables(patient_id);
};
onMounted(fetchData);

const instructionWearables = computed(
    () => instructionWearable.instruction_wearables
);
const selected = ref(instructionWearables.value.length - 1);
watch(
    instructionWearables,
    async (newInstructionWearables) => {
        selected.value = newInstructionWearables.length - 1;
    },
    { immediate: true }
);
</script>
