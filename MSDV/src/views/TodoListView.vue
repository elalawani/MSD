<template>
    <div class="container mx-auto mt-10 p-4">
        <div class="flex flex-col justify-center">
            <h1 class="text-4xl font-extrabold mb-4">Todo</h1>
            <ul class="flex flex-col overflow-auto">
                <li
                    v-for="(task, index) in tasks"
                    :key="index"
                    class="px-2 py-4 shadow dark:bg-slate-800 mb-1 flex flex-row justify-between items-center hover:border-b border-b-slate-500 hover:shadow-inner"
                >
                    <div
                        v-if="!task.editing"
                        class="py-2 px-4 mb-4 rounded cursor-pointer"
                        @click="editTask(task, index)"
                    >
                        <span>{{ index + 1 }} - </span>
                        <span
                            :class="
                                task.completed === true ? 'line-through' : ''
                            "
                            >{{ task.name }}</span
                        >
                        <div class="mt-3">{{ dateTime(task.created_at) }}</div>
                    </div>

                    <input
                        v-else
                        :ref="`editInput-${index}`"
                        v-model="taskName"
                        class="bg-slate-800 border border-gray-300 rounded py-2 px-4 mb-4 w-full"
                        @blur="updateTask(task.id)"
                        @keydown.enter="updateTask(task.id)"
                    />
                    <div class="flex flex-row">
                        <button
                            @click="deleteTask(task.id)"
                            class="text-red-900 p-3 hover:text-red-700"
                        >
                            Delete
                        </button>
                        <button
                            v-if="task.completed === false"
                            @click="doneTasks(task)"
                            class="text-sky-900 p-3 hover:text-sky-700"
                        >
                            Done
                        </button>
                    </div>
                </li>
            </ul>
            <div class="mt-4 shadow-lg p-5 rounded">
                <input
                    type="text"
                    v-model="newTask"
                    class="border border-gray-300 rounded w-full py-2 px-4 mb-4 text-slate-900"
                    placeholder="deine neue Aufgabe"
                    @keydown.enter="addTask"
                />
                <div v-if="error.length" class="text-xs text-red-500 mb-4">
                    {{ error }}
                </div>
                <button
                    @click="addTask"
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                    Add Task
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useTodolistStore } from '@/stores/todolist/todolist';
import dateTime from '../setUp/global/date-filter';
import { useToastStore } from '@/stores/toast';

export default {
    data() {
        return {
            tasks: [],
            newTask: '',
            taskName: '',
            error: '',
            noPatientError: ''
        };
    },
    methods: {
        dateTime,
        editTask(task, index) {
            this.tasks.forEach((t) => {
                if (t !== task) t.editing = false;
            });
            task.editing = true;
            this.taskName = task.name;
            this.$nextTick(() => {
                this.$refs[`editInput-${index}`][0].focus();
            });
        },
        async doneTasks(task) {
            this.noPatientError = '';
            if (task.patient) {
                await axios
                    .post(
                        '/api/documentation/individual/create/',
                        {
                            name: task.name,
                            patient: task.patient
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }
                    )
                    .then(async (response) => {
                        await axios
                            .put(`api/todo/update/${task.id}/`, {
                                name: task.name,
                                completed: true
                            })
                            .then(() => {
                                this.get_tasks();
                                useToastStore().showToast(
                                    5000,
                                    'Die Aufgabe wurde erfolgreich auf „Erledigt“ gesetzt ' +
                                        'und im Patientendokument aufgeführt',
                                    'border border-green-500 bg-green-100 text-green-900'
                                );
                            });
                    })
                    .catch((e) => {
                        console.error(e);
                    });
            } else {
                this.noPatientError =
                    'das Task hat keine patient es kann nur deletet';
                useToastStore().showToast(
                    1000,
                    this.noPatientError,
                    'border border-red-500 bg-red-100 text-red-900'
                );
            }
        },
        updateTask(taskId) {
            axios
                .put(`api/todo/update/${taskId}/`, {
                    name: this.taskName
                })
                .then((response) => {
                    let task = this.tasks.find((task) => task.id === taskId);
                    if (task) {
                        task.name = this.taskName;
                        task.editing = false;
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        deleteTask(index) {
            axios
                .delete(`api/todo/delete/${index}/`)
                .then((response) => {
                    this.get_tasks();
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        addTask() {
            if (this.newTask !== '') {
                axios
                    .post('api/todo/create/', {
                        name: this.newTask
                    })
                    .then((response) => {
                        this.newTask = '';
                        this.error = '';
                        this.get_tasks();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            } else {
                this.error = 'bitte eine Aufgabe eingeben';
            }
        },
        async get_tasks() {
            const store = useTodolistStore();
            await store.getTasks().then(() => {
                this.tasks = store.tasks;
            });
        }
    },
    mounted() {
        this.get_tasks();
    }
};
</script>
