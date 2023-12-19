<template>
    <div class="mt-14 mx-4">
        <div class="text-2xl font-bold">
            <span v-if="userStore.user.role === 'DR'">Dr. </span>
            <router-link to="/profile">
                {{ userStore.user.username }}
            </router-link>
        </div>
        <div class="flex flex-col sm:flex-row justify-around mt-20">
            <div
                v-if="todos"
                class="w-full sm:w-2/5 mb-4 dark:border-none shadow dark:bg-slate-800 p-2 rounded"
            >
                <div class="flex justify-between">
                    <span> meine Aufgaben </span>
                    <router-link
                        to="/todolist"
                        class="text-sky-500 hover:font-bold"
                    >
                        alle Aufgaben
                    </router-link>
                </div>
                <div>
                    <hr />
                    <ul class="list divide-y divide-slate-700">
                        <li
                            class="my-3"
                            v-for="(myTodo, index) in todos"
                            :key="index"
                        >
                            <router-link
                                class="hover:font-bold p-2"
                                to="/todolist"
                                v-if="index < 3"
                                >{{ index + 1 }}. {{ myTodo.name }}
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
            <div
                v-if="patients.length"
                class="w-full sm:w-2/5 mb-4 dark:border-none shadow dark:bg-slate-800 p-2 rounded-lg"
            >
                <div class="flex justify-between">
                    <span> meine Patienten </span>
                    <router-link
                        class="text-sky-500 hover:font-bold"
                        to="/view"
                    >
                        suchen
                    </router-link>
                    <router-link
                        v-if="userStore.user.role === 'ST'"
                        class="text-sky-500 hover:font-bold"
                        to="/create_patient"
                    >
                        &plus; hinzufügen
                    </router-link>
                </div>
                <div>
                    <hr />
                    <ul class="list">
                        <li
                            class="my-3"
                            v-for="(patient, index) in patients"
                            :key="index"
                        >
                            <router-link
                                :to="`details/${patient.id}/info`"
                                v-if="index < 3"
                            >
                                {{ patient.first_name }}
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="flex flex-col sm:flex-row justify-around mt-20">
            <div
                class="w-full sm:w-2/5 mb-4 dark:border-none shadow dark:bg-slate-800 p-2 rounded-lg"
            >
                <div class="flex justify-between">
                    <span> meine Termine </span>
                    <router-link to="/" class="text-sky-500 hover:font-bold">
                        alle Termine
                    </router-link>
                </div>
                <div>
                    <hr />
                    <ul class="list divide-y divide-slate-700">
                        <li
                            class="my-3"
                            v-for="(myTodo, index) in todos"
                            :key="index"
                        >
                            <router-link
                                class="hover:font-bold p-2"
                                to="/"
                                v-if="index < 3"
                                >{{ index + 1 }}. {{ myTodo.name }}
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
            <div
                v-if="patients.length"
                class="w-full sm:w-2/5 mb-4 dark:border-none shadow dark:bg-slate-800 p-2 rounded-lg"
            >
                <div class="flex justify-between">
                    <span> meine Nachrichten </span>
                    <span class="mr-4"> erstellt am: </span>
                </div>
                <div>
                    <hr />
                    <ul class="list">
                        <li
                            class="my-3"
                            v-for="(conversations, index) in conversation"
                            :key="index"
                        >
                            <div class="flex justify-between" v-if="index < 3">
                                <div class="relative group">
                                    <router-link
                                        :to="`details/${conversations.patient.id}/conversation`"
                                    >
                                        conversations für
                                        {{ conversations.patient.first_name }}
                                    </router-link>
                                    <div
                                        class="absolute bg-slate-700 z-40 p-4 rounded-xl hidden group-hover:block"
                                    >
                                        Gesprächsteilnehmer
                                        <div
                                            class="font-extralight flex flex-col hover:text-sky-600"
                                            v-for="(
                                                users, index
                                            ) in conversations.users"
                                            :key="index"
                                        >
                                            {{ users.username }}
                                        </div>
                                    </div>
                                </div>
                                <span class="mr-4">
                                    {{ dateTime(conversations.created_at) }}
                                </span>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { useUserStore } from '@/stores/accounts/user';
import { useTodolistStore } from '@/stores/todolist/todolist';
import { computed, onMounted, ref } from 'vue';
import { usePatientStore } from '@/stores/patient/patient';
import { useConversationStore } from '@/stores/converstaion/conversation';
import dateTime from '../setUp/global/date-filter';
const userStore = useUserStore();
const todoStore = useTodolistStore();
const patientStore = usePatientStore();
const conversationStore = useConversationStore();
const getTasks = async () => {
    await todoStore.getTasks();
};
const getPatient = async () => {
    await patientStore.getAllPatients();
};
const getConversation = async () => {
    await conversationStore.getConversation();
};

onMounted(getTasks);
onMounted(getPatient);
onMounted(getConversation);
const conversation = computed(() => conversationStore.conversations);
const patients = computed(() => patientStore.patient_list);
const todos = computed(() => todoStore.tasks);
</script>
